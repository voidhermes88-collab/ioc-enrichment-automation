"""
IOC Enrichment Automation - VirusTotal + AbuseIPDB -> Slack
Built by Norbert Csanya - SOC Automation Demo
Loom: https://www.loom.com/share/faf3524408da4caf9deea89ff55ab6
"""
import sys
import requests
import os
from datetime import datetime

def check_virustotal(ioc):
    # Replace with real VT API key for production
    print(f"[+] Checking VirusTotal for {ioc}...")
    # Mock response for demo - replace with real API call
    return {"malicious": 3, "harmless": 68, "suspicious": 1, "link": f"https://www.virustotal.com/gui/search/{ioc}"}

def check_abuseipdb(ip):
    print(f"[+] Checking AbuseIPDB for {ip}...")
    # Mock response for demo - replace with real API call
    return {"abuse_confidence": 85, "total_reports": 42, "is_whitelisted": False}

def push_to_slack(message):
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if webhook:
        requests.post(webhook, json={"text": message})
        print("[+] Pushed to Slack #threat-intel")
    else:
        print(f"[+] Slack alert (mock): {message}")

def main():
    ioc = sys.argv[1] if len(sys.argv) > 1 else "185.220.101.5"
    print(f"[*] IOC Enrichment started for: {ioc} at {datetime.now()}")
    
    vt = check_virustotal(ioc)
    abuse = check_abuseipdb(ioc)
    
    summary = f"""
--- IOC REPORT: {ioc} ---
VirusTotal: {vt['malicious']} malicious / {vt['harmless']} clean
AbuseIPDB: {abuse['abuse_confidence']}% confidence, {abuse['total_reports']} reports
VT Link: {vt['link']}
Done in 2.3s - Auto-push to Slack #threat-intel
"""
    print(summary)
    push_to_slack(summary)
    print("[Done] Full workflow can be rebuilt in n8n for SOC.")

if __name__ == "__main__":
    main()
