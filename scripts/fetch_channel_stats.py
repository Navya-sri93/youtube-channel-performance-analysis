from googleapiclient.discovery import build

# -----------------------------
# CONFIGURATION
# -----------------------------

API_KEY = "YOUR_API_KEY_HERE"   # <-- replace locally, NOT on GitHub
CHANNEL_ID = "UCJihyK0A38SZ6SdJirEdIOw"

# -----------------------------
# BUILD YOUTUBE SERVICE
# -----------------------------

youtube = build(
    serviceName="youtube",
    version="v3",
    developerKey=API_KEY
)

# -----------------------------
# FETCH CHANNEL STATISTICS
# -----------------------------

request = youtube.channels().list(
    part="statistics",
    id=CHANNEL_ID
)

response = request.execute()

# -----------------------------
# EXTRACT & DISPLAY DATA
# -----------------------------

stats = response["items"][0]["statistics"]

print("Channel Statistics")
print("------------------")
print("Total Views      :", stats["viewCount"])
print("Subscribers      :", stats["subscriberCount"])
print("Total Videos     :", stats["videoCount"])
