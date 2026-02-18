"""
Log Analyzer Module - Contains detection rules for identifying suspicious activities
This module analyzes log entries and detects various types of attacks
"""

from datetime import datetime, timedelta
from collections import defaultdict
import re


class LogAnalyzer:
    """
    Analyzes log files for suspicious activities and security threats
    """
    
    def __init__(self):
        # Track failed login attempts: {ip_address: [(timestamp1, timestamp2, ...)]}
        self.failed_logins = defaultdict(list)
        
        # Track total requests per minute for traffic spike detection
        self.request_counts = defaultdict(int)
        
        # SQL injection keywords to detect
        self.sql_keywords = [
            'SELECT', 'UNION', 'DROP', 'DELETE', 'INSERT', 
            'UPDATE', 'OR 1=1', 'OR 1 = 1', '--', 'EXEC',
            'EXECUTE', 'SCRIPT', 'JAVASCRIPT', 'ONERROR'
        ]
    
    
    def parse_log_line(self, log_line):
        """
        Parse a log line and extract important information
        
        Expected log format:
        [TIMESTAMP] IP_ADDRESS - ACTION - STATUS - URL
        Example: [2024-01-15 14:23:45] 192.168.1.100 - LOGIN - FAILED - /admin
        
        Args:
            log_line: Single line from the log file
            
        Returns:
            dict: Parsed log information or None if parsing fails
        """
        try:
            # Regular expression to parse log format
            pattern = r'\[(.*?)\]\s+([\d\.]+)\s+-\s+(.*?)\s+-\s+(.*?)\s+-\s+(.*?)$'
            match = re.match(pattern, log_line.strip())
            
            if match:
                return {
                    'timestamp': match.group(1),
                    'ip_address': match.group(2),
                    'action': match.group(3),
                    'status': match.group(4),
                    'url': match.group(5)
                }
        except Exception as e:
            print(f"Error parsing log line: {e}")
        
        return None
    
    
    def detect_failed_logins(self, log_entry):
        """
        Detect multiple failed login attempts from the same IP
        Rule: More than 5 failed login attempts within 1 minute
        
        Args:
            log_entry: Parsed log entry dictionary
            
        Returns:
            dict: Alert information if detected, None otherwise
        """
        if log_entry['action'] == 'LOGIN' and log_entry['status'] == 'FAILED':
            ip = log_entry['ip_address']
            timestamp = datetime.strptime(log_entry['timestamp'], "%Y-%m-%d %H:%M:%S")
            
            # Add this failed attempt to tracking
            self.failed_logins[ip].append(timestamp)
            
            # Remove attempts older than 1 minute
            one_minute_ago = timestamp - timedelta(minutes=1)
            self.failed_logins[ip] = [
                t for t in self.failed_logins[ip] if t > one_minute_ago
            ]
            
            # Check if more than 5 failed attempts in the last minute
            if len(self.failed_logins[ip]) > 5:
                return {
                    'timestamp': log_entry['timestamp'],
                    'alert_type': 'Brute Force Attack',
                    'severity': 'High',
                    'ip_address': ip,
                    'description': f'Detected {len(self.failed_logins[ip])} failed login attempts from {ip} within 1 minute'
                }
        
        return None
    
    
    def detect_sql_injection(self, log_entry):
        """
        Detect SQL injection attempts in URLs
        Rule: Check for SQL keywords in URL parameters
        
        Args:
            log_entry: Parsed log entry dictionary
            
        Returns:
            dict: Alert information if detected, None otherwise
        """
        url = log_entry['url'].upper()
        
        # Check if any SQL keyword is in the URL
        for keyword in self.sql_keywords:
            if keyword in url:
                return {
                    'timestamp': log_entry['timestamp'],
                    'alert_type': 'SQL Injection Attempt',
                    'severity': 'Critical',
                    'ip_address': log_entry['ip_address'],
                    'description': f'SQL injection keyword "{keyword}" detected in URL: {log_entry["url"]}'
                }
        
        return None
    
    
    def detect_admin_access(self, log_entry):
        """
        Detect attempts to access admin pages
        Rule: Any request to URLs containing 'admin'
        
        Args:
            log_entry: Parsed log entry dictionary
            
        Returns:
            dict: Alert information if detected, None otherwise
        """
        url = log_entry['url'].lower()
        
        if 'admin' in url or 'administrator' in url:
            # Determine severity based on success/failure
            severity = 'Critical' if log_entry['status'] == 'SUCCESS' else 'Medium'
            
            return {
                'timestamp': log_entry['timestamp'],
                'alert_type': 'Admin Access Attempt',
                'severity': severity,
                'ip_address': log_entry['ip_address'],
                'description': f'Admin page access attempt from {log_entry["ip_address"]}: {log_entry["url"]} - Status: {log_entry["status"]}'
            }
        
        return None
    
    
    def detect_traffic_spike(self, log_entry):
        """
        Detect unusual traffic spikes (potential DDoS)
        Rule: More than 50 requests in the same minute
        
        Args:
            log_entry: Parsed log entry dictionary
            
        Returns:
            dict: Alert information if detected, None otherwise
        """
        # Extract minute from timestamp (ignore seconds)
        timestamp = log_entry['timestamp'][:16]  # Format: "YYYY-MM-DD HH:MM"
        
        # Increment request count for this minute
        self.request_counts[timestamp] += 1
        
        # Check if traffic exceeds threshold
        if self.request_counts[timestamp] > 50:
            # Only alert once per minute when threshold is first exceeded
            if self.request_counts[timestamp] == 51:
                return {
                    'timestamp': log_entry['timestamp'],
                    'alert_type': 'Traffic Spike Detected',
                    'severity': 'High',
                    'ip_address': 'Multiple',
                    'description': f'Unusual traffic spike detected: {self.request_counts[timestamp]} requests at {timestamp}'
                }
        
        return None
    
    
    def analyze_log_entry(self, log_line):
        """
        Analyze a single log entry against all detection rules
        
        Args:
            log_line: Single line from log file
            
        Returns:
            list: List of alerts detected (can be multiple alerts per line)
        """
        alerts = []
        
        # Parse the log line
        log_entry = self.parse_log_line(log_line)
        
        if not log_entry:
            return alerts
        
        # Run all detection rules
        detection_rules = [
            self.detect_failed_logins,
            self.detect_sql_injection,
            self.detect_admin_access,
            self.detect_traffic_spike
        ]
        
        for rule in detection_rules:
            alert = rule(log_entry)
            if alert:
                alerts.append(alert)
        
        return alerts
    
    
    def analyze_log_file(self, file_path):
        """
        Analyze an entire log file
        
        Args:
            file_path: Path to the log file
            
        Returns:
            list: List of all alerts detected in the file
        """
        all_alerts = []
        
        try:
            with open(file_path, 'r') as file:
                for line_number, line in enumerate(file, 1):
                    alerts = self.analyze_log_entry(line)
                    all_alerts.extend(alerts)
            
            print(f"✓ Analyzed {line_number} log entries")
            print(f"✓ Detected {len(all_alerts)} alerts")
            
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        except Exception as e:
            print(f"Error analyzing log file: {e}")
        
        return all_alerts
    
    
    def analyze_log_content(self, content):
        """
        Analyze log content (text) instead of a file
        
        Args:
            content: Log content as string
            
        Returns:
            list: List of all alerts detected
        """
        all_alerts = []
        
        lines = content.split('\n')
        for line in lines:
            if line.strip():  # Skip empty lines
                alerts = self.analyze_log_entry(line)
                all_alerts.extend(alerts)
        
        return all_alerts
