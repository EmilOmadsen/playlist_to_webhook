# Webhook Integration Update

## Overview
The Spotify Playlist Generator has been updated to send generated playlists to a webhook instead of creating them directly on Spotify.

## Changes Made

### 1. Updated Redirect URI
- Changed from: `https://web-production-747b3.up.railway.app/callback`
- Changed to: `http://127.0.0.1:3000/callback` (for local testing)

### 2. New Webhook Integration
- Added `send_playlist_to_webhook()` method to `SpotifyPlaylistGenerator` class
- Webhook URL: `https://thelabelsunday.app.n8n.cloud/webhook/1e2d8f4b-2ae6-4503-b331-319e9cc9c1b0`
- Modified `generate_playlists()` function to use webhook instead of Spotify API

### 3. Updated Frontend
- Changed button text from "Generate" to "Send to Webhook"
- Updated result display to show webhook status instead of Spotify links
- Modified success messages to reflect webhook sending

### 4. Webhook Payload Format
The webhook receives the following JSON structure:
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

## Testing

### Local Testing
1. Set your redirect URI to: `http://127.0.0.1:3000/callback`
2. Run the application: `python app.py`
3. Test webhook functionality: `python test_webhook.py`

### Webhook Test
The `test_webhook.py` script can be used to test the webhook connection independently:
```bash
python test_webhook.py
```

## Functionality Preserved
- ✅ Spotify login and authentication
- ✅ Playlist search and ranking algorithms
- ✅ Playlist selection and mixing
- ✅ User interface and experience
- ✅ All existing features except direct Spotify playlist creation

## New Behavior
- Instead of creating playlists on Spotify, the app now sends playlist data to the specified webhook
- Users still authenticate with Spotify to access their account and search playlists
- The webhook receives complete playlist data including track details and user information
- Frontend shows webhook delivery status instead of Spotify playlist links

## Environment Variables
Make sure these are set for local testing:
- `SPOTIFY_CLIENT_ID`: Your Spotify app client ID
- `SPOTIFY_CLIENT_SECRET`: Your Spotify app client secret
- `REDIRECT_URI`: `http://127.0.0.1:3000/callback` (for local testing)
