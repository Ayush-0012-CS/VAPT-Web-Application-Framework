# Submission Notes

## Project title
Vulnerability Assessment and Penetration Testing (VAPT) on a Web Application (Framework)

## Main objective
To build a controlled web-security assessment framework that identifies common configuration and input-handling weaknesses and presents evidence, severity, risk score, and remediation guidance through a dashboard.

## Technologies
Python, Flask, Requests, HTML, CSS

## Main modules
1. Target Validation
2. HTTP Security Header Assessment
3. Server Banner Disclosure
4. Cookie Security Checks
5. Reflected Input Marker Check
6. Severity & Risk Scoring
7. Dashboard Reporting.

 ##Demo Login Credentials
Use the following credentials for the academic demonstration:

**Username: admin
**Password: admin123

These credentials are for the local academic demo only. Do not use them in a production environment.
## Suggested demo flow
1. Run `python demo_target.py`
2. In another terminal run `python app.py`
3. Open `http://127.0.0.1:5000`
4. Enter `http://127.0.0.1:5001`
5. Click Start VAPT Scan
6. Explain findings and remediation recommendations.

## Viva points
- VAPT means Vulnerability Assessment and Penetration Testing.
- Vulnerability assessment identifies and prioritizes weaknesses.
- Penetration testing validates security weaknesses in a controlled manner.
- This project is intentionally non-destructive and limited to local systems.
