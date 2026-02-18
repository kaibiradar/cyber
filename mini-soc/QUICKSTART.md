# 🚀 Quick Start Guide - Mini SOC

**Get up and running in 5 minutes!**

## Prerequisites

- Python 3.8+ installed
- Web browser

## Step 1: Install Dependencies

```bash
cd d:\cyber\mini-soc
pip install -r requirements.txt
```

## Step 2: Start Backend Server

```bash
cd backend
python main.py
```

✅ You should see: `API will be available at: http://127.0.0.1:8000`

⚠️ **Keep this terminal window open!**

## Step 3: Open Dashboard

1. Navigate to `d:\cyber\mini-soc\frontend\`
2. Double-click `index.html`
3. Opens in your browser automatically

## Step 4: Test It!

In the dashboard:
1. Find dropdown: **"Or Analyze Existing Log"**
2. Select: **sample_log.txt**
3. Click: **"Analyze"** button
4. Wait 2-3 seconds

🎉 **Success!** You should see alerts appear!

## Troubleshooting

**"Module not found" error?**
```bash
pip install fastapi uvicorn python-multipart pydantic
```

**"Can't connect to API"?**
- Check if backend is running
- Visit: http://127.0.0.1:8000 (should show JSON response)

**No alerts showing?**
- Verify you clicked "Analyze" button
- Check browser console (F12) for errors

## What's Next?

- Read the full [README.md](README.md) for detailed documentation
- Try uploading your own log files
- Explore the API at: http://127.0.0.1:8000/docs
- Customize the detection rules

**Happy monitoring! 🛡️**
