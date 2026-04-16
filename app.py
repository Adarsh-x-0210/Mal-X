from flask import Flask, request, jsonify, render_template
import os
import hashlib
import math
import re

app = Flask(__name__)

# Malware signature database (demo)
MALWARE_SIGNATURES = {
    "e99a18c428cb38d5f260853678922e03": "Trojan.Generic",
    "5d41402abc4b2a76b9719d911017c592": "Virus.Test",
    "d41d8cd98f00b204e9800998ecf8427e": "Empty.File.Threat",
}

SUSPICIOUS_EXTENSIONS = {
    '.exe', '.bat', '.cmd', '.scr', '.com', '.pif',
    '.msi', '.jar', '.apk', '.bin', '.dmg'
}

SUSPICIOUS_KEYWORDS = [
    b'powershell', b'cmd.exe', b'wscript', b'cscript',
    b'regsvr32', b'mshta', b'rundll32', b'certutil', b'bitsadmin'
]


# ---------------- HASHING ---------------- #

def calculate_hashes(file_bytes):
    return {
        "md5": hashlib.md5(file_bytes).hexdigest(),
        "sha256": hashlib.sha256(file_bytes).hexdigest()
    }


# ---------------- ENTROPY ---------------- #

def calculate_entropy(data):
    if not data:
        return 0

    entropy = 0
    for x in range(256):
        p_x = data.count(bytes([x])) / len(data)
        if p_x > 0:
            entropy -= p_x * math.log2(p_x)
    return entropy


# ---------------- STRING EXTRACTION ---------------- #

def extract_strings(file_bytes):
    return re.findall(rb'[ -~]{4,}', file_bytes)


# ---------------- ANALYSIS ENGINE ---------------- #

def analyze_file(file_bytes, filename):
    hashes = calculate_hashes(file_bytes)
    file_extension = os.path.splitext(filename)[1].lower()
    file_size = len(file_bytes)

    score = 0
    indicators = []

    # 1. Signature check
    if hashes["md5"] in MALWARE_SIGNATURES:
        score += 90
        indicators.append("Known malware signature match")

    # 2. Extension check
    if file_extension in SUSPICIOUS_EXTENSIONS:
        score += 30
        indicators.append(f"Suspicious extension: {file_extension}")

    # 3. Size anomaly
    if file_size > 100 * 1024 * 1024:
        score += 20
        indicators.append("Unusually large file")
    elif file_size < 10:
        score += 40
        indicators.append("Unusually small file")

    # 4. Keyword detection (on extracted strings)
    extracted = extract_strings(file_bytes)
    extracted_lower = [s.lower() for s in extracted]

    found_keywords = []
    for kw in SUSPICIOUS_KEYWORDS:
        for s in extracted_lower:
            if kw in s:
                found_keywords.append(kw.decode())
                break

    if found_keywords:
        score += 40
        indicators.append(f"Suspicious commands: {', '.join(found_keywords)}")

    # 5. Entropy check
    entropy = calculate_entropy(file_bytes)
    if entropy > 7.5:
        score += 30
        indicators.append("High entropy (packed/encrypted file)")

    # ---------------- VERDICT ---------------- #

    if score >= 80:
        risk = "CRITICAL"
        malicious = True
    elif score >= 50:
        risk = "HIGH"
        malicious = True
    elif score >= 20:
        risk = "MEDIUM"
        malicious = False
    else:
        risk = "LOW"
        malicious = False

    return {
        "file": {
            "name": filename,
            "size": file_size,
            "extension": file_extension
        },
        "hashes": hashes,
        "analysis": {
            "entropy": round(entropy, 2),
            "score": score
        },
        "indicators": indicators,
        "verdict": {
            "malicious": malicious,
            "risk": risk,
            "confidence": min(score, 100)
        }
    }


# ---------------- ROUTES ---------------- #

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def scan_file():
    file = request.files.get('file')

    if not file:
        return jsonify({'error': 'No file provided'}), 400

    try:
        file_bytes = file.read()
        filename = file.filename

        if len(file_bytes) == 0:
            return jsonify({'error': 'Empty file'}), 400

        result = analyze_file(file_bytes, filename)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': f'Scan failed: {str(e)}'}), 500


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'running',
        'version': '2.0.0',
        'features': [
            'Multi-hash detection',
            'Entropy analysis',
            'Heuristic scoring',
            'Keyword extraction'
        ]
    })


# ---------------- RUN ---------------- #

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)