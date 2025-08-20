# 🚂 Deploy to Railway - Complete Guide

## Why Railway?
- ✅ **Free tier** with 500 hours/month
- ✅ **Always-on** deployment
- ✅ **Easy setup** - just connect GitHub
- ✅ **Automatic HTTPS**
- ✅ **Environment variables** support

## Step-by-Step Deployment

### 1. Prepare Your Project
Your project is already ready! You have:
- ✅ `app.py` (Flask app)
- ✅ `requirements.txt` (dependencies)
- ✅ `Procfile` (tells Railway how to run)

### 2. Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project"

### 3. Deploy Your App
1. Choose "Deploy from GitHub repo"
2. Select your repository: `EmilOmadsen/yessir`
3. Railway will automatically detect it's a Python app

### 4. Set Environment Variables
In Railway dashboard, add these variables:
```
SPOTIFY_CLIENT_ID=d7a59142072e4223a5e94195be60a1d5
SPOTIFY_CLIENT_SECRET=ef91d4916f9249f985d4bbd545473541
PORT=8080
PUBLIC=true
SECRET_KEY=your-secret-key-change-this
```

### 5. Update Spotify Redirect URI
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Find your app
3. Add this redirect URI:
   ```
   https://your-app-name.railway.app/callback
   ```
   (Replace `your-app-name` with your actual Railway app name)

### 6. Deploy!
- Railway will automatically build and deploy
- You'll get a URL like: `https://your-app-name.railway.app`

## 🎉 Result
- Your app runs **24/7**
- **Always accessible** via the Railway URL
- **Automatic HTTPS**
- **No more Codespaces needed**

## Troubleshooting
- If you get build errors, check the Railway logs
- Make sure all environment variables are set
- Verify your Spotify redirect URI matches exactly

## Next Steps
1. Deploy to Railway
2. Test your app
3. Share the Railway URL with others!
