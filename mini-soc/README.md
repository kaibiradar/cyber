# 🛡️ Mini SOC - Log Monitoring and Alert System

A beginner-friendly **Blue Team** cybersecurity project that monitors log files for suspicious activities and displays alerts on a real-time dashboard.

## 📋 Project Overview

This project simulates a Security Operations Center (SOC) log monitoring system. It analyzes server log files and detects various types of attacks including:

- **Brute Force Attacks** - Multiple failed login attempts (5+ within 1 minute)
- **SQL Injection** - Malicious database queries and keywords
- **Admin Access Attempts** - Unauthorized access to admin pages
- **Traffic Spikes** - Potential DDoS attacks (50+ requests/minute)

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Programming language
- **FastAPI 0.104.1** - Modern web framework for building APIs
- **Uvicorn 0.24.0** - ASGI web server for running FastAPI
- **SQLite** - Lightweight database for storing alerts (built into Python)
- **Pydantic 2.5.0** - Data validation library
- **Python Multipart 0.0.6** - File upload handling

### Frontend
- **HTML5** - Structure and markup
- **CSS3** - Styling and responsive design
- **Vanilla JavaScript (ES6+)** - Interactive functionality
- **Chart.js 4.4.0** - Data visualization and graphs
- **Fetch API** - Asynchronous HTTP requests

### Development Tools
- **VS Code** - Recommended code editor
- **Git** - Version control (optional)
- **PowerShell/Terminal** - Command line interface

### Security Concepts
- **Log Analysis** - Pattern matching and threat detection
- **Regular Expressions (Regex)** - Log parsing
- **REST API Design** - Backend communication
- **CORS (Cross-Origin Resource Sharing)** - API security

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

## 🚀 Complete Installation & Setup Guide

### Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.8 or higher** - [Download here](https://www.python.org/downloads/)
  - During installation, check "Add Python to PATH"
- **pip** - Python package manager (comes with Python)
- **Web browser** - Chrome, Firefox, Edge, or Safari
- **Code Editor** - VS Code recommended (optional)

### Step-by-Step Installation

#### Step 1: Verify Python Installation

Open PowerShell or Terminal and verify Python is installed:

```bash
python --version
```

Expected output: `Python 3.8.x` or higher

```bash
pip --version
```

Expected output: `pip x.x.x from...`

#### Step 2: Navigate to Project Directory

```bash
cd d:\cyber\mini-soc
```

Or on your system:
```bash
cd /path/to/mini-soc
```

#### Step 3: Install Python Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- ✅ FastAPI 0.104.1 - Web framework for building APIs
- ✅ Uvicorn 0.24.0 - ASGI web server
- ✅ Python-multipart 0.0.6 - File upload support
- ✅ Pydantic 2.5.0 - Data validation

**Alternative installation** (if above fails):
```bash
pip install fastapi uvicorn python-multipart pydantic
```

#### Step 4: Initialize the Database

The database will be created automatically when you first run the server. You can also manually initialize it:

```bash
cd backend
python database.py
```

Expected output: `✓ Database initialized successfully`

#### Step 5: Start the Backend Server

**Windows (PowerShell):**
```bash
cd d:\cyber\mini-soc\backend
python main.py
```

**macOS/Linux:**
```bash
cd /path/to/mini-soc/backend
python3 main.py
```

