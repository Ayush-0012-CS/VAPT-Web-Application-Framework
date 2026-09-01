# VAPT-Web-Application-Framework
A Python-based VAPT framework for assessing web application security, detecting common vulnerabilities, and generating security risk insights.
# Demo Login
*Username:admin  
*Password:admin123 

# How to Run

1. Install Python.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run:
   `python app.py`
4. Open `http://127.0.0.1:5000`

# Project Motto

> Identify Vulnerabilities. Assess Risks. Strengthen Security.

# How It Works

1. Login – User logs into the VAPT Lab using the demo credentials.
2. Enter Target – User enters the web application URL to be assessed.
3. URL Validation – The framework validates the target URL.
4. Security Scan – It sends an HTTP request and checks the application's response.
5. Header Analysis – Important security headers are checked for missing configurations.
6. Risk Assessment – A threat score is calculated based on the missing security headers.
7. Results – The dashboard displays the HTTP status, HTTPS status, server information, security-header status, risk level, and alerts.

# Workflow

Login → Enter Target URL → Validate Target → Scan → Analyze Security Headers → Calculate Risk → Display Results.

#Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Requests Library

# Security Checks

The framework currently performs:

- HTTP response status check
- HTTPS availability check
- Server header inspection
- Security header analysis
- Missing security header detection
- Risk score calculation
- Security alerts generation

# Project Scope

This project is developed for academic and educational purposes. 
It demonstrates basic VAPT concepts and security-header assessment 
in a controlled local testing environment.

Only systems for which you have explicit permission should be tested.
