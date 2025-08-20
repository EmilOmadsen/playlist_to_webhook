#!/usr/bin/env python3
"""
Test script for webhook functionality
"""

import requests
import json
import time

def test_webhook():
    """Test sending data to the webhook"""
    webhook_url = "https://thelabelsunday.app.n8n.cloud/webhook/1e2d8f4b-2ae6-4503-b331-319e9cc9c1b0"
    
    # Sample playlist data
    test_payload = {
        'playlist_name': 'Test Playlist',
        'playlist_description': 'This is a test playlist sent from the webhook generator',
        'tracks': [
            {
                'id': 'test_track_1',
                'name': 'Test Track 1',
                'artist': 'Test Artist 1',
                'album': 'Test Album 1',
                'duration_ms': 180000,
                'popularity': 75,
                'uri': 'spotify:track:test_track_1',
                'added_at': '2024-01-01T00:00:00Z'
            },
            {
                'id': 'test_track_2',
                'name': 'Test Track 2',
                'artist': 'Test Artist 2',
                'album': 'Test Album 2',
                'duration_ms': 200000,
                'popularity': 80,
                'uri': 'spotify:track:test_track_2',
                'added_at': '2024-01-01T00:00:00Z'
            }
        ],
        'total_tracks': 2,
        'generated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'user_info': {
            'user_id': 'test_user_123',
            'user_name': 'Test User'
        }
    }
    
    try:
        print(f"Testing webhook at: {webhook_url}")
        print(f"Sending payload: {json.dumps(test_payload, indent=2)}")
        
        response = requests.post(webhook_url, json=test_payload, timeout=30)
        
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
        if response.text:
            print(f"Response body: {response.text}")
        
        if response.status_code == 200:
            print("✅ Webhook test successful!")
            return True
        else:
            print(f"❌ Webhook test failed with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Webhook test error: {e}")
        return False

if __name__ == "__main__":
    test_webhook()