You should see output like:
```
============================================================
🛡️  MINI SOC - Log Monitoring and Alert System
============================================================
Starting FastAPI server...
API will be available at: http://127.0.0.1:8000
API documentation at: http://127.0.0.1:8000/docs
============================================================
INFO:     Started server process [xxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ **Server Status**: Running
🌐 **API URL**: http://127.0.0.1:8000
📚 **API Docs**: http://127.0.0.1:8000/docs

**⚠️ IMPORTANT: Keep this terminal window open!** The server needs to keep running.

#### Step 6: Open the Frontend Dashboard

**Method 1 - File Explorer:**
1. Navigate to `d:\cyber\mini-soc\frontend\` folder
2. Double-click `index.html`
3. It will open in your default browser

**Method 2 - Browser:**
1. Open your web browser
2. Press `Ctrl+O` (or `Cmd+O` on Mac)
3. Browse to `mini-soc/frontend/index.html`
4. Click Open

**Method 3 - VS Code:**
1. Right-click on `index.html`
2. Select "Open with Live Server" (if installed)
3. Or select "Reveal in File Explorer" → then double-click

#### Step 7: Verify Everything is Working

In the dashboard, you should see:
- ✅ "Mini SOC Dashboard" header
- ✅ Statistics cards showing 0 alerts
- ✅ Empty alerts table
- ✅ Empty graph

**Test the connection:**
- Open browser console (F12)
- You should see: `🛡️ Mini SOC Dashboard Loaded`
- If you see "Error loading dashboard", the backend isn't running

## 📖 How to Use the Mini SOC System

### First Time Usage - Analyze Sample Log

The project includes a sample log file with realistic attack patterns. Follow these steps:

1. **In the Dashboard**, locate the **"Or Analyze Existing Log"** section
2. Click the dropdown menu
3. Select **`sample_log.txt`** from the list
4. Click the **"Analyze"** button
5. Wait 2-3 seconds for processing
6. **Watch the magic happen!** 🎉

**You should see:**
- ✅ Success message: "✓ Success! Detected X alerts"
- ✅ Statistics cards update with numbers
- ✅ Alerts table populates with detected threats
- ✅ Graph shows attack timeline

**Expected Results from Sample Log:**
- ~10-15 alerts detected
- Multiple brute force attempts
- Several SQL injection attacks
- Admin access attempts
- Possible traffic spike

### Upload Your Own Log File

1. **Prepare your log file** in the correct format (see below)
2. Click **"Choose File"** under "Upload Log File"
3. Select your `.txt` or `.log` file
4. Click **"Upload & Analyze"**
5. View the results in the dashboard

### Log File Format

Your log files must follow this format:

```
[YYYY-MM-DD HH:MM:SS] IP_ADDRESS - ACTION - STATUS - URL
```

**Components:**
- `[YYYY-MM-DD HH:MM:SS]` - Timestamp in brackets
- `IP_ADDRESS` - IPv4 address (e.g., 192.168.1.100)
- `ACTION` - Activity type (LOGIN, REQUEST, etc.)
- `STATUS` - Result (SUCCESS, FAILED)
- `URL` - Requested path or page

**Valid Examples:**
```
[2024-01-15 14:23:01] 192.168.1.100 - LOGIN - FAILED - /login
[2024-01-15 14:25:10] 10.0.0.50 - REQUEST - SUCCESS - /admin
[2024-01-15 14:26:30] 172.16.0.25 - REQUEST - SUCCESS - /api/users?id=1
```

### Dashboard Features Explained

#### 1. Statistics Cards (Top Section)
- **Total Alerts** - All detected threats across all severities
- **Critical** - Highest priority (SQL injection, successful admin access)
- **High** - Serious threats (brute force, traffic spikes)
- **Medium** - Moderate threats (failed admin access)

#### 2. Attacks Over Time Graph
- **X-axis**: Time (hour by hour)
- **Y-axis**: Number of alerts
- **Purpose**: Identify when most attacks occur
- **Use Case**: Spot attack patterns and timing

#### 3. Alerts Table
Shows detailed information for each alert:
- **ID** - Unique alert identifier
- **Timestamp** - When the attack occurred
- **Alert Type** - Category of threat
- **Severity** - Risk level (color-coded)
- **IP Address** - Source of the attack
- **Description** - Detailed explanation

#### 4. Control Panel
- **Upload Log File** - Add new logs for analysis
- **Analyze Existing Log** - Process logs already in the system
- **Refresh Dashboard** - Reload all data from database
- **Clear All Alerts** - Delete all alerts (requires confirmation)

### Real-Time Monitoring Workflow

**Typical SOC analyst workflow:**

1. **Upload logs** from your web server
2. **Review statistics** to understand threat landscape
3. **Examine the graph** to identify attack patterns
4. **Investigate alerts** in the table
5. **Take action** based on severity:
   - **Critical**: Immediate investigation required
   - **High**: Investigate within 1 hour
   - **Medium**: Review during normal operations
6. **Clear old alerts** after investigation
7. **Repeat** with new logs

## 🎯 Detection Rules (Security Logic)

The system uses 4 detection rules to identify threats. Each rule is explained in detail:

### 1. Brute Force Attack Detection 🔓

**What it detects**: Password guessing attacks

**Rule Logic**:
- Tracks failed login attempts per IP address
- Triggers when: **More than 5 failed logins** from the same IP **within 1 minute**
- Uses sliding time window to track attempts

**Severity**: High 🟠

**Technical Implementation**:
```python
# Tracks: {IP: [timestamp1, timestamp2, ...]}
# Removes attempts older than 1 minute
# Alerts if count > 5
```

**Example**:
```
[2024-01-15 14:23:01] 192.168.1.100 - LOGIN - FAILED - /login
[2024-01-15 14:23:15] 192.168.1.100 - LOGIN - FAILED - /login
[2024-01-15 14:23:28] 192.168.1.100 - LOGIN - FAILED - /login
[2024-01-15 14:23:42] 192.168.1.100 - LOGIN - FAILED - /login
[2024-01-15 14:23:55] 192.168.1.100 - LOGIN - FAILED - /login
[2024-01-15 14:24:08] 192.168.1.100 - LOGIN - FAILED - /login  ← ALERT!
```

**Why it matters**: Attackers often use automated tools to guess passwords. This detects those attempts.

---

### 2. SQL Injection Detection 💉

**What it detects**: Database manipulation attacks

**Rule Logic**:
- Scans URL parameters for SQL keywords
- Triggers when detected: `SELECT`, `UNION`, `DROP`, `DELETE`, `INSERT`, `UPDATE`, `OR 1=1`, `--`, `EXEC`, `EXECUTE`, `SCRIPT`, `JAVASCRIPT`, `ONERROR`

**Severity**: Critical 🔴

**Technical Implementation**:
```python
# Converts URL to uppercase
# Checks if any SQL keyword exists in URL
# Case-insensitive matching
```

**Examples**:
```
✅ DETECTED: /api/users?id=1 UNION SELECT * FROM passwords--
✅ DETECTED: /search?q=admin' OR 1=1--
✅ DETECTED: /products?id=5 DROP TABLE users--
✅ DETECTED: /api/data?query=SELECT password FROM users
❌ SAFE: /products?search=laptop
```

**Why it matters**: SQL injection can expose entire databases, steal data, or delete records. Critical to detect.

---

### 3. Admin Access Attempt Detection 👑

**What it detects**: Unauthorized access to administrative areas

**Rule Logic**:
- Checks if URL contains `admin` or `administrator`
- Severity depends on success:
  - **Critical** 🔴 if STATUS = SUCCESS (breach!)
  - **Medium** 🟡 if STATUS = FAILED (attempt blocked)

**Technical Implementation**:
```python
# Case-insensitive search for 'admin' in URL
# Dynamic severity based on access success
```

**Examples**:
```
🔴 CRITICAL: /admin/login - SUCCESS
🔴 CRITICAL: /administrator/config - SUCCESS
🟡 MEDIUM: /admin/dashboard - FAILED
🟡 MEDIUM: /admin - FAILED
```

**Why it matters**: Admin panels have powerful controls. Unauthorized access = full system compromise.

---

### 4. Traffic Spike Detection 📈

**What it detects**: Potential DDoS (Distributed Denial of Service) attacks

**Rule Logic**:
- Counts total requests per minute (ignores seconds)
- Triggers when: **More than 50 requests** in the same minute
- Alerts only once when threshold is first exceeded

**Severity**: High 🟠

**Technical Implementation**:
```python
# Groups by minute: "YYYY-MM-DD HH:MM"
# Increments counter for each request
# Alerts at count = 51 (not every request after)
```

**Example**:
```
[2024-01-15 14:28:01] 192.168.1.200 - LOGIN - FAILED - /login
[2024-01-15 14:28:03] 192.168.1.201 - LOGIN - FAILED - /login
... (50+ requests in 14:28)
← ALERT: Traffic Spike Detected!
```

**Why it matters**: Sudden traffic spikes indicate automated attacks or DDoS attempts that can crash servers.

---

### Detection Rule Summary Table

| Rule | Trigger | Severity | Real-World Impact |
|------|---------|----------|-------------------|
| Brute Force | 5+ failed logins (1 min) | High | Account takeover |
| SQL Injection | SQL keywords in URL | Critical | Data breach, data loss |
| Admin Access | Access to /admin URLs | Critical/Medium | Full compromise |
| Traffic Spike | 50+ requests (1 min) | High | Service disruption |

## 📊 Dashboard Features

### Statistics Cards
- **Total Alerts** - Count of all detected threats
- **Critical Alerts** - Highest priority threats (immediate action required)
- **High Alerts** - Serious threats requiring attention
- **Medium Alerts** - Moderate threats to monitor

### Alerts Table
Displays detailed information for each alert:
- Alert ID
- Timestamp (when attack occurred)
- Alert Type (category)
- Severity Level (color-coded badges)
- IP Address (attack source)
- Description (detailed explanation)

### Attacks Over Time Chart
Visual graph powered by Chart.js showing:
- When attacks occurred
- Attack frequency patterns
- Timeline visualization
- Interactive hover tooltips

## 🏗️ Project Architecture

### System Overview

```
┌─────────────────┐      HTTP/REST API     ┌──────────────────┐
│                 │ ◄──────────────────────►│                  │
│  Frontend       │    JSON Requests        │   Backend        │
│  (Dashboard)    │    JSON Responses       │   (FastAPI)      │
│                 │                         │                  │
└─────────────────┘                         └────────┬─────────┘
                                                     │
                                                     │ SQLite
                                                     ▼
                                            ┌─────────────────┐
                                            │                 │
                                            │   Database      │
                                            │   (alerts.db)   │
                                            │                 │
                                            └─────────────────┘
