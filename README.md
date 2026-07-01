# NetAutoAI

## Overview

NetAutoAI is an AI-powered network automation and security auditing platform designed to simplify the analysis of Cisco network configurations. The application automatically analyzes network devices, detects configuration issues, evaluates security best practices, and generates comprehensive reports with AI-assisted recommendations.

The goal of NetAutoAI is to reduce the time required for manual network audits while improving configuration accuracy and security compliance.

---

## Features

### Device Discovery
- Automatically discover Cisco devices on the network.
- Retrieve device information through SSH.
- Support for multiple network devices.

### Configuration Analysis
- Parse Cisco configuration files.
- Analyze:
  - VLAN configuration
  - Trunk interfaces
  - Access interfaces
  - Routing protocols
  - Access Control Lists (ACLs)
  - Interface configurations
  - Port security
  - Password configurations
  - Management settings

### Security Audit
Detect common security issues such as:
- Telnet enabled
- Weak password encryption
- Missing SSH configuration
- Unsecured VTY lines
- Missing banners
- Insecure management access
- Unused interfaces left active
- Missing port security
- ACL inconsistencies
- Routing configuration issues

### AI Report Generation
- Generate human-readable reports using Artificial Intelligence.
- Explain detected issues.
- Recommend remediation steps.
- Prioritize security findings.

### Dashboard
- Modern web interface.
- Device management.
- Configuration upload.
- Analysis history.
- Generated reports.

---

## Technologies Used

### Backend
- Python
- Flask
- Paramiko
- Netmiko
- TextFSM
- SQLite

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### AI
- OpenAI API

### Networking
- Cisco IOS
- SSH

### Virtualization
- VMware Workstation
- GNS3

---

## Project Architecture

```
                +------------------+
                | Web Interface    |
                +--------+---------+
                         |
                         |
                 Flask Backend
                         |
     +-------------------+------------------+
     |                   |                  |
 Device Discovery   Config Parser    AI Report Engine
     |                   |                  |
     +-------------------+------------------+
                         |
                    SQLite Database
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/netautoai.git
cd netautoai
```

### Create a virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

---

## Project Structure

```
NetAutoAI/
│
├── app.py
├── requirements.txt
├── config.py
├── database/
├── templates/
├── static/
├── reports/
├── parser/
├── analyzer/
├── ai/
├── uploads/
├── models/
├── utils/
└── README.md
```

---

## Example Workflow

1. Connect to a Cisco device.
2. Retrieve its running configuration.
3. Parse the configuration.
4. Perform security analysis.
5. Detect misconfigurations.
6. Generate an AI-powered report.
7. Display results through the web dashboard.

---

## Example Security Checks

| Category | Check |
|----------|-------|
| SSH | SSH enabled |
| Telnet | Telnet disabled |
| Passwords | Password encryption enabled |
| VLAN | Native VLAN configuration |
| Trunks | Allowed VLAN verification |
| Interfaces | Unused ports shutdown |
| ACL | ACL validation |
| Routing | Routing configuration analysis |
| Management | Secure management access |
| Port Security | Enabled on access ports |

---

## Future Improvements

- Multi-vendor support (Juniper, Huawei, Arista)
- Compliance checking (CIS Benchmarks)
- Automated configuration remediation
- Real-time network monitoring
- Network topology visualization
- REST API
- Docker deployment
- Role-Based Access Control (RBAC)
- SIEM integration
- Cloud deployment

---

## Educational Purpose

This project was developed as a Final Year Project (PFE) to demonstrate practical applications of:

- Network Automation
- Artificial Intelligence
- Cybersecurity
- Cisco Network Administration
- Python Programming
- Web Development

---

## Author

**Rawen Khaddar**

Bachelor's Degree in Computer Networks and Telecommunications

Interested in:
- Cybersecurity
- Network Automation
- Artificial Intelligence
- DevSecOps

---

## License

This project is released under the MIT License.
