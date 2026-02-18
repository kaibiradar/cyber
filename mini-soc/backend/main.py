"""
Mini SOC - Log Monitoring and Alert System
Main FastAPI Application

This is a beginner-friendly Blue Team cybersecurity project that:
- Monitors log files for suspicious activities
- Detects various types of attacks
- Stores alerts in a database
- Provides a REST API for the frontend dashboard
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from datetime import datetime

# Import our custom modules
import database
import log_analyzer

# Create FastAPI application instance
app = FastAPI(
    title="Mini SOC API",
    description="Log Monitoring and Alert System API",
    version="1.0.0"
)

# Enable CORS (Cross-Origin Resource Sharing) so frontend can access the API
# This allows our HTML/JS frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Initialize database when application starts
database.init_database()

# Create log analyzer instance
analyzer = log_analyzer.LogAnalyzer()


@app.get("/")
def root():
    """
    Root endpoint - API health check
    """
    return {
        "message": "Mini SOC API is running!",
        "version": "1.0.0",
        "status": "healthy"
    }


@app.post("/api/upload-log")
async def upload_log_file(file: UploadFile = File(...)):
    """
    Upload a log file and analyze it for suspicious activities
    
    Args:
        file: The uploaded log file
        
    Returns:
        JSON response with analysis results
    """
    try:
        # Read the uploaded file content
        content = await file.read()
        log_content = content.decode('utf-8')
        
        # Save the uploaded file (optional, for record keeping)
        upload_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        os.makedirs(upload_dir, exist_ok=True)
        
        file_path = os.path.join(upload_dir, f"uploaded_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(file_path, 'w') as f:
            f.write(log_content)
        
        # Analyze the log content
        alerts = analyzer.analyze_log_content(log_content)
        
        # Save all detected alerts to database
        for alert in alerts:
            database.save_alert(
                timestamp=alert['timestamp'],
                alert_type=alert['alert_type'],
                severity=alert['severity'],
                ip_address=alert['ip_address'],
                description=alert['description']
            )
        
        return {
            "success": True,
            "message": f"Log file analyzed successfully",
            "alerts_detected": len(alerts),
            "file_saved": file_path
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


@app.post("/api/analyze-log/{filename}")
def analyze_existing_log(filename: str):
    """
    Analyze an existing log file from the logs directory
    
    Args:
        filename: Name of the log file to analyze
        
    Returns:
        JSON response with analysis results
    """
    try:
        # Construct file path
        logs_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        file_path = os.path.join(logs_dir, filename)
        
        # Check if file exists
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail=f"Log file '{filename}' not found")
        
        # Analyze the log file
        alerts = analyzer.analyze_log_file(file_path)
        
        # Save all detected alerts to database
        saved_count = 0
        for alert in alerts:
            database.save_alert(
                timestamp=alert['timestamp'],
                alert_type=alert['alert_type'],
                severity=alert['severity'],
                ip_address=alert['ip_address'],
                description=alert['description']
            )
            saved_count += 1
        
        return {
            "success": True,
            "message": f"Analyzed {filename}",
            "alerts_detected": len(alerts),
            "alerts_saved": saved_count
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing file: {str(e)}")


@app.get("/api/alerts")
def get_alerts():
    """
    Retrieve all alerts from the database
    
    Returns:
        JSON response with all alerts
    """
    try:
        alerts = database.get_all_alerts()
        total_count = database.get_alerts_count()
        
        return {
            "success": True,
            "total": total_count,
            "alerts": alerts
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving alerts: {str(e)}")


@app.get("/api/alerts/count")
def get_alerts_count():
    """
    Get the total count of alerts
    
    Returns:
        JSON response with alert count
    """
    try:
        count = database.get_alerts_count()
        
        return {
            "success": True,
            "count": count
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting alerts: {str(e)}")


@app.get("/api/alerts/stats")
def get_alert_statistics():
    """
    Get statistics about alerts (for dashboard graphs)
    
    Returns:
        JSON response with alert statistics grouped by type and time
    """
    try:
        alerts = database.get_all_alerts()
        
        # Count alerts by type
        alerts_by_type = {}
        alerts_by_severity = {}
        alerts_by_hour = {}
        
        for alert in alerts:
            # Count by type
            alert_type = alert['alert_type']
            alerts_by_type[alert_type] = alerts_by_type.get(alert_type, 0) + 1
            
            # Count by severity
            severity = alert['severity']
            alerts_by_severity[severity] = alerts_by_severity.get(severity, 0) + 1
            
            # Count by hour (for time-based graph)
            try:
                timestamp = alert['timestamp']
                hour = timestamp[:13]  # Extract "YYYY-MM-DD HH"
                alerts_by_hour[hour] = alerts_by_hour.get(hour, 0) + 1
            except:
                pass
        
        return {
            "success": True,
            "by_type": alerts_by_type,
            "by_severity": alerts_by_severity,
            "by_hour": alerts_by_hour
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting statistics: {str(e)}")


@app.delete("/api/alerts")
def clear_alerts():
    """
    Delete all alerts from the database
    
    Returns:
        JSON response confirming deletion
    """
    try:
        database.clear_all_alerts()
        
        return {
            "success": True,
            "message": "All alerts cleared successfully"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error clearing alerts: {str(e)}")


@app.get("/api/logs/list")
def list_log_files():
    """
    List all available log files in the logs directory
    
    Returns:
        JSON response with list of log files
    """
    try:
        logs_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        
        # Create logs directory if it doesn't exist
        os.makedirs(logs_dir, exist_ok=True)
        
        # Get all .txt files in the logs directory
        log_files = [f for f in os.listdir(logs_dir) if f.endswith('.txt')]
        
        return {
            "success": True,
            "count": len(log_files),
            "files": log_files
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing log files: {str(e)}")


# Run the application
if __name__ == "__main__":
    import uvicorn
    
    print("=" * 60)
    print("🛡️  MINI SOC - Log Monitoring and Alert System")
    print("=" * 60)
    print("Starting FastAPI server...")
    print("API will be available at: http://127.0.0.1:8000")
    print("API documentation at: http://127.0.0.1:8000/docs")
    print("=" * 60)
    
    # Start the server
    # host="0.0.0.0" makes it accessible from other devices on the network
    # port=8000 is the default port
    # reload=True automatically restarts server when code changes (useful for development)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