```

### Backend Architecture (backend/)

**1. main.py** - FastAPI Application (9,068 bytes)
- REST API endpoints (8 routes)
- CORS middleware configuration
- File upload handling
- Request/response processing
- Server initialization

**2. log_analyzer.py** - Detection Engine (9,233 bytes)
- LogAnalyzer class
- 4 detection rule methods
- Log parsing with regex
- Pattern matching algorithms
- Alert generation logic

**3. database.py** - Data Layer (3,330 bytes)
- SQLite database operations
- CRUD functions (Create, Read, Update, Delete)
- Alert storage and retrieval
- Database initialization
- Schema management

**4. alerts.db** - SQLite Database (auto-generated)
- **alerts** table with schema:
  ```sql
  CREATE TABLE alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    alert_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    ip_address TEXT,
    description TEXT NOT NULL,
    created_at TEXT NOT NULL
  )
  ```

### Frontend Architecture (frontend/)

**1. index.html** - User Interface
- Semantic HTML5 structure
- Responsive layout
- Dashboard sections:
  - Header with branding
  - Control panel for file management
  - Statistics cards grid
  - Chart canvas
  - Alerts table
  - Footer

**2. styles.css** - Styling & Design
- Gradient backgrounds (cybersecurity theme)
- Card-based layout
- Responsive grid system
- Color-coded severity badges
- Hover effects and transitions
- Mobile-responsive breakpoints

**3. script.js** - Interactivity & API Calls
- Dashboard initialization
- Fetch API for backend communication
- Chart.js integration
- DOM manipulation
- Event handlers for buttons
- Real-time data updates
- Error handling and user feedback

### Data Flow Diagram

```
User Action
    │
    ▼
┌───────────────────┐
│  Upload Log File  │
└─────────┬─────────┘
          │
          ▼
┌────────────────────┐
│  POST /api/upload  │
│   (Frontend JS)    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────────┐
│  FastAPI Endpoint      │
│  Receives FormData     │
└─────────┬──────────────┘
          │
          ▼
┌─────────────────────────┐
│  LogAnalyzer.analyze()  │
│  Parse & Detect         │
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  Run Detection Rules:   │
│  1. Brute Force         │
│  2. SQL Injection       │
│  3. Admin Access        │
│  4. Traffic Spike       │
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  database.save_alert()  │
│  Store in SQLite        │
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  Return JSON Response   │
│  {success, count}       │
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  Update Dashboard       │
│  Refresh Data           │
└─────────────────────────┘
```

## 🔧 API Endpoints Documentation

The backend provides 8 REST API endpoints. All responses are in JSON format.

### Base URL
```
http://127.0.0.1:8000
```

---

### 1. Health Check
**GET** `/`

Check if the API is running.

**Response:**
```json
{
  "message": "Mini SOC API is running!",
  "version": "1.0.0",
  "status": "healthy"
}
```

**Status Code:** 200 OK

---

### 2. Upload Log File
**POST** `/api/upload-log`

Upload and analyze a log file.

**Request:**
- **Content-Type:** `multipart/form-data`
- **Body:** 
  - `file` (file): The log file to upload (.txt or .log)

**Response:**
```json
{
  "success": true,
  "message": "Log file analyzed successfully",
  "alerts_detected": 15,
  "file_saved": "logs/uploaded_20240115_142345.txt"
}
```

**Status Codes:**
- 200 OK - Success
- 500 Internal Server Error - Processing failed

**Example (cURL):**
```bash
curl -X POST "http://127.0.0.1:8000/api/upload-log" \
  -F "file=@sample_log.txt"
```

---

### 3. Analyze Existing Log
**POST** `/api/analyze-log/{filename}`

Analyze a log file already in the logs directory.

**Parameters:**
- `filename` (path) - Name of the log file (e.g., "sample_log.txt")

**Response:**
```json
{
  "success": true,
  "message": "Analyzed sample_log.txt",
  "alerts_detected": 12,
  "alerts_saved": 12
}
```

**Status Codes:**
- 200 OK - Success
- 404 Not Found - File doesn't exist
- 500 Internal Server Error - Analysis failed

**Example (cURL):**
```bash
curl -X POST "http://127.0.0.1:8000/api/analyze-log/sample_log.txt"
```

---

### 4. Get All Alerts
**GET** `/api/alerts`

Retrieve all alerts from the database.

**Response:**
```json
{
  "success": true,
  "total": 25,
  "alerts": [
    {
      "id": 1,
      "timestamp": "2024-01-15 14:23:01",
      "alert_type": "Brute Force Attack",
      "severity": "High",
      "ip_address": "192.168.1.100",
      "description": "Detected 7 failed login attempts from 192.168.1.100 within 1 minute",
      "created_at": "2024-01-15 15:30:22"
    },
    ...
  ]
}
```

**Status Code:** 200 OK

**Example (cURL):**
```bash
curl -X GET "http://127.0.0.1:8000/api/alerts"
```

---

### 5. Get Alerts Count
**GET** `/api/alerts/count`

Get the total number of alerts.

**Response:**
```json
{
  "success": true,
  "count": 25
}
```

**Status Code:** 200 OK

---

### 6. Get Alert Statistics
**GET** `/api/alerts/stats`

Get aggregated statistics for dashboard visualizations.

**Response:**
```json
{
  "success": true,
  "by_type": {
    "Brute Force Attack": 8,
    "SQL Injection Attempt": 5,
    "Admin Access Attempt": 7,
    "Traffic Spike Detected": 2
  },
  "by_severity": {
    "Critical": 12,
    "High": 10,
    "Medium": 3
  },
  "by_hour": {
    "2024-01-15 14": 15,
    "2024-01-15 15": 10
  }
}
```

**Status Code:** 200 OK

**Use Case:** Powers the Chart.js graph and statistics cards

---

### 7. Clear All Alerts
**DELETE** `/api/alerts`

Delete all alerts from the database.

**Response:**
```json
{
  "success": true,
  "message": "All alerts cleared successfully"
}
```

**Status Code:** 200 OK

**⚠️ Warning:** This action cannot be undone!

---

### 8. List Log Files
**GET** `/api/logs/list`

Get a list of all available log files.

**Response:**
```json
{
  "success": true,
  "count": 3,
  "files": [
    "sample_log.txt",
    "uploaded_20240115_142345.txt",
    "uploaded_20240116_093022.txt"
  ]
}
```

**Status Code:** 200 OK

---

### Interactive API Documentation

FastAPI automatically generates interactive API documentation:

**Swagger UI (Recommended):**
```
http://127.0.0.1:8000/docs
```
- Interactive interface
- Test endpoints directly in browser
- See request/response schemas
- Try it out with your data

**ReDoc (Alternative):**
```
http://127.0.0.1:8000/redoc
```
- Clean, readable documentation
- Better for reference

### API Testing Tools

**1. Browser (GET requests only)**
```
http://127.0.0.1:8000/api/alerts
```

**2. cURL (All methods)**
```bash
# GET request
curl http://127.0.0.1:8000/api/alerts

