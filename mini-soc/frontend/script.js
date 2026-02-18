/**
 * Mini SOC Dashboard - JavaScript
 * Handles all frontend interactions and API communication
 */

// API Base URL - Change this if your backend runs on a different port
const API_URL = 'http://127.0.0.1:8000';

// Chart.js instance (global variable)
let alertsChart = null;

/**
 * Initialize the dashboard when page loads
 */
document.addEventListener('DOMContentLoaded', function() {
    console.log('🛡️ Mini SOC Dashboard Loaded');
    
    // Load initial data
    loadDashboard();
    
    // Load available log files for the dropdown
    loadLogFilesList();
    
    // Set up auto-refresh every 30 seconds (optional)
    // setInterval(loadDashboard, 30000);
});


/**
 * Load all dashboard data (alerts, statistics, chart)
 */
async function loadDashboard() {
    console.log('Loading dashboard data...');
    
    try {
        // Fetch alerts from API
        const response = await fetch(`${API_URL}/api/alerts`);
        const data = await response.json();
        
        if (data.success) {
            // Update statistics cards
            updateStatistics(data.alerts);
            
            // Update alerts table
            updateAlertsTable(data.alerts);
            
            // Update chart
            await updateChart();
            
            console.log('✓ Dashboard loaded successfully');
        }
    } catch (error) {
        console.error('Error loading dashboard:', error);
        showMessage('Error loading dashboard data. Make sure the backend server is running.', 'error');
    }
}


/**
 * Update the statistics cards with alert counts
 */
function updateStatistics(alerts) {
    // Count total alerts
    const totalAlerts = alerts.length;
    document.getElementById('totalAlerts').textContent = totalAlerts;
    
    // Count alerts by severity
    let criticalCount = 0;
    let highCount = 0;
    let mediumCount = 0;
    
    alerts.forEach(alert => {
        switch(alert.severity.toLowerCase()) {
            case 'critical':
                criticalCount++;
                break;
            case 'high':
                highCount++;
                break;
            case 'medium':
                mediumCount++;
                break;
        }
    });
    
    document.getElementById('criticalAlerts').textContent = criticalCount;
    document.getElementById('highAlerts').textContent = highCount;
    document.getElementById('mediumAlerts').textContent = mediumCount;
}


/**
 * Update the alerts table with data
 */
function updateAlertsTable(alerts) {
    const tableBody = document.getElementById('alertsTableBody');
    
    // Clear existing rows
    tableBody.innerHTML = '';
    
    // If no alerts, show message
    if (alerts.length === 0) {
        tableBody.innerHTML = `
            <tr>
                <td colspan="6" class="no-alerts">
                    No alerts detected yet. Upload or analyze a log file to get started.
                </td>
            </tr>
        `;
        return;
    }
    
    // Add rows for each alert
    alerts.forEach(alert => {
        const row = document.createElement('tr');
        
        // Get severity badge class
        const severityClass = `severity-${alert.severity.toLowerCase()}`;
        
        row.innerHTML = `
            <td>${alert.id}</td>
            <td>${alert.timestamp}</td>
            <td class="alert-type">${alert.alert_type}</td>
            <td><span class="${severityClass}">${alert.severity}</span></td>
            <td>${alert.ip_address}</td>
            <td>${alert.description}</td>
        `;
        
        tableBody.appendChild(row);
    });
}


/**
 * Update or create the alerts chart
 */
async function updateChart() {
    try {
        // Fetch statistics from API
        const response = await fetch(`${API_URL}/api/alerts/stats`);
        const data = await response.json();
        
        if (!data.success) {
            console.error('Failed to fetch statistics');
            return;
        }
        
        // Prepare data for chart
        const alertsByHour = data.by_hour || {};
        const labels = Object.keys(alertsByHour).sort();
        const values = labels.map(label => alertsByHour[label]);
        
        // Get canvas context
        const ctx = document.getElementById('alertsChart').getContext('2d');
        
        // Destroy existing chart if it exists
        if (alertsChart) {
            alertsChart.destroy();
        }
        
        // Create new chart
        alertsChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels.length > 0 ? labels : ['No Data'],
                datasets: [{
                    label: 'Alerts Detected',
                    data: values.length > 0 ? values : [0],
                    backgroundColor: 'rgba(44, 83, 100, 0.2)',
                    borderColor: 'rgba(44, 83, 100, 1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: 'rgba(244, 67, 54, 1)',
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2,
                    pointRadius: 5,
                    pointHoverRadius: 7
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                        labels: {
                            font: {
                                size: 14,
                                weight: 'bold'
                            }
                        }
                    },
                    title: {
                        display: true,
                        text: 'Attack Timeline',
                        font: {
                            size: 16,
                            weight: 'bold'
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1,
                            font: {
                                size: 12
                            }
                        },
                        title: {
                            display: true,
                            text: 'Number of Alerts',
                            font: {
                                size: 14,
                                weight: 'bold'
                            }
                        }
                    },
                    x: {
                        ticks: {
                            font: {
                                size: 11
                            },
                            maxRotation: 45,
                            minRotation: 45
                        },
                        title: {
                            display: true,
                            text: 'Time',
                            font: {
                                size: 14,
                                weight: 'bold'
                            }
                        }
                    }
                }
            }
        });
        
    } catch (error) {
        console.error('Error updating chart:', error);
    }
}


