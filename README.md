# IOC Enrichment Automation (VirusTotal + AbuseIPDB -> Slack)

🎥 60-sec Demo: https://www.loom.com/share/faf3524408da4caf9deea89ff55ab6

Automates manual IOC checks that SOC analysts do daily.
- Enriches IP/domain via VirusTotal & AbuseIPDB API
- Auto-pushes enriched alert to Slack #threat-intel in 2.3s
- Built in Python, easily rebuildable in n8n

## Usage
python3 threat_check.py 185.220.101.5

Built by Norbert Csanya for SOC Automation demo.