# POST request
curl -X POST http://127.0.0.1:8000/api/analyze-log/sample_log.txt

# DELETE request
curl -X DELETE http://127.0.0.1:8000/api/alerts
```

**3. Postman**
- Import the endpoints
- Test with GUI
- Save request collections

**4. Python requests**
```python
import requests

# Get alerts
response = requests.get('http://127.0.0.1:8000/api/alerts')
data = response.json()
print(data)
```

## 🎓 Learning Objectives & Skills Developed

This project teaches you valuable skills across multiple domains:

### 1. Backend Development

**Python Programming:**
- Object-Oriented Programming (OOP) with classes
- Working with dictionaries and data structures
- Exception handling (try/except)
- File I/O operations
- String manipulation and parsing

**FastAPI Framework:**
- Creating REST API endpoints
- Request/response handling
- File uploads (multipart/form-data)
- Middleware configuration (CORS)
- Path parameters and query parameters
- HTTP status codes
- JSON serialization

**Database Operations:**
- SQLite database setup
- SQL queries (CREATE, INSERT, SELECT, DELETE)
- CRUD operations
- Database schema design
- Data persistence

### 2. Cybersecurity Concepts

**Blue Team Skills:**
- Log analysis and monitoring
- Threat detection methodologies
- Attack pattern recognition
- Incident identification
- Security event correlation

**Attack Types:**
- Brute force password attacks
- SQL injection vulnerabilities
- Privilege escalation attempts
- DDoS/traffic anomalies
- Web application security

**SOC Operations:**
- Alert triage and prioritization
- Severity classification
- Timeline analysis
- Threat intelligence gathering

### 3. Frontend Development

**HTML5:**
- Semantic markup
- Form handling
- File input elements
- Table structures
- Accessibility considerations

**CSS3:**
- Flexbox and Grid layouts
- Responsive design
- CSS animations and transitions
- Color theory for UX
- Component-based styling

**JavaScript (ES6+):**
- Async/await patterns
- Fetch API for HTTP requests
- DOM manipulation
- Event handling
- JSON parsing
- Error handling
- Array methods (map, filter, forEach)

**Data Visualization:**
- Chart.js library integration
- Creating interactive graphs
- Data transformation for visualization
- Color coding for severity

### 4. Software Engineering Practices

**Code Organization:**
- Modular architecture
- Separation of concerns
- Single Responsibility Principle
- Code documentation
- Naming conventions

**API Design:**
- RESTful principles
- HTTP methods (GET, POST, DELETE)
- Resource naming
- Status codes
- Error responses

**Version Control Ready:**
- Project structure
- Configuration management
- Dependencies management
- Documentation

### 5. DevOps & Deployment Concepts

**Local Development:**
- Setting up development environments
- Managing dependencies
- Running servers locally
- Testing APIs

**Debugging:**
- Reading error messages
- Using browser developer tools
- Server-side logging
- Network request inspection

### Skills Progression

**Beginner Level:**
- ✅ Understand the code structure
- ✅ Run the project successfully
- ✅ Modify detection thresholds
- ✅ Change UI colors and text

**Intermediate Level:**
- ✅ Add new detection rules
- ✅ Modify database schema
- ✅ Create additional API endpoints
- ✅ Enhance the dashboard UI

**Advanced Level:**
- ✅ Implement authentication
- ✅ Add machine learning detection
- ✅ Create real-time monitoring
- ✅ Deploy to production server

## 🛠️ Advanced Customization Guide

### Adding New Detection Rules

**Step 1:** Open `backend/log_analyzer.py`

**Step 2:** Add your detection method to the `LogAnalyzer` class:

```python
def detect_port_scan(self, log_entry):
    """
    Detect port scanning attempts
    Rule: Multiple requests to different ports from same IP
    """
    # Your detection logic here
    if some_condition:
        return {
            'timestamp': log_entry['timestamp'],
            'alert_type': 'Port Scan Detected',
            'severity': 'High',
            'ip_address': log_entry['ip_address'],
            'description': f'Port scanning detected from {log_entry["ip_address"]}'
        }
    
    return None
```

**Step 3:** Add your rule to the `analyze_log_entry` method:

```python
def analyze_log_entry(self, log_line):
    alerts = []
    log_entry = self.parse_log_line(log_line)
    
    if not log_entry:
        return alerts
    
    # Add your new rule here
    detection_rules = [
        self.detect_failed_logins,
        self.detect_sql_injection,
        self.detect_admin_access,
        self.detect_traffic_spike,
        self.detect_port_scan,  # ← Your new rule
    ]
    
    for rule in detection_rules:
        alert = rule(log_entry)
        if alert:
            alerts.append(alert)
    
    return alerts
```

**Example: Detect Suspicious User-Agents**

```python
def detect_suspicious_user_agent(self, log_entry):
    """
    Detect attacks tools based on User-Agent
    """
    # Add user_agent to your log format first
    suspicious_agents = [
        'SQLMAP', 'NIKTO', 'NMAP', 'MASSCAN', 
        'METASPLOIT', 'BURP', 'HAVIJ'
    ]
    
    user_agent = log_entry.get('user_agent', '').upper()
    
    for agent in suspicious_agents:
        if agent in user_agent:
            return {
                'timestamp': log_entry['timestamp'],
                'alert_type': 'Suspicious Tool Detected',
                'severity': 'High',
                'ip_address': log_entry['ip_address'],
                'description': f'Attack tool "{agent}" detected from {log_entry["ip_address"]}'
            }
    
    return None
```

---

### Customizing Alert Severity Levels

Edit severity in any detection function:

```python
# Change from High to Critical
'severity': 'Critical'  # Options: Critical, High, Medium, Low
```

**Add new severity level:**

1. **Backend:** Already supports any string
2. **Frontend CSS (`styles.css`):** Add badge style:

```css
.severity-low {
    background: #4CAF50;
    color: white;
    padding: 5px 12px;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.85em;
    display: inline-block;
}
```

---

### Customizing Dashboard Appearance

**Change Color Scheme:**

Edit `frontend/styles.css`:

```css
/* Header gradient */
header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Stat card accent colors */
.stat-card {
    border-left: 5px solid #667eea;  /* Your color */
}

