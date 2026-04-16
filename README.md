# 🛡️ MAL-X — AI Powered Malware Detection System

![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3.3-black?logo=flask)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

---

## 🚀 Overview

**MAL-X** is a web-based malware detection system that analyzes files using a combination of:

- Signature-based detection  
- Heuristic analysis  
- Entropy analysis (advanced)  
- Suspicious behavior detection  

It provides **real-time threat analysis**, confidence scoring, and a modern dashboard UI.

---

## 📸 Features

✅ Signature Detection (MD5 + SHA256)  
✅ File Extension Analysis  
✅ Entropy-based Detection (packed/encrypted files)  
✅ Suspicious Keyword Detection  
✅ Heuristic Risk Scoring System  
✅ Clean Dashboard UI  
✅ File Hash Generation  
✅ Indicator-based Threat Explanation  

---

## 🏗️ Project Structure
Mal-X/
│
├── app.py
├── templates/
│ └── index.html
├── requirements.txt
├── vercel.json
└── README.md



---

## ⚙️ Installation & Setup

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Run the application
Bash

python app.py
3️⃣ Open in browser

http://localhost:5000
🎯 How It Works
Upload a file

System extracts hashes & metadata

Runs detection checks:

Signature match

Extension analysis

Entropy calculation

Keyword detection

Generates risk score

Displays results in dashboard

📊 Detection Logic
Feature	Description
Signature Matching	Known malware hash detection
Heuristic Analysis	Rule-based suspicious behavior
Entropy Check	Detects packed/encrypted files
Keyword Scan	Detects command execution patterns
Risk Scoring	Combines all signals into final verdict

🚨 Risk Levels
Level	Meaning
CRITICAL 🚨	Known malware detected
HIGH 🔴	Strong malicious indicators
MEDIUM 🟡	Suspicious behavior
LOW 🟢	Likely safe

📈 Confidence Levels
90–100% → Very High

70–89% → High

50–69% → Medium

<50% → Low

🛠️ Requirements
Python 3.6+

Flask

Modern Browser

⚠️ Disclaimer
This project is built for educational and demonstration purposes only.

It should not be used as a replacement for enterprise-grade security tools.

🧠 Future Improvements
🔍 VirusTotal API integration

📊 Graph-based threat visualization

🗂 Scan history tracking

⚛️ React frontend upgrade

🧠 Machine learning-based detection

🤝 Contributing
Contributions are welcome!

Feel free to fork the repo and submit a pull request.

⭐ If you like this project
Give it a star ⭐ on GitHub!

👨‍💻 Author
Adarsh Ajnadkar