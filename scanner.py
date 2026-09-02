import re
import socket
import ssl
from urllib.parse import urlparse
import requests

TIMEOUT = 5

def _finding(name, severity, evidence, recommendation):
    return {
        "name": name, "severity": severity,
        "evidence": evidence, "recommendation": recommendation
    }

def _valid_local_target(target):
    if not target:
        return False, "Enter a target URL."
    if not re.match(r"^https?://", target, re.I):
        target = "http://" + target
    p = urlparse(target)
    host = (p.hostname or "").lower()
    allowed = {"localhost", "127.0.0.1", "::1"}
    if host not in allowed:
        return False, "For this academic demo, scan only a local target such as http://127.0.0.1:5001."
    return True, target

def scan_target(target):
    ok, value = _valid_local_target(target)
    if not ok:
        return {"error": value, "findings": [], "score": 0, "scanned_at": ""}
    target = value
    findings = []
    try:
        r = requests.get(target, timeout=TIMEOUT, allow_redirects=True)
    except requests.RequestException as e:
        return {"error": f"Target is not reachable: {e}", "findings": [], "score": 0, "scanned_at": ""}

    h = {k.lower(): v for k, v in r.headers.items()}

    required = {
        "content-security-policy": ("Missing Content-Security-Policy header",
            "Add a restrictive Content-Security-Policy appropriate for the application."),
        "x-content-type-options": ("Missing X-Content-Type-Options header",
            "Set X-Content-Type-Options: nosniff."),
        "x-frame-options": ("Missing X-Frame-Options header",
            "Set X-Frame-Options: DENY or SAMEORIGIN as appropriate."),
        "referrer-policy": ("Missing Referrer-Policy header",
            "Set a suitable Referrer-Policy such as strict-origin-when-cross-origin.")
    }
    for key, (name, rec) in required.items():
        if key not in h:
            findings.append(_finding(name, "Medium", "Header was not present in the HTTP response.", rec))

    if "server" in h:
        findings.append(_finding(
            "Server Banner Disclosure", "Low",
            f"Server header exposes: {h['server']}",
            "Minimize unnecessary server/version disclosure in production."
        ))

    set_cookie = h.get("set-cookie", "")
    if set_cookie and "httponly" not in set_cookie.lower():
        findings.append(_finding(
            "Cookie Missing HttpOnly", "Medium",
            "A Set-Cookie response did not include HttpOnly.",
            "Add HttpOnly to session cookies where client-side JavaScript does not need access."
        ))
    if set_cookie and r.url.lower().startswith("https://") and "secure" not in set_cookie.lower():
        findings.append(_finding(
            "Cookie Missing Secure Flag", "Medium",
            "A cookie on an HTTPS response did not include Secure.",
            "Add the Secure flag to sensitive cookies."
        ))

    # Simple reflected-input demonstration check: only on the local target.
    marker = "VAPT_TEST_MARKER_123"
    try:
        q = target + ("&" if "?" in target else "?") + "q=" + marker
        rr = requests.get(q, timeout=TIMEOUT)
        if marker in rr.text:
            findings.append(_finding(
                "Potential Reflected Input", "High",
                "A harmless test marker was reflected in the response body.",
                "Validate and contextually encode untrusted input before rendering it."
            ))
    except requests.RequestException:
        pass

    weights = {"Critical": 10, "High": 7, "Medium": 4, "Low": 1}
    raw = sum(weights.get(f["severity"], 0) for f in findings)
    score = min(100, raw * 5)

    return {
        "error": None,
        "findings": findings,
        "score": score,
        "scanned_at": datetime.now().strftime("%d %b %Y, %H:%M:%S"),
        "status": r.status_code,
        "final_url": r.url
    }
