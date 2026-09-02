from flask import Flask, request, redirect, url_for, render_template_string
from urllib.parse import urlparse
import requests

app = Flask(__name__)
app.secret_key = "vapt-demo-secret"

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>VAPT Lab - Login</title>
<style>
body{margin:0;background:#0b1220;color:white;font-family:Arial;display:flex;
justify-content:center;align-items:center;height:100vh}
.box{background:#111c30;padding:40px;border-radius:15px;width:350px;
box-shadow:0 0 30px #000}
h1{text-align:center;color:#38bdf8}
input{width:100%;padding:12px;margin:10px 0;border:0;border-radius:8px;
box-sizing:border-box}
button{width:100%;padding:13px;background:#0ea5e9;color:white;border:0;
border-radius:8px;font-weight:bold;cursor:pointer}
.error{color:#fb7185;text-align:center}
</style>
</head>
<body>
<div class="box">
<h1>🛡️ VAPT LAB</h1>
<p style="text-align:center">Security Testing Dashboard</p>
<form method="POST">
<input name="username" placeholder="Username" required>
<input name="password" type="password" placeholder="Password" required>
<button>LOGIN</button>
</form>
{% if error %}<p class="error">{{error}}</p>{% endif %}
</div>
</body>
</html>
"""

DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>VAPT Security Dashboard</title>
<style>
body{margin:0;background:#08111f;color:#e5e7eb;font-family:Arial}
header{padding:20px 40px;background:#101b2d;border-bottom:1px solid #26364d}
header h1{margin:0;color:#38bdf8}
.container{padding:35px}
.card{background:#111c30;padding:25px;border-radius:15px;margin-bottom:20px}
input{padding:13px;width:70%;border:0;border-radius:8px}
button{padding:13px 20px;background:#0ea5e9;color:white;border:0;
border-radius:8px;font-weight:bold;cursor:pointer}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.stat{background:#111c30;padding:25px;border-radius:15px}
.stat h2{font-size:32px;color:#38bdf8}
.badge{padding:8px 12px;border-radius:20px;background:#16a34a}
.warning{color:#fbbf24}.danger{color:#fb7185}
</style>
</head>
<body>
<header>
<h1>🛡️ VAPT Security Dashboard</h1>
<p>Web Application Vulnerability Assessment Lab</p>
</header>

<div class="container">

<div class="card">
<h2>🔎 Target Scanner</h2>
<form method="POST">
<input name="target" placeholder="http://127.0.0.1:5000" required>
<button>Start VAPT Testing</button>
</form>
</div>

{% if result %}
<div class="grid">
<div class="stat">
<p>Threat Score</p>
<h2>{{result.score}}/100</h2>
</div>
<div class="stat">
<p>Security Status</p>
<h2>{{result.status}}</h2>
</div>
<div class="stat">
<p>Target</p>
<h3>{{result.target}}</h3>
</div>
</div>

<div class="card">
<h2>📊 Scan Results</h2>
<p>HTTP Status: <b>{{result.http_status}}</b></p>
<p>Server Header: <b>{{result.server}}</b></p>
<p>HTTPS: <b>{{result.https}}</b></p>
<p>Security Headers: <b>{{result.headers}}</b></p>

{% for alert in result.alerts %}
<p class="warning">⚠️ {{alert}}</p>
{% endfor %}
</div>
{% endif %}

</div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Demo credentials for local lab only
        if username == "admin" and password == "admin123":
            return redirect(url_for("dashboard"))

        error = "Invalid username or password"

    return render_template_string(LOGIN_HTML, error=error)


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    result = None

    if request.method == "POST":
        target = request.form.get("target", "").strip()

        try:
            parsed = urlparse(target)

            if parsed.scheme not in ["http", "https"] or not parsed.netloc:
                raise ValueError("Invalid URL")

            response = requests.get(target, timeout=5)

            security_headers = [
                "X-Frame-Options",
                "X-Content-Type-Options",
                "Content-Security-Policy",
                "Strict-Transport-Security"
            ]

            missing = [
                h for h in security_headers
                if h not in response.headers
            ]

            score = min(100, len(missing) * 20)

            alerts = []
            for header in missing:
                alerts.append(f"Missing security header: {header}")

            result = {
                "target": target,
                "http_status": response.status_code,
                "server": response.headers.get("Server", "Not disclosed"),
                "https": "Enabled" if parsed.scheme == "https" else "Not enabled",
                "headers": f"{len(security_headers)-len(missing)}/{len(security_headers)} present",
                "score": score,
                "status": "LOW RISK" if score < 40 else "MEDIUM RISK" if score < 70 else "HIGH RISK",
                "alerts": alerts
            }

        except Exception as e:
            result = {
                "target": target,
                "http_status": "Error",
                "server": "-",
                "https": "-",
                "headers": "-",
                "score": 100,
                "status": "SCAN ERROR",
                "alerts": [str(e)]
            }

    return render_template_string(DASHBOARD_HTML, result=result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)