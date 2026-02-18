# 🛠️ Technology Stack - Mini SOC

Complete overview of all technologies, libraries, and tools used in this project.

## Backend Stack

### Core Technologies

| Technology | Version | Purpose | Documentation |
|------------|---------|---------|---------------|
| **Python** | 3.8+ | Programming language | [python.org](https://www.python.org/) |
| **FastAPI** | 0.104.1 | Web framework for APIs | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) |
| **Uvicorn** | 0.24.0 | ASGI web server | [uvicorn.org](https://www.uvicorn.org/) |
| **SQLite** | Built-in | Embedded database | [sqlite.org](https://www.sqlite.org/) |
| **Pydantic** | 2.5.0 | Data validation | [pydantic.dev](https://pydantic.dev/) |
| **Python-multipart** | 0.0.6 | File upload handling | [GitHub](https://github.com/andrew-d/python-multipart) |

### Why These Technologies?

**FastAPI:**
- ✅ Modern and fast (high performance)
- ✅ Easy to learn for beginners
- ✅ Automatic API documentation
- ✅ Type hints support
- ✅ Async capabilities

**SQLite:**
- ✅ No separate database server needed
- ✅ Zero configuration
- ✅ File-based (portable)
- ✅ Perfect for learning and prototyping
- ⚠️ Not for high-traffic production

**Uvicorn:**
- ✅ Lightning-fast ASGI server
- ✅ Production-ready
- ✅ Hot reload during development
- ✅ WebSocket support

---

## Frontend Stack

### Core Technologies

| Technology | Version | Purpose | Source |
|------------|---------|---------|--------|
| **HTML5** | - | Structure and markup | Standard |
| **CSS3** | - | Styling and design | Standard |
| **JavaScript (ES6+)** | - | Interactivity | Standard |
| **Chart.js** | 4.4.0 | Data visualization | [chartjs.org](https://www.chartjs.org/) |

### Frontend Architecture

**HTML5 Features Used:**
- Semantic elements (`<header>`, `<section>`, `<footer>`)
- Form elements (`<input type="file">`)
- Canvas element (for Chart.js)
- Table structures
- Responsive meta viewport

**CSS3 Features Used:**
- Flexbox layout
- Grid layout
- Gradients (linear)
- Transitions and animations
- Custom properties (variables)
- Media queries (responsive design)
- Box shadow effects

**JavaScript ES6+ Features Used:**
- `async/await` for asynchronous operations
- Arrow functions
- Template literals
- Destructuring
- `fetch()` API for HTTP requests
- Modules (potential)
- `const` and `let` declarations

**Chart.js:**
- ✅ Easy to use
- ✅ Responsive charts
- ✅ Interactive tooltips
- ✅ Multiple chart types
- ✅ Beautiful out-of-the-box

---

## Python Libraries Deep Dive

### 1. FastAPI (Web Framework)

```python
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
```

**Key Features Used:**
- Routing decorators (`@app.get`, `@app.post`)
- Dependency injection
- Request/Response models
- Middleware (CORS)
- Automatic data validation
- File upload handling
- Path and query parameters
- JSON serialization

**Why not Flask/Django?**
- FastAPI is faster
- Built-in async support
- Automatic API documentation
- Modern Python type hints
- Better for APIs

---

### 2. SQLite3 (Database)

```python
import sqlite3
```

**Features Used:**
- Table creation (`CREATE TABLE`)
- Data insertion (`INSERT`)
- Data retrieval (`SELECT`)
- Data deletion (`DELETE`)
- Row factory for dict-like access
- Connection and cursor management
- Transaction management (`commit()`)

**Schema Design:**
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

---

### 3. Standard Library Modules

**datetime:**
```python
from datetime import datetime, timedelta
```
- Timestamp parsing
- Time window calculations
- Date formatting

**re (Regular Expressions):**
```python
import re
```
- Log line parsing
- Pattern matching
- Text extraction

**collections:**
```python
from collections import defaultdict
```
- Tracking failed login attempts
- Request counting
- Efficient data structures

**os:**
```python
import os
```
- File path operations
- Directory creation
- Environment variables (potential)

---

## Development Tools

### Recommended

| Tool | Purpose | Platform |
|------|---------|----------|
| **VS Code** | Code editor | Windows/Mac/Linux |
| **Git** | Version control | All |
| **PowerShell/Bash** | Terminal | Windows/Unix |
| **Chrome DevTools** | Frontend debugging | Browser |
| **Postman** | API testing | All |

### VS Code Extensions (Optional)

- Python (Microsoft)
- Pylance (Python IntelliSense)
- Better Comments
- Material Icon Theme
- Live Server
- Thunder Client (API testing)

---

## API Architecture

### RESTful Design Principles

**Endpoints Structure:**
```
GET    /                         # Health check
POST   /api/upload-log           # Upload file
POST   /api/analyze-log/{file}   # Analyze file
GET    /api/alerts               # Get all alerts
GET    /api/alerts/count         # Get count
GET    /api/alerts/stats         # Get statistics
DELETE /api/alerts               # Delete all
GET    /api/logs/list            # List files
```

**Design Patterns:**
- Resource-based URLs
- HTTP verbs for actions
- JSON request/response
- Proper status codes
- CORS enabled
- Consistent error handling

---

## Security Technologies

### Currently Implemented

**CORS Middleware:**
```python
from fastapi.middleware.cors import CORSMiddleware
```
- Allows cross-origin requests
- Configured for all origins (development)
- Should be restricted in production

### Not Implemented (Educational Project)

⚠️ **Missing for production:**
- Authentication (JWT, OAuth)
- Authorization (RBAC)
- Input validation (comprehensive)
- Rate limiting
- HTTPS/SSL
- SQL injection prevention (prepared statements used)
- XSS prevention
- CSRF protection
- Encryption at rest

---

## Data Flow Technologies

### Request Lifecycle

```
Browser (Frontend)
    ↓ [HTTP/HTTPS]
FastAPI (Backend)
    ↓ [Function Call]
Log Analyzer (Processing)
    ↓ [SQL Query]
SQLite Database (Storage)
    ↓ [Response]
JSON Response
    ↓ [HTTP]
Frontend Update (DOM Manipulation)
```

### Technologies at Each Layer

1. **Client Layer**
   - JavaScript Fetch API
   - FormData API
   - DOM API

2. **Server Layer**
   - FastAPI routing
   - Uvicorn ASGI server
   - Python asyncio

3. **Business Logic**
   - Python classes
   - Regular expressions
   - Algorithm implementation

4. **Data Layer**
   - SQLite database
   - SQL queries
   - File system I/O

---

## Visualization Stack

### Chart.js Integration

**Library:**
- Chart.js v4.4.0
- Downloaded from CDN

**Chart Configuration:**
```javascript
{
    type: 'line',           // Chart type
    data: {...},            // Dataset
    options: {
        responsive: true,    // Auto-resize
        plugins: {...},      // Customization
        scales: {...}        // Axis configuration
    }
}
```

**Features Used:**
- Line charts
- Custom colors
- Interactive tooltips
- Responsive design
- Grid customization
- Legend display

---

## File Structure & Organization

```
mini-soc/
├── backend/              # Python backend
│   ├── main.py          # FastAPI app (9KB)
│   ├── database.py      # SQLite operations (3KB)
│   ├── log_analyzer.py  # Detection engine (9KB)
│   └── alerts.db        # Database file (auto-generated)
├── frontend/            # Web frontend
│   ├── index.html       # UI structure
│   ├── styles.css       # Styling
│   └── script.js        # Interactivity
├── logs/                # Log files
│   └── sample_log.txt   # Sample data
├── requirements.txt     # Python dependencies
├── README.md           # Documentation
├── QUICKSTART.md       # Quick setup guide
└── TECH_STACK.md       # This file
```

---

## Dependency Management

### Python Dependencies

**requirements.txt:**
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6
pydantic==2.5.0
```

**Installation:**
```bash
pip install -r requirements.txt
```

**Virtual Environment (Recommended):**
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install
pip install -r requirements.txt
```

### Frontend Dependencies

**Chart.js:**
- Loaded via CDN (no installation needed)
- `https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js`

---

## Performance Considerations

### Backend

**Strengths:**
- ✅ Fast API response times
- ✅ Efficient SQLite queries
- ✅ Minimal memory footprint

**Limitations:**
- ⚠️ Synchronous log processing
- ⚠️ Single-threaded analysis
- ⚠️ SQLite not for concurrent writes

**Optimization Opportunities:**
- Use async processing
- Implement caching (Redis)
- Batch database operations
- Add indexing to database

### Frontend

**Strengths:**
- ✅ Vanilla JS (no framework overhead)
- ✅ Minimal external dependencies
- ✅ Efficient DOM updates

**Limitations:**
- ⚠️ No virtual DOM
- ⚠️ Manual state management
- ⚠️ Large tables can be slow

**Optimization Opportunities:**
- Implement pagination
- Use virtual scrolling
- Lazy load chart data
- Add service workers

---

## Deployment Options

### Local Development
- ✅ Current setup
- Uvicorn development server
- File-based database

### Production (If Needed)

**Docker:**
```dockerfile
FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

**Cloud Platforms:**
- Heroku (Free tier)
- AWS (EC2, Elastic Beanstalk)
- DigitalOcean (Droplets)
- Google Cloud Platform
- Azure

**Database Upgrade:**
- PostgreSQL (production)
- MySQL (alternative)
- MongoDB (NoSQL option)

---

## Learning Resources

### Official Documentation

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Python Docs](https://docs.python.org/)
- [Chart.js Docs](https://www.chartjs.org/docs/)
- [SQLite Docs](https://www.sqlite.org/docs.html)
- [MDN Web Docs](https://developer.mozilla.org/)

### Tutorials

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [JavaScript Tutorial](https://javascript.info/)
- [Chart.js Getting Started](https://www.chartjs.org/docs/latest/getting-started/)

---

## Technology Comparison

### Alternative Stacks

**MERN Stack:**
- MongoDB, Express, React, Node.js
- More complex but scalable

**Django Stack:**
- Django, PostgreSQL, Bootstrap
- More batteries-included

**Flask Stack:**
- Flask, SQLAlchemy, Jinja2
- More lightweight but less features

**Why This Stack?**
- ✅ Simple to learn
- ✅ Fast development
- ✅ Modern Python features
- ✅ Automatic documentation
- ✅ Minimal dependencies

---

## Summary

This Mini SOC project uses a **modern, lightweight, beginner-friendly stack**:

**Backend:** Python + FastAPI + SQLite
**Frontend:** HTML + CSS + Vanilla JS + Chart.js
**Server:** Uvicorn ASGI

**Perfect for:**
- 🎓 Learning web development
- 🔐 Understanding cybersecurity concepts
- 💻 Building portfolio projects
- 🚀 Rapid prototyping

**Not suitable for:**
- ❌ Enterprise production
- ❌ High-traffic applications
- ❌ Mission-critical systems

---

*For questions about specific technologies, consult the official documentation linked above.*
