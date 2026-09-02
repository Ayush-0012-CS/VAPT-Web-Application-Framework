# 🛡️ VAPT Web Application Framework

A Python and Flask-based academic **Vulnerability Assessment and Penetration Testing (VAPT)** framework designed to demonstrate basic web application security testing in a controlled local environment.

---

## 📌 Project Overview

The **VAPT Web Application Framework** is an academic cybersecurity project that demonstrates how a web application can be assessed for common security weaknesses.

The framework provides a simple web dashboard where an authorized localhost target can be entered and checked using automated security assessment techniques.

The system presents security findings, risk score, severity, evidence, and remediation recommendations in an easy-to-understand format.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate the basic VAPT workflow:

- Target validation
- Security assessment
- Vulnerability identification
- Severity classification
- Risk-score calculation
- Evidence generation
- Remediation recommendations

---

## 🔐 Demo Login Credentials

Use the following credentials for the academic demonstration:

- **Username: admin
- **Password: admin123

> These credentials are for the local academic demo only. Do not use them in a production environment.

---

## 🛡️ Key Features

- 🔐 Login-based VAPT dashboard
- 🎯 Local target validation
- 🔎 HTTP security-header assessment
- 🖥️ Server-banner disclosure check
- 🍪 Cookie security-flag checks
- 🧪 Harmless reflected-input marker check
- ⚠️ Vulnerability severity classification
- 📊 Risk-score calculation
- 📝 Evidence generation
- 💡 Remediation recommendations
- 📋 Easy-to-understand scan results

---

## 🏗️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11+ | Backend programming |
| Flask | Web application framework |
| HTML5 | User interface |
| CSS3 | Dashboard styling |
| Windows 11 | Development platform |
| GitHub | Source-code management |

---

## 📂 Project Structure

```text
VAPT-Web-Application-Framework/
│
├── app.py
├── scanner.py
├── requirements.txt
├── index.html
├── style.css
├── README.md
└── PROJECT_NOTES.md


### File Description

| File | Purpose |
|---|---|
| `app.py` | Main Flask application and dashboard |
| `scanner.py` | Security assessment and scanning logic |
| `index.html` | Login/dashboard interface |
| `style.css` | Frontend styling |
| `requirements.txt` | Required Python packages |
| `README.md` | Project documentation |
| `PROJECT_NOTES.md` | Project development notes |

---

## 🔄 How the Project Works

The project follows this basic workflow:

```text
User
  ↓
Login
  ↓
VAPT Dashboard
  ↓
Enter Authorized Local Target
  ↓
Target Validation
  ↓
Security Checks
  ↓
Vulnerability Detection
  ↓
Severity Classification
  ↓
Risk Score
  ↓
Evidence
  ↓
Remediation Recommendation
```

---

## 📊 What the Framework Checks

The framework demonstrates basic checks such as:

### 1. Security Headers

Checks whether important HTTP security headers are present, including:

- X-Frame-Options
- X-Content-Type-Options
- Content-Security-Policy
- Strict-Transport-Security

### 2. Server Information

Checks whether server information is disclosed through HTTP response headers.

### 3. Cookie Security

Checks security-related cookie attributes where applicable.

### 4. Reflected Input

Uses a harmless test marker to demonstrate basic reflected-input detection.

### 5. Risk Assessment

The framework calculates a simple risk score based on detected security issues and classifies the result.

---

## 🚦 Risk Classification

The dashboard uses a simple risk classification:

| Score | Status |
|---|---|
| 0–39 | LOW RISK |
| 40–69 | MEDIUM RISK |
| 70–100 | HIGH RISK |

> The score is intended for academic demonstration and should not be treated as a professional vulnerability rating such as CVSS.

---

## 💻 Windows 11 Setup

### Step 1 — Install Python

Install **Python 3.11 or newer**.

### Step 2 — Open the Project

Open the project folder in **Visual Studio Code**.

### Step 3 — Create Virtual Environment

Open the VS Code terminal and run:

```bash
python -m venv venv
```

### Step 4 — Activate Virtual Environment

```bash
.\venv\Scripts\activate
```

### Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6 — Start the Application

```bash
python app.py
```

### Step 7 — Open the Dashboard

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧪 Demo Procedure

For the project demonstration:

1. Start the Flask application.
2. Open `http://127.0.0.1:5000`.
3. Login using:
   - Username: `admin`
   - Password: `admin123`
4. Enter an authorized localhost target.
5. Click **Start VAPT Testing**.
6. Wait for the security assessment.
7. Review the HTTP status and server information.
8. Review security-header results.
9. Check the risk score and security status.
10. Review alerts and recommended remediation.

---

## 🎯 Demo Target

For a controlled local demonstration, use: 
for demo check..
test...
https://vapt-web-application-framework-1.onrender.com

```text
http://127.0.0.1:5001
```

or:

```text
http://localhost:5001
```

The target application should be running locally before starting the scan.

---

## 🔒 Safety & Scope

This project is designed for **educational and authorized local testing**.

The intended scope is localhost testing.

The framework does not perform:

- Credential attacks
- Brute-force attacks
- Destructive testing
- Unauthorized exploitation
- Unauthorized scanning

Only test systems that you own or have explicit permission to assess.

---

## 📈 Expected Output

After a scan, the dashboard displays information such as:

- Target URL
- HTTP status
- Server information
- HTTPS status
- Security-header results
- Detected alerts
- Risk score
- Overall security status

This makes the results easy to understand during an academic demonstration.

---

## 🎓 Academic Purpose

This project demonstrates practical concepts related to:

- Web Application Security
- Vulnerability Assessment
- Penetration Testing Concepts
- Python Programming
- Flask Web Development
- HTTP Security
- Security Headers
- Risk Assessment
- Security Remediation

---

## 🌟 Project Motto

> **“Identify vulnerabilities, understand the risk, and improve web application security.”**

---


---

## 📜 Disclaimer

This project is developed strictly for **educational and academic purposes**.

It is intended to demonstrate basic VAPT concepts in a controlled local environment. The results produced by this framework are for learning and demonstration and should not be considered a complete professional security assessment.

Always obtain proper authorization before performing security testing on any system.

---

## ⭐ Project Summary

**VAPT Web Application Framework** is a Python-Flask based academic cybersecurity project that demonstrates the complete basic VAPT workflow — from target validation and security checks to vulnerability identification, risk scoring, evidence, and remediation recommendations.

The project provides a simple dashboard that helps students understand practical web application security testing in a controlled environment.