/* Severity badges */
.severity-critical {
    background: #e74c3c;  /* Your color */
}
```

**Change Dashboard Title:**

Edit `frontend/index.html`:

```html
<h1>🛡️ My Custom SOC Dashboard</h1>
<p>Enterprise Security Monitoring</p>
```

---

### Modifying Detection Thresholds

**Brute Force Threshold:**

```python
# In detect_failed_logins() method
# Change from 5 to your preferred number
if len(self.failed_logins[ip]) > 10:  # Now requires 10+ attempts
```

**Traffic Spike Threshold:**

```python
# In detect_traffic_spike() method
# Change from 50 to your preferred number
if self.request_counts[timestamp] > 100:  # Now requires 100+ requests
```

**Time Window:**

```python
# In detect_failed_logins() method
# Change from 1 minute to 5 minutes
one_minute_ago = timestamp - timedelta(minutes=5)
```

---

### Adding New API Endpoints

Edit `backend/main.py`:

```python
@app.get("/api/alerts/recent")
def get_recent_alerts():
    """
    Get alerts from the last 24 hours
    """
    from datetime import datetime, timedelta
    
    all_alerts = database.get_all_alerts()
    yesterday = datetime.now() - timedelta(days=1)
    
    recent = [
        alert for alert in all_alerts 
        if datetime.strptime(alert['created_at'], "%Y-%m-%d %H:%M:%S") > yesterday
    ]
    
    return {
        "success": True,
        "count": len(recent),
        "alerts": recent
    }
