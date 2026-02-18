"""
Database Module - Handles SQLite database operations for storing alerts
This module creates and manages the alerts database
"""

import sqlite3
from datetime import datetime
import os

# Database file path
DB_PATH = os.path.join(os.path.dirname(__file__), "alerts.db")


def init_database():
    """
    Initialize the SQLite database and create the alerts table if it doesn't exist
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create alerts table with necessary columns
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            alert_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            ip_address TEXT,
            description TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    print("✓ Database initialized successfully")


def save_alert(timestamp, alert_type, severity, ip_address, description):
    """
    Save a new alert to the database
    
    Args:
        timestamp: When the suspicious activity occurred
        alert_type: Type of alert (e.g., 'Failed Login', 'SQL Injection')
        severity: Alert severity ('Low', 'Medium', 'High', 'Critical')
        ip_address: IP address involved in the activity
        description: Detailed description of the alert
    
    Returns:
        int: The ID of the newly created alert
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""
        INSERT INTO alerts (timestamp, alert_type, severity, ip_address, description, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (timestamp, alert_type, severity, ip_address, description, created_at))
    
    alert_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return alert_id


def get_all_alerts():
    """
    Retrieve all alerts from the database
    
    Returns:
        list: List of dictionaries containing alert information
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM alerts ORDER BY created_at DESC")
    rows = cursor.fetchall()
    
    # Convert rows to list of dictionaries
    alerts = [dict(row) for row in rows]
    
    conn.close()
    return alerts


def get_alerts_count():
    """
    Get the total number of alerts in the database
    
    Returns:
        int: Total count of alerts
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM alerts")
    count = cursor.fetchone()[0]
    
    conn.close()
    return count


def clear_all_alerts():
    """
    Delete all alerts from the database (useful for testing)
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM alerts")
    
    conn.commit()
    conn.close()
    print("✓ All alerts cleared")


# Initialize database when this module is imported
if __name__ == "__main__":
    init_database()
