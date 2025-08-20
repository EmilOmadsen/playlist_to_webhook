# Spotify Playlist Generator with Webhook Integration

A Flask web application that generates mixed playlists from Spotify search results and sends them to a webhook instead of creating them directly on Spotify.

## 🚀 Features

- **Spotify OAuth Authentication**: Secure login with Spotify accounts
- **Playlist Search & Ranking**: Advanced algorithms to find trending playlists by keyword
- **Webhook Integration**: Sends generated playlists to external webhook for processing
- **Modern UI**: Beautiful, responsive interface with Bootstrap
- **Local Development**: Easy setup for local testing

## 🔧 Recent Updates

### Webhook Integration (Latest)
- ✅ **NEW**: Send generated playlists to webhook instead of creating on Spotify
- ✅ **NEW**: Updated redirect URI for local testing (`http://127.0.0.1:3000/callback`)
- ✅ **Preserved**: All existing Spotify authentication and playlist ranking functionality
- ✅ **Enhanced**: Better user feedback for webhook delivery status

## 📋 Prerequisites

- Python 3.7+
- Spotify Developer Account
- Webhook endpoint (for receiving playlist data)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd webhook_gen
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Spotify App**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new app or use existing one
   - Add redirect URI: `http://127.0.0.1:3000/callback` (for local testing)
   - For production: Add `https://your-app-name.railway.app/callback`
   - Note your Client ID and Client Secret

4. **Configure environment variables**
   ```bash
   # Create .env file (optional - app uses hardcoded values for testing)
   echo "SPOTIFY_CLIENT_ID=your_client_id" > .env
   echo "SPOTIFY_CLIENT_SECRET=your_client_secret" >> .env
   echo "REDIRECT_URI=http://127.0.0.1:3000/callback" >> .env
   ```

## 🚀 Running the Application

### Local Development
```bash
python3 app.py
```

The application will run on `http://127.0.0.1:3000`

### With Custom Port
```bash
PORT=3001 python3 app.py
```

### Production Deployment (Railway)
1. **Deploy to Railway**: Follow the guide in `railway_deploy.md`
2. **Set Environment Variables**: Configure in Railway dashboard
3. **Update Spotify Redirect URI**: Add your Railway URL
4. **Access**: Your app will be available at `https://your-app-name.railway.app`

## 🧪 Testing

### Test Webhook Connection
```bash
python3 test_webhook.py
```

### Full Application Flow
1. Open `http://127.0.0.1:3000`
2. Login with Spotify
3. Search for playlists
4. Select playlists to mix
5. Click "Send to Webhook"
6. Check webhook delivery status

## 🔗 Webhook Integration

### Webhook URL
Generated playlists are sent to:
```
https://thelabelsunday.app.n8n.cloud/webhook/1e2d8f4b-2ae6-4503-b331-319e9cc9c1b0
```

### Payload Format
The webhook receives JSON data in this format:
```json
{
  "playlist_name": "Generated Playlist Name",
  "playlist_description": "Playlist description",
  "tracks": [
    {
      "id": "track_id",
      "name": "Track Name",
      "artist": "Artist Name",
      "album": "Album Name",
      "duration_ms": 180000,
      "popularity": 75,
      "uri": "spotify:track:track_id",
      "added_at": "2024-01-01T00:00:00Z"
    }
  ],
  "total_tracks": 20,
  "generated_at": "2024-01-01 12:00:00",
  "user_info": {
    "user_id": "spotify_user_id",
    "user_name": "User Display Name"
  }
}
```

## 📁 Project Structure

```
webhook_gen/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── test_webhook.py        # Webhook testing script
├── templates/             # HTML templates
│   ├── dashboard.html     # Dashboard page
│   ├── generator.html     # Playlist generator page
│   └── login.html         # Login page
├── docs/                  # Documentation
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables
- `SPOTIFY_CLIENT_ID`: Your Spotify app client ID
- `SPOTIFY_CLIENT_SECRET`: Your Spotify app client secret
- `REDIRECT_URI`: OAuth redirect URI (default: `http://127.0.0.1:3000/callback`)
- `PORT`: Application port (default: 3000)

### Spotify App Settings
Make sure your Spotify app has these redirect URIs configured:
- `http://127.0.0.1:3000/callback` (for local development)
- `https://your-production-domain.com/callback` (for production)

## 🎯 Key Features

### Before vs After
| Feature | Before | After |
|---------|--------|-------|
| Playlist Creation | Direct to Spotify | Send to Webhook |
| Button Text | "Generate" | "Send to Webhook" |
| Results | Spotify Links | Webhook Status |
| Authentication | ✅ Same | ✅ Same |
| Playlist Rankings | ✅ Same | ✅ Same |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues:
1. Check the console output for error messages
2. Verify your Spotify app settings
3. Test the webhook connection with `test_webhook.py`
4. Ensure all dependencies are installed

## 🔄 Version History

- **v2.0**: Webhook integration, updated UI, local testing support
- **v1.0**: Original Spotify playlist creation functionality
