## 📌 Features

- 🔍 Network configuration analysis
- ⚙️ Automated configuration validation
- 🛡️ Security compliance checking
- 🌐 Multi-vendor configuration support
- 📊 Interactive dashboard
- 📄 Automatic report generation
- 🚨 Detection of configuration issues
- 🔄 Configuration comparison
- 📈 Network statistics and visualization
- 👤 User authentication and role management

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask
- SQLite
- REST API

### Frontend
- PySide6 (Qt for Python)

### Network Automation
- Netmiko
- Paramiko
- Cisco Configuration Parsing
- SSH Automation

### Data Processing
- JSON
- Regular Expressions
- Configuration Parsing Engine

---

## 📂 Project Structure

```text
NetAutoAI/
│
├── app.py
├── requirements.txt
├── config.py
├── database/
├── desktop_app/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
├── uploads/
├── reports/
├── analyzer/
├── automation/
├── models/
└── README.md
```

---

## ⚡ Installation

### Clone the repository

```bash
git clone https://github.com/louaymhouachi/pfe_project-.git
```

### Navigate to the project

```bash
cd pfe_project-
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

## 1. Start the Backend Server

From the project root directory, activate the virtual environment and run:

```bash
python app.py
```

**Keep this terminal open** because it runs the backend server.

---

## 2. Start the Desktop Application (Frontend)

Open **a second Command Prompt (CMD)**.

Navigate to the project directory, activate the virtual environment again, then go to the desktop application folder:

```bash
venv\Scripts\activate
cd desktop_app
python main.py
```

The NetAutoAI desktop interface will launch and connect to the backend server.

---

## 🔐 Default Administrator Account

Use the following credentials to log in for the first time:

| Username | Password |
|----------|----------|
| **admin** | **admin123** |

> **Note:** It is recommended to change the default administrator password after the first login.

---

## 📖 How to Use

After logging in, you can:

- Upload Cisco configuration files.
- Connect to Cisco devices via SSH.
- Analyze network configurations.
- Detect security vulnerabilities and misconfigurations.
- Review VLAN, ACL, Routing, NAT, DHCP, DNS, and Interface configurations.
- Generate detailed security and configuration reports.
- Export generated reports.

---

## 🎯 Main Modules

### Configuration Analyzer

Analyzes Cisco device configurations and extracts:

- Hostname
- VLANs
- Trunk Ports
- Access Ports
- Routing Configuration
- ACLs
- Interfaces
- DHCP Configuration
- DNS Settings
- NAT Configuration

---

### Security Validator

Checks for:

- Weak passwords
- Telnet enabled
- Missing SSH configuration
- Unused VLANs
- Insecure services
- Missing ACL protection
- Configuration inconsistencies

---

### Report Generator

Generates professional reports including:

- Executive Summary
- Device Information
- Network Overview
- VLAN Analysis
- Routing Analysis
- ACL Analysis
- Security Findings
- Recommendations

---

## 👨‍💻 Authors

- **Louay Mhouachi**
- **Rawen Khaddar**

**Final Year Project (PFE)**

---

## 🎓 Academic Context

This project was developed as part of a Final Year Project (Projet de Fin d'Études) in the field of Computer Networks and Cybersecurity.

---

## 🚀 Future Improvements

- AI-assisted configuration recommendations
- Real-time device monitoring
- Multi-vendor support
- Network topology visualization
- Configuration backup automation
- Compliance scoring
- CVE vulnerability integration

---

## 📜 License

This project is developed for educational purposes.
