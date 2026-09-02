# VAPT Web Application Framework

A compact academic Vulnerability Assessment and Penetration Testing (VAPT) framework built with Python and Flask.

## What it demonstrates
- Professional VAPT dashboard
- Local web-application target validation
- HTTP security-header assessment
- Server-banner disclosure check
- Cookie security flag checks
- Harmless reflected-input marker check
- Severity classification and risk score
- Evidence + remediation recommendations

## Safety
This demo intentionally accepts **only localhost targets**:
- `http://127.0.0.1:5001`
- `http://localhost:5001`
- `http://[::1]:5001`

It does not perform exploitation, credential attacks, brute force, destructive testing, or scanning of third-party systems.

## Windows 11 setup

1. Install Python 3.11+.
2. Open this project folder in VS Code.
3. Open Terminal.
4. Create a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

5. Install dependencies:

```powershell
pip install -r requirements.txt
```

6. Start the dashboard:

```powershell
python app.py
```

7. Open:
`http://127.0.0.1:5000`

## Demo target

For a visible demo, run a second local Flask application on port 5001, then scan:

`http://127.0.0.1:5001`

The scanner is designed as an academic framework rather than a replacement for professional penetration-testing tools.
