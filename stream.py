import subprocess

def get_live_stream_url(youtube_url):
    result = subprocess.run(
        ["yt-dlp", "-g", youtube_url],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    # The first URL is typically the video stream
    return result.stdout.strip().split('\n')[0]

# Use the live stream URL
youtube_url = "https://www.youtube.com/watch?v=w2gG6XjN1qk"
stream_url = get_live_stream_url(youtube_url)
print("Stream URL:", stream_url)
