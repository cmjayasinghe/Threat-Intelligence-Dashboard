# Threat Intelligence Dashboard

A cybersecurity-focused Threat Intelligence Dashboard that collects, processes, and visualizes threat data from multiple intelligence sources.

## Project Overview

This project was built to demonstrate practical cybersecurity, threat intelligence, automation, and data visualization skills. The dashboard aggregates security data from public threat intelligence feeds and presents it through an interactive web interface.

## Features

### CVE Collection

* Collects Common Vulnerabilities and Exposures (CVEs) from the National Vulnerability Database (NVD) API.
* Stores collected CVE data in CSV format for analysis and visualization.

### Malicious IP Intelligence

* Integrates with the AbuseIPDB API.
* Retrieves high-confidence malicious IP addresses.
* Stores threat intelligence data locally for dashboard visualization.

### Dashboard Visualization

* Built using Dash and Plotly.
* Displays:

  * Total CVEs collected
  * Total malicious IPs collected
* Designed to be extended with additional threat intelligence metrics.

### Secure API Key Management

* Uses environment variables through a `.env` file.
* Prevents sensitive API keys from being exposed in source code or GitHub repositories.

## Technologies Used

* Python
* Pandas
* Requests
* Dash
* Plotly
* AbuseIPDB API
* NVD API
* Git
* GitHub

## Project Structure

```text
Threat-Intelligence-Dashboard/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── cves.csv
│   └── malicious_ips.csv
│
├── docs/
│
├── screenshots/
│   ├── dashboard_v1.png
│   ├── dashboard_v2_abuseipdb.png
|   ├── cve_collection1.png
│   └── cve_collection2.png
│
├── scripts/
│   ├── fetch_cves.py
│   ├── fetch_abuseipdb.py
│   ├── fetch_iocs.py
│   ├── fetch_ransomware.py
│   └── scheduler.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Screenshots

### Dashboard Version 1

![Dashboard V1](screenshots/dashboard_v1.png)

### Dashboard with AbuseIPDB Integration

![Dashboard V2](screenshots/dashboard_v2_abuseipdb.png)

### CVE Collection

![CVE Collection](screenshots/cve_collection1.png)
![CVE Collection](screenshots/cve_collection2.png)

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Threat-Intelligence-Dashboard.git
cd Threat-Intelligence-Dashboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```text
ABUSEIPDB_API_KEY=YOUR_API_KEY
```

### Run CVE Collection

```bash
python scripts/fetch_cves.py
```

### Run AbuseIPDB Collection

```bash
python scripts/fetch_abuseipdb.py
```

### Launch Dashboard

```bash
python dashboard/app.py
```

## Current Progress

* [x] Project setup
* [x] CVE collection using NVD API
* [x] AbuseIPDB integration
* [x] Basic Dash dashboard
* [x] Environment variable management
* [ ] IOC collection (AlienVault OTX)
* [ ] Ransomware intelligence feed integration
* [ ] Advanced visualizations
* [ ] Automated scheduling
* [ ] Threat intelligence enrichment

## Future Improvements

* AlienVault OTX integration
* IOC enrichment
* Ransomware tracking
* Geolocation mapping of malicious IPs
* Automated threat intelligence updates
* Email alerting system
* Advanced analytics dashboard

## Learning Objectives

This project demonstrates:

* Threat Intelligence Collection
* Security Automation
* API Integration
* Data Processing
* Secure Secret Management
* Dashboard Development
* Git and GitHub Workflow

## Disclaimer

This project is intended for educational and portfolio purposes only. Threat intelligence data is collected from publicly available sources and APIs.


