# 🛡️ Mini SOC - Log Monitoring and Alert System

A beginner-friendly **Blue Team** cybersecurity project that monitors log files for suspicious activities and displays alerts on a dashboard.

## 📋 Project Overview

This project simulates a Security Operations Center (SOC) log monitoring system. It analyzes server log files and detects various types of attacks including:

- **Brute Force Attacks** - Multiple failed login attempts
- **SQL Injection** - Malicious database queries
- **Admin Access Attempts** - Unauthorized access to admin pages
- **Traffic Spikes** - Potential DDoS attacks

## 🗂️ Folder Structure

```
mini-soc/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── database.py          # SQLite database operations
│   ├── log_analyzer.py      # Detection rules and log analysis
│   └── alerts.db            # SQLite database (created automatically)
├── frontend/
│   ├── index.html           # Dashboard HTML
│   ├── styles.css           # Dashboard styles
│   └── script.js            # Dashboard JavaScript
├── logs/
│   └── sample_log.txt       # Sample log file for testing
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Web browser (Chrome, Firefox, Edge, etc.)

### Step 1: Install Python Dependencies

Open a terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

This will install:
- FastAPI (web framework)
- Uvicorn (web server)
- Python-multipart (for file uploads)

### Step 2: Start the Backend Server

Navigate to the backend folder and run:

```bash
cd backend
python main.py
```

You should see output like:
```
🛡️  MINI SOC - Log Monitoring and Alert System
Starting FastAPI server...
API will be available at: http://127.0.0.1:8000
```

**Keep this terminal window open** - the server needs to keep running.

### Step 3: Open the Frontend Dashboard

1. Navigate to the `frontend` folder
2. Open `index.html` in your web browser

**Alternative**: Right-click on `index.html` → Open with → Your Browser

## 📖 How to Use

### Option 1: Analyze Sample Log File

1. In the dashboard, find the **"Or Analyze Existing Log"** section
2. Select `sample_log.txt` from the dropdown
3. Click **"Analyze"** button
4. Watch as alerts appear in the dashboard!

### Option 2: Upload Your Own Log File

1. Click **"Choose File"** under "Upload Log File"
2. Select a `.txt` or `.log` file
3. Click **"Upload & Analyze"**
4. View the detected alerts

### Log File Format

Logs should follow this format:
```
[TIMESTAMP] IP_ADDRESS - ACTION - STATUS - URL
```

Example:
```
[2024-01-15 14:23:01] 192.168.1.100 - LOGIN - FAILED - /login
[2024-01-15 14:25:10] 10.0.0.50 - REQUEST - SUCCESS - /admin
```

## 🎯 Detection Rules

### 1. Brute Force Attack Detection
- **Trigger**: More than 5 failed login attempts from the same IP within 1 minute
- **Severity**: High
- **Example**: 6+ `LOGIN - FAILED` entries from same IP

### 2. SQL Injection Detection
- **Trigger**: SQL keywords in URL (SELECT, UNION, DROP, OR 1=1, etc.)
- **Severity**: Critical
- **Example**: `/api/users?id=1 UNION SELECT * FROM passwords`

### 3. Admin Access Detection
- **Trigger**: Any request to URLs containing "admin" or "administrator"
- **Severity**: Critical (if successful), Medium (if failed)
- **Example**: `/admin/dashboard`, `/administrator/config`

### 4. Traffic Spike Detection
- **Trigger**: More than 50 requests in the same minute
- **Severity**: High
- **Example**: 51+ requests with timestamps in the same minute

## 📊 Dashboard Features

### Statistics Cards
- **Total Alerts** - Count of all detected threats
- **Critical Alerts** - Highest priority threats
- **High Alerts** - Serious threats requiring attention
- **Medium Alerts** - Moderate threats

### Alerts Table
Displays detailed information for each alert:
- Alert ID
- Timestamp
- Alert Type
- Severity Level
- IP Address
- Description

### Attacks Over Time Chart
Visual graph showing when attacks occurred, helping identify attack patterns.

## 🔧 API Endpoints

The backend provides these REST API endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/api/upload-log` | Upload and analyze log file |
| POST | `/api/analyze-log/{filename}` | Analyze existing log file |
| GET | `/api/alerts` | Get all alerts |
| GET | `/api/alerts/count` | Get total alert count |
| GET | `/api/alerts/stats` | Get alert statistics |
| DELETE | `/api/alerts` | Clear all alerts |
| GET | `/api/logs/list` | List available log files |

### Testing API with Browser

Visit `http://127.0.0.1:8000/docs` to see interactive API documentation!

## 🎓 Learning Objectives

This project teaches:

1. **Backend Development**
   - REST API design with FastAPI
   - Database operations with SQLite
   - File handling and processing
   - Pattern matching with regular expressions

2. **Cybersecurity Concepts**
   - Log analysis techniques
   - Threat detection rules
   - Attack pattern recognition
   - Security monitoring basics

3. **Frontend Development**
   - Asynchronous JavaScript (fetch API)
   - Data visualization with Chart.js
   - Responsive web design
   - User interface design

## 🛠️ Customization Ideas

### Add New Detection Rules

Edit `backend/log_analyzer.py` and add new detection methods:

```python
def detect_port_scan(self, log_entry):
    # Your detection logic here
    pass
```

### Change Alert Severity Levels

Modify severity levels in detection functions:
```python
'severity': 'Critical'  # or 'High', 'Medium', 'Low'
```

### Customize Dashboard Colors

Edit `frontend/styles.css` to change the color scheme:
```css
.stat-card.critical {
    border-left-color: #your-color;
}
```

## 📝 Troubleshooting

### Backend Server Won't Start

**Error**: `ModuleNotFoundError: No module named 'fastapi'`
- **Solution**: Run `pip install -r requirements.txt`

### Dashboard Can't Connect to API

**Error**: "Error loading dashboard data"
- **Solution**: Make sure backend server is running on port 8000
- Check console: `http://127.0.0.1:8000` should be accessible

### Database Errors

**Error**: Database-related errors
- **Solution**: Delete `alerts.db` and restart the backend server

### No Alerts Appearing

- **Check**: Make sure you clicked "Analyze" button
- **Check**: Log file format matches expected format
- **Check**: Browser console for JavaScript errors (F12)

## 🔐 Security Notes

**IMPORTANT**: This is an educational project with some simplified security practices:

- ⚠️ CORS is set to allow all origins (`*`) - In production, specify exact domains
- ⚠️ No authentication on API endpoints - Real SOCs require authentication
- ⚠️ SQLite is used for simplicity - Production systems use PostgreSQL/MySQL
- ⚠️ Detection rules are basic - Real systems use advanced ML/AI

**Never use this in a production environment without proper security hardening!**

## 📚 Further Learning

### Recommended Topics
- SIEM (Security Information and Event Management) systems
- Intrusion Detection Systems (IDS)
- Advanced log analysis techniques
- Machine learning for threat detection
- Security automation and orchestration

### Similar Tools to Explore
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Splunk
- Wazuh
- OSSEC

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new detection rules
- Improve the UI/UX
- Add more visualization options
- Create additional log samples
- Write documentation

## 📄 License

This project is created for educational purposes. Feel free to use and modify for learning.

## 🎉 Credits

Created as a beginner-friendly Blue Team cybersecurity project.

---

**Happy Learning! 🎓🛡️**

If you found this project helpful, star the repository and share it with others learning cybersecurity!