/**
 * Upload and analyze a log file
 */
async function uploadLogFile() {
    const fileInput = document.getElementById('fileUpload');
    const file = fileInput.files[0];
    
    if (!file) {
        showMessage('Please select a file to upload', 'error');
        return;
    }
    
    // Create FormData object
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        showMessage('Uploading and analyzing log file...', 'info');
        
        // Upload file to API
        const response = await fetch(`${API_URL}/api/upload-log`, {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            showMessage(`✓ Success! Detected ${data.alerts_detected} alerts`, 'success');
            
            // Reload dashboard to show new alerts
            setTimeout(() => {
                loadDashboard();
            }, 1000);
            
            // Clear file input
            fileInput.value = '';
        } else {
            showMessage('Error analyzing file', 'error');
        }
        
    } catch (error) {
        console.error('Error uploading file:', error);
        showMessage('Error uploading file. Make sure the backend server is running.', 'error');
    }
}


/**
 * Load list of available log files
 */
async function loadLogFilesList() {
    try {
        const response = await fetch(`${API_URL}/api/logs/list`);
        const data = await response.json();
        
        if (data.success) {
            const select = document.getElementById('logFileSelect');
            
            // Clear existing options except the first one
            select.innerHTML = '<option value="">Select a log file...</option>';
            
            // Add options for each log file
            data.files.forEach(filename => {
                const option = document.createElement('option');
                option.value = filename;
                option.textContent = filename;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Error loading log files list:', error);
    }
}


/**
 * Analyze a selected log file from the dropdown
 */
async function analyzeSelectedLog() {
    const select = document.getElementById('logFileSelect');
    const filename = select.value;
    
    if (!filename) {
        showMessage('Please select a log file to analyze', 'error');
        return;
    }
    
    try {
        showMessage('Analyzing log file...', 'info');
        
        // Call API to analyze the selected file
        const response = await fetch(`${API_URL}/api/analyze-log/${filename}`, {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (data.success) {
            showMessage(`✓ Success! Detected ${data.alerts_detected} alerts`, 'success');
            
            // Reload dashboard to show new alerts
            setTimeout(() => {
                loadDashboard();
            }, 1000);
        } else {
            showMessage('Error analyzing file', 'error');
        }
        
    } catch (error) {
        console.error('Error analyzing file:', error);
        showMessage('Error analyzing file. Make sure the backend server is running.', 'error');
    }
}


/**
 * Clear all alerts from the database
 */
async function clearAllAlerts() {
    // Confirm action
    if (!confirm('Are you sure you want to delete all alerts? This cannot be undone.')) {
        return;
    }
    
    try {
        showMessage('Clearing all alerts...', 'info');
        
        // Call API to clear alerts
        const response = await fetch(`${API_URL}/api/alerts`, {
            method: 'DELETE'
        });
        
        const data = await response.json();
        
        if (data.success) {
            showMessage('✓ All alerts cleared successfully', 'success');
            
            // Reload dashboard
            setTimeout(() => {
                loadDashboard();
            }, 1000);
        } else {
            showMessage('Error clearing alerts', 'error');
        }
        
    } catch (error) {
        console.error('Error clearing alerts:', error);
        showMessage('Error clearing alerts. Make sure the backend server is running.', 'error');
    }
}


/**
 * Show a message to the user
 */
function showMessage(message, type) {
    // Remove any existing messages
    const existingMessage = document.querySelector('.message');
    if (existingMessage) {
        existingMessage.remove();
    }
    
    // Create new message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `message message-${type}`;
    messageDiv.textContent = message;
    
    // Insert at the top of the container
    const container = document.querySelector('.container');
    container.insertBefore(messageDiv, container.firstChild);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}
