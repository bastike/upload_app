# Upload App

## 🚀 Deploy Your Flask App to Render (Free Tier)
✅ What You’ll Get
- A public URL like: https://jeniz-upload.onrender.com
- No login or warning page for users
- Always-on hosting (free tier includes 750 hours/month)

## 🧰 Step-by-Step Guide
1. Prepare Your Project Folder
Your folder should contain:
upload-app/
├── app.py
├── requirements.txt
├── uploads/         ← (optional, or create at runtime)


## 2. Create requirements.txt
This tells Render which Python packages to install:
flask
werkzeug


You can generate it with:
pip freeze > requirements.txt


## 3. Create render.yaml (optional but recommended)
This configures your service:
services:
  - type: web
    name: jeniz-upload
    env: python
    buildCommand: ""
    startCommand: python app.py
    plan: free


## 4. Push to GitHub
If you haven’t already:
git init
git add .
git commit -m "Initial upload app"
git remote add origin https://github.com/YOUR_USERNAME/jeniz-upload.git
git push -u origin main


## 5. Go to Render.com
- Sign up (free)
- Click “New +” → Web Service
- Connect your GitHub repo
- Set:
- Build Command: (leave blank)
- Start Command: python app.py
- Environment: Python 3.x
- Click Deploy

## ✅ After Deployment
==> Your service is live 🎉
==> 
==> ///////////////////////////////////////////////////////////
==> 
==> Available at your primary URL https://upload-app-9pm2.onrender.com
==> 
==> ///////////////////////////////////////////////////////////
127.0.0.1 - - [04/Nov/2025 14:57:48] "GET / HTTP/1.1" 200 -

You can now:
- Share it via QR code
- Embed it in your WooCommerce site
- Use it at events for customer uploads