```

---

### Expanding Database Schema

**Add new column to alerts table:**

Edit `backend/database.py`:

```python
def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            alert_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            ip_address TEXT,
            description TEXT NOT NULL,
            created_at TEXT NOT NULL,
            country TEXT,              -- NEW COLUMN
            resolved BOOLEAN DEFAULT 0 -- NEW COLUMN
        )
    """)
    
    conn.commit()
    conn.close()
```

**⚠️ Note:** Delete existing `alerts.db` after schema changes.

---

### Adding Email Alerts

Install package:
```bash
pip install python-dotenv smtplib
```

Add to `backend/main.py`:

```python
import smtplib
from email.message import EmailMessage

def send_email_alert(alert):
    """
    Send email notification for critical alerts
    """
    if alert['severity'] != 'Critical':
        return
    
    msg = EmailMessage()
    msg['Subject'] = f'🚨 CRITICAL ALERT: {alert["alert_type"]}'
    msg['From'] = 'soc@yourcompany.com'
    msg['To'] = 'admin@yourcompany.com'
    msg.set_content(f"""
    Alert Type: {alert['alert_type']}
    Severity: {alert['severity']}
    IP Address: {alert['ip_address']}
    Description: {alert['description']}
    Timestamp: {alert['timestamp']}
    """)
    
    # Configure your SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your-email@gmail.com', 'your-password')
        smtp.send_message(msg)

# Call it after saving alert
database.save_alert(...)
send_email_alert(alert)
```

---

### Adding Authentication

**Simple API Key Authentication:**

```python
from fastapi import Header, HTTPException

API_KEY = "your-secret-key-here"

@app.post("/api/upload-log")
async def upload_log_file(
    file: UploadFile = File(...),
    api_key: str = Header(None)
):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    # Rest of your code...
```

**Frontend (script.js):**

```javascript
const response = await fetch(`${API_URL}/api/upload-log`, {
    method: 'POST',
    headers: {
        'api-key': 'your-secret-key-here'
    },
    body: formData
});
```

---

### Real-Time Monitoring

**Add WebSocket support:**

```bash
pip install websockets
```

```python
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Push new alerts to connected clients
        new_alerts = get_new_alerts()
        await websocket.send_json(new_alerts)
        await asyncio.sleep(5)
```

---

### Export Alerts to CSV

Add endpoint in `backend/main.py`:

```python
import csv
from fastapi.responses import StreamingResponse
import io

@app.get("/api/alerts/export")
def export_alerts():
    """
    Export alerts to CSV file
    """
    alerts = database.get_all_alerts()
    
    # Create CSV in memory
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=[
        'id', 'timestamp', 'alert_type', 'severity', 
        'ip_address', 'description', 'created_at'
    ])
    
    writer.writeheader()
    writer.writerows(alerts)
    
    # Return as downloadable file
    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=alerts.csv"}
    )
```

**Frontend button:**

```html
<button onclick="exportAlerts()" class="btn btn-info">
    📥 Export to CSV
</button>
```

```javascript
function exportAlerts() {
    window.location.href = `${API_URL}/api/alerts/export`;
}
```

## 📝 Comprehensive Troubleshooting Guide

### Issue 1: Backend Server Won't Start

**Error Message:**
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution:**
```bash
# Install dependencies
pip install -r requirements.txt

# Or install individually
pip install fastapi uvicorn python-multipart pydantic
```

**Verify Installation:**
```bash
python -c "import fastapi, uvicorn; print('✓ Success!')"
```

---

**Error Message:**
```
Address already in use (Port 8000)
```

**Solution:**
```bash
# Windows - Find process using port 8000
netstat -ano | findstr :8000

# Kill process (replace PID with actual number)
taskkill /PID <PID> /F

# Linux/Mac - Find and kill process
lsof -ti:8000 | xargs kill -9
```

**Alternative:** Change port in `main.py`:
```python
uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
```

---

### Issue 2: Dashboard Can't Connect to API

**Symptoms:**
- Dashboard loads but shows "Error loading dashboard data"
- Console shows network errors
- Statistics show 0 alerts even after analyzing

**Solutions:**

**1. Check if backend is running:**
```bash
# Test in browser
http://127.0.0.1:8000

# Or use cURL
curl http://127.0.0.1:8000
```

Expected response: `{"message":"Mini SOC API is running!","version":"1.0.0","status":"healthy"}`

**2. Check CORS settings:**
- Open browser console (F12)
- Look for CORS errors
- Ensure backend has CORS middleware enabled (it does by default)

**3. Check API URL in frontend:**
Open `frontend/script.js` and verify:
```javascript
const API_URL = 'http://127.0.0.1:8000';  // Should match your backend
```

**4. Browser cache:**
```
Ctrl+Shift+R (hard refresh)
or
Clear browser cache
```

---

### Issue 3: Database Errors

**Error Message:**
```
sqlite3.OperationalError: no such table: alerts
```

**Solution:**
```bash
# Delete database and let it recreate
cd backend
del alerts.db    # Windows
rm alerts.db     # Linux/Mac

# Reinitialize
python database.py
```

---

**Error Message:**
```
sqlite3.OperationalError: database is locked
```

**Solution:**
- Close all programs accessing the database
- Restart the backend server
- Delete `.db-journal` file if it exists

---

### Issue 4: No Alerts Appearing

**Check 1: Log File Format**

Your log file MUST match this exact format:
```
[YYYY-MM-DD HH:MM:SS] IP_ADDRESS - ACTION - STATUS - URL
```

**Common Mistakes:**
- ❌ Missing brackets around timestamp
- ❌ Wrong date format
- ❌ Missing spaces around hyphens
- ❌ Invalid IP address format

**Check 2: Did You Click Analyze?**
- Select file from dropdown
- Click the "Analyze" button
- Wait for success message

**Check 3: Browser Console**
```
Press F12 → Console tab
Look for JavaScript errors
```

---

### Issue 5: Python Import Errors in VS Code

**Symptoms:**
- Red squiggly lines under imports
- "Import could not be resolved" warnings

**Solution 1: Select Python Interpreter**
```
Ctrl+Shift+P → "Python: Select Interpreter"
Choose the Python where packages are installed
```

**Solution 2: Reload Window**
```
Ctrl+Shift+P → "Developer: Reload Window"
```

**Solution 3: Install in VS Code Terminal**
```
# Use VS Code's integrated terminal
pip install -r requirements.txt
```

---

### Issue 6: Chart Not Displaying

**Check 1: Chart.js Loaded?**

Open browser console and run:
```javascript
typeof Chart
```

Should return: `"function"`

If `"undefined"`, add to `index.html`:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

**Check 2: Canvas Element Exists?**
```javascript
document.getElementById('alertsChart')
```

Should return: `<canvas id="alertsChart"></canvas>`

---

### Issue 7: Port Permission Errors

**Error (Linux/Mac):**
```
Permission denied: Port 8000
```

**Solution:**
```bash
# Use port > 1024 (no admin rights needed)
# Edit main.py, change port to 8080 or 8000

# Or run with sudo (not recommended)
sudo python main.py
```

---

### Issue 8: File Upload Not Working

**Check 1: File Size**
- Default limit: 10MB
- Ensure your log file isn't too large

**Check 2: File Extension**
```html
<input type="file" accept=".txt,.log">
```
- Only `.txt` and `.log` files accepted by default

**Check 3: Backend Logs**
```
Check terminal where backend is running
Look for error messages
```

---

### Issue 9: Slow Performance

**Symptoms:**
- Analysis takes too long
- Dashboard loads slowly

**Solutions:**

**1. Large Log Files:**
```python
# Split large files into smaller chunks
# Process in batches
```

**2. Too Many Alerts:**
```
Clear old alerts periodically
Use the "Clear All Alerts" button
```

**3. Browser Performance:**
```
Close unnecessary tabs
Disable browser extensions
Use Chrome/Edge for best performance
```

---

### Common Questions

**Q: Can I use this in production?**
A: No, this is educational only. It lacks security features like authentication, input validation, rate limiting, etc.

**Q: How do I add more detection rules?**
A: Edit `backend/log_analyzer.py` and add new detection methods to the `LogAnalyzer` class.

**Q: Can I change the port?**
A: Yes, edit `main.py` line 289: `uvicorn.run(..., port=YOUR_PORT)`

**Q: Does it work on Mac/Linux?**
A: Yes! Just use `python3` instead of `python` in commands.

**Q: Can I deploy this to a server?**
A: Yes, but add authentication, HTTPS, and security hardening first.

**Q: How do I reset everything?**
A: Delete `alerts.db`, restart server, refresh dashboard.

---

### Getting Help

**Debug Mode:**

Enable detailed logging in `main.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Check Logs:**
- Backend: Terminal where `python main.py` is running
- Frontend: Browser console (F12)

**Test Each Component:**

1. **Backend:**
   ```bash
   python -c "import database; database.init_database()"
   python -c "import log_analyzer; print('OK')"
   ```

2. **API:**
   ```bash
   curl http://127.0.0.1:8000
   ```

3. **Frontend:**
   - Open browser console (F12)
   - Look for errors

## � Future Enhancement Ideas

Want to take this project further? Here are ideas for expansion:

### Beginner Enhancements

1. **Add More Detection Rules**
   - Directory traversal attacks (`../../../etc/passwd`)
   - Cross-Site Scripting (XSS) attempts
   - Command injection patterns
   - Suspicious file uploads

2. **Improve UI/UX**
   - Dark mode toggle
   - Alert filtering by severity
   - Search functionality in alerts table
   - Pagination for large datasets
   - Sort alerts by different columns

3. **Enhanced Logging**
   - Log analysis history
   - Upload history tracking
   - System activity log
   - Error logging

### Intermediate Enhancements

4. **GeoIP Integration**
   - Show attacker's country
   - Map visualization of attacks
   - Block attacks from specific countries
   - GeoIP database integration

5. **Alert Management**
   - Mark alerts as "Resolved"
   - Add comments to alerts
   - Assign alerts to team members
   - Priority flagging

6. **Reporting Features**
   - Generate PDF reports
   - Schedule daily/weekly summaries
   - Export to different formats (JSON, XML)
   - Custom report templates

7. **Multi-User Support**
   - User authentication (login/logout)
   - Role-Based Access Control (RBAC)
   - User activity tracking
   - Admin dashboard

### Advanced Enhancements

8. **Machine Learning Detection**
   - Anomaly detection with scikit-learn
   - Pattern recognition
   - Predictive threat modeling
   - Auto-tuning detection thresholds

9. **Real-Time Monitoring**
   - WebSocket integration
   - Live log streaming
   - Real-time alerts
   - Auto-refresh dashboard

10. **Integration Features**
    - Slack/Discord notifications
    - Email alerts for critical threats
    - Integration with existing SIEM tools
    - Webhook support for external systems

11. **Advanced Analytics**
    - Threat intelligence feeds
    - IP reputation lookups
    - Correlation between different attack types
    - Attack pattern prediction

12. **Scalability**
    - PostgreSQL/MySQL instead of SQLite
    - Redis caching layer
    - Microservices architecture
    - Kubernetes deployment

### Enterprise Features

13. **Security Hardening**
    - HTTPS/SSL certificate
    - JWT authentication
    - Rate limiting
    - Input validation and sanitization
    - SQL injection prevention
    - CSRF protection

14. **Performance Optimization**
    - Async log processing
    - Queue-based analysis (RabbitMQ/Celery)
    - Batch processing for large files
    - Database indexing

15. **Compliance & Auditing**
    - Audit trails
    - Compliance reports (SOC 2, ISO 27001)
    - Data retention policies
    - GDPR compliance features

---

## 📚 Further Learning Resources

### Cybersecurity & Blue Team

**Online Courses:**
- [TryHackMe](https://tryhackme.com/) - SOC Level 1 Path
- [Blue Team Labs Online](https://blueteamlabs.online/)
- [Cybrary](https://www.cybrary.it/) - SOC Analyst courses
- [LetsDefend](https://letsdefend.io/) - SOC Analyst training

**Books:**
- "Blue Team Handbook" by Don Murdoch
- "The Practice of Network Security Monitoring" by Richard Bejtlich
- "Practical Malware Analysis" by Michael Sikorski
- "Security Operations Center" by Joseph Muniz

**Certifications:**
- CompTIA Security+
- Certified SOC Analyst (CSA)
- Blue Team Level 1 (BTL1)
- GIAC Security Essentials (GSEC)

### Web Development

**FastAPI:**
- [Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Full Course - YouTube](https://www.youtube.com/results?search_query=fastapi+tutorial)

**JavaScript:**
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [JavaScript.info](https://javascript.info/)
- [Chart.js Documentation](https://www.chartjs.org/docs/)

**Python:**
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python for Cybersecurity](https://www.cybrary.it/course/python/)

### Similar Projects to Build

1. **Port Scanner** - Scan networks for open ports
2. **Password Strength Checker** - Analyze password security
3. **Network Traffic Analyzer** - Parse packet captures
4. **Malware Hash Checker** - Check files against VirusTotal
5. **Phishing Email Detector** - Analyze email headers
6. **Web Vulnerability Scanner** - Automated security testing

---

## 🌟 Similar Tools & Technologies

### Professional SIEM Tools

**Open Source:**
- **Wazuh** - Host-based intrusion detection
- **OSSEC** - Open source HIDS
- **Security Onion** - Network security monitoring
- **ELK Stack** (Elasticsearch, Logstash, Kibana) - Log management
- **Graylog** - Centralized log management

**Commercial:**
- **Splunk** - Industry-leading SIEM
- **IBM QRadar** - Enterprise SIEM
- **AlienVault OSSIM** - Unified security management
- **LogRhythm** - Security analytics platform

### Technologies Similar to This Project

| Component | This Project | Enterprise Alternative |
|-----------|--------------|------------------------|
| Backend | FastAPI | Django, Flask, Node.js |
| Database | SQLite | PostgreSQL, MySQL, MongoDB |
| Frontend | Vanilla JS | React, Vue, Angular |
| Visualization | Chart.js | D3.js, Plotly, Grafana |
| Server | Uvicorn | Gunicorn, Nginx, Apache |
| Deployment | Local | Docker, Kubernetes, AWS |

---

## 🔐 Security Notes & Best Practices

**⚠️ IMPORTANT DISCLAIMERS:**

### This is an Educational Project

This Mini SOC system is designed for:
- ✅ Learning cybersecurity concepts
- ✅ Understanding log analysis
- ✅ Practicing web development
- ✅ Testing in local environments
- ✅ Portfolio demonstrations

**NOT suitable for:**
- ❌ Production environments
- ❌ Real security monitoring
- ❌ Protecting actual networks
- ❌ Compliance requirements
- ❌ Mission-critical systems

### Known Limitations

1. **No Authentication**
   - API endpoints are publicly accessible
   - No user management
   - No session handling

2. **Simplified Security**
   - CORS allows all origins (`*`)
   - No input validation/sanitization
   - No rate limiting
   - No encryption for data at rest

3. **Basic Detection**
   - Simple pattern matching only
   - No machine learning
   - No correlation between events
   - High false positive potential

4. **Limited Scalability**
   - SQLite not suitable for high traffic
   - Synchronous processing
   - Single-threaded analysis
   - No load balancing

5. **Database Security**
   - No encryption
   - No access controls
   - No backup mechanisms
   - No data validation

### Security Improvements for Production

If you want to deploy this (for learning purposes):

**1. Add HTTPS:**
```bash
# Use Let's Encrypt for free SSL
certbot --nginx -d yourdomain.com
```

**2. Implement Authentication:**
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.post("/api/upload-log")
async def upload_log(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Validate token
    pass
```

**3. Environment Variables:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
DB_PATH = os.getenv('DB_PATH')
```

**4. Input Validation:**
```python
from pydantic import BaseModel, validator

class AlertModel(BaseModel):
    ip_address: str
    
    @validator('ip_address')
    def validate_ip(cls, v):
        # Validate IP format
        import ipaddress
        ipaddress.ip_address(v)
        return v
```

**5. Rate Limiting:**
```bash
pip install slowapi
```

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/api/upload-log")
@limiter.limit("5/minute")
async def upload_log(request: Request):
    pass
```

---

## 💡 Tips & Best Practices

### For Beginners

1. **Read the code comments** - Every file has detailed explanations
2. **Start small** - Test with sample_log.txt first
3. **Check browser console** - Press F12 to see errors
4. **Use API docs** - Visit http://127.0.0.1:8000/docs
5. **One change at a time** - Test after each modification

### For Development

1. **Use version control** - Git is your friend
2. **Test frequently** - After each change
3. **Keep backups** - Of your database and code
4. **Comment your code** - Explain why, not what
5. **Follow conventions** - PEP 8 for Python, etc.

### For Learning

1. **Experiment** - Break things and fix them
2. **Add features gradually** - One at a time
3. **Read documentation** - FastAPI docs are excellent
4. **Join communities** - Reddit, Discord, Stack Overflow
5. **Build similar projects** - Apply what you learned

## ❓ Frequently Asked Questions (FAQ)

### General Questions

**Q: Is this a real SOC system?**
A: No, it's a simplified educational simulation to help you learn Blue Team concepts and web development.

**Q: Can I use this for my school/college project?**
A: Absolutely! It's designed for learning. Just remember to credit the source if required.

**Q: Do I need cybersecurity experience to use this?**
A: No! It's beginner-friendly. Basic Python and web development knowledge helps.

**Q: How long does it take to set up?**
A: 10-15 minutes for complete setup and first test.

**Q: Is it free?**
A: Yes, completely free and open source.

### Technical Questions

**Q: Can I run this on Windows/Mac/Linux?**
A: Yes! It works on all operating systems with Python 3.8+.

**Q: What Python version do I need?**
A: Python 3.8 or higher. Check with `python --version`.

**Q: Can I change the port number?**
A: Yes, edit `main.py` line 289: `uvicorn.run(..., port=YOUR_PORT)`.

**Q: Does the server need to stay running?**
A: Yes, keep the terminal open. The backend must run for the dashboard to work.

**Q: Can I access this from another device on my network?**
A: Yes! Replace `127.0.0.1` with your computer's IP address in `script.js`.

**Q: How much disk space does it need?**
A: Less than 50MB including dependencies.

**Q: Can I analyze really large log files?**
A: The system can handle files up to ~100MB. For larger files, split them into chunks.

### Feature Questions

**Q: Can I add my own detection rules?**
A: Yes! Edit `backend/log_analyzer.py` and add new detection methods.

**Q: Can I export alerts?**
A: Not by default, but you can add CSV export (see Customization Guide).

**Q: Does it detect all types of attacks?**
A: No, only 4 basic types. You can add more rules yourself.

**Q: Can I get email notifications?**
A: Not built-in, but you can add it (see Advanced Customization).

**Q: Does it work with real server logs?**
A: It works with any logs matching the required format (see Log File Format section).

### Troubleshooting Questions

**Q: Why do I see "Module not found" errors?**
A: Run `pip install -r requirements.txt` to install dependencies.

**Q: The dashboard shows 0 alerts after analyzing. Why?**
A: Check if: 1) You clicked "Analyze", 2) Log format is correct, 3) Backend is running.

**Q: Can I reset everything?**
A: Yes, delete `alerts.db` and restart the backend server.

**Q: The chart isn't showing. What's wrong?**
A: Ensure Chart.js is loaded. Check browser console (F12) for errors.

**Q: I get "Port already in use". How to fix?**
A: Another process is using port 8000. Either kill it or change the port in `main.py`.

### Development Questions

**Q: Can I modify the code?**
A: Yes! That's encouraged. Experiment and learn.

**Q: How do I contribute improvements?**
A: Make your changes and share them with the community.

**Q: Can I use this code in my own project?**
A: Yes, it's for educational purposes. Just credit appropriately if required.

**Q: What if I break something?**
A: Delete your changes and re-download the original files. Or use Git version control.

**Q: Where can I get help?**
A: Check the Troubleshooting Guide, read error messages, and use browser console (F12).

### Deployment Questions

**Q: Can I deploy this to the cloud?**
A: Yes, for learning. Use Heroku, AWS, or DigitalOcean. Add security first!

**Q: Is it production-ready?**
A: No. It lacks authentication, encryption, and production-grade security.

**Q: Can I use it for my company's security?**
A: No. Use professional SIEM tools like Splunk, Wazuh, or ELK Stack.

**Q: How do I scale it for many users?**
A: Replace SQLite with PostgreSQL, add Redis caching, use async processing.

---

## 🤝 Contributing & Community

This is a learning project, and contributions are welcome!

### How to Contribute

**Found a Bug?**
- Document the steps to reproduce
- Include error messages
- Share your environment details

**Have an Enhancement Idea?**
- Describe the feature
- Explain the use case
- Consider backward compatibility

**Want to Add Code?**
- Keep it beginner-friendly
- Add comments explaining your code
- Test thoroughly
- Document any new features

### Community Guidelines

- **Be respectful** - We're all learning
- **Be helpful** - Share knowledge generously
- **Be patient** - Everyone starts somewhere
- **Be curious** - Ask questions and experiment

### Project Goals

This project aims to:
1. ✅ Teach Blue Team cybersecurity concepts
2. ✅ Provide hands-on experience with log analysis
3. ✅ Demonstrate REST API development
4. ✅ Showcase data visualization techniques
5. ✅ Remain beginner-friendly and well-documented

---

## 📄 License & Usage

### Educational Use

This project is created for **educational purposes**.

**You are free to:**
- ✅ Use it for learning
- ✅ Modify the code
- ✅ Use it in school/college projects
- ✅ Share it with others
- ✅ Clone and experiment
- ✅ Build upon it for personal projects

**Attribution:**
If you use this project in coursework, presentations, or derived works, appropriate credit is appreciated but not required.

### Disclaimer

**NO WARRANTY:**
This software is provided "as is" without warranty of any kind. Use at your own risk.

**EDUCATIONAL ONLY:**
Not intended for production use. Not suitable for real security monitoring.

**NO LIABILITY:**
The creators are not responsible for any damage or security issues arising from use of this software.

---

## 📞 Support & Contact

### Getting Help

**Before asking for help:**
1. ✅ Read the README thoroughly
2. ✅ Check the Troubleshooting Guide
3. ✅ Search the FAQ
4. ✅ Look at browser console (F12)
5. ✅ Check backend terminal for errors

**When asking for help, include:**
- What you're trying to do
- What happened instead
- Error messages (exact text)
- Your operating system
- Python version (`python --version`)
- What you've already tried

### Resources

- **Documentation**: This README file
- **API Docs**: http://127.0.0.1:8000/docs (when running)
- **Code Comments**: Read the source files

---

## 🎉 Project Summary

### What You Built

Congratulations! You now have a functional **Mini SOC** system featuring:

**Backend:**
- ✅ REST API with 8 endpoints
- ✅ SQLite database for persistence
- ✅ 4 detection rules for common attacks
- ✅ Log parsing and analysis engine
- ✅ FastAPI web framework

**Frontend:**
- ✅ Interactive dashboard
- ✅ Real-time data visualization
- ✅ Statistics cards
- ✅ Alert management interface
- ✅ Chart.js graphs

**Features:**
- ✅ Upload and analyze log files
- ✅ Detect brute force attacks
- ✅ Identify SQL injection attempts
- ✅ Monitor admin access
- ✅ Spot traffic anomalies

### Skills Acquired

Through this project, you learned:
- 🎓 Backend API development
- 🎓 Database operations
- 🎓 Frontend development
- 🎓 Cybersecurity concepts
- 🎓 Log analysis techniques
- 🎓 Threat detection
- 🎓 Data visualization

### Next Steps

**Continue Learning:**
1. Add more detection rules
2. Improve the UI/UX
3. Integrate external APIs
4. Deploy to the cloud
5. Build similar projects
6. Contribute to open source

**Career Paths:**
- 🛡️ SOC Analyst
- 🔐 Security Engineer
- 💻 Full-Stack Developer
- 📊 Data Analyst
- ☁️ DevSecOps Engineer

---

## 🌟 Final Thoughts

**Congratulations on building your Mini SOC!** 🎉

You've created a functional cybersecurity monitoring system that demonstrates real-world Blue Team concepts. Whether you're learning cybersecurity, web development, or both, this project provides a solid foundation.

**Remember:**
- Keep experimenting and learning
- Security is a journey, not a destination
- Every expert was once a beginner
- The best way to learn is by doing

**What's Next?**
Take what you've learned and build something new. Modify this project, create your own tools, or contribute to open source. The cybersecurity community needs passionate learners like you!

---

**Happy Learning! 🎓🛡️**

**Stay curious. Stay secure.**

---

<div align="center">

### ⭐ If you found this project helpful, share it with others learning cybersecurity!

**Built with ❤️ for aspiring cybersecurity professionals**

*Last Updated: February 2026*

</div>
