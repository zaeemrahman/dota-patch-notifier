import os, requests
from discord import SyncWebhook

# ↓ paste your webhook URL between the quotes ↓
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
GID_FILE    = "last_gid.txt"
API_URL     = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/"

webhook = SyncWebhook.from_url(WEBHOOK_URL)

def fetch_latest():
    params = {"appid":570,"count":1,"maxlength":0,"format":"json"}
    data   = requests.get(API_URL, params=params).json()
    item   = data["appnews"]["newsitems"][0]
    return item["gid"], item["title"], item["url"]

def get_last_gid():
    try:
        return open(GID_FILE).read().strip()
    except FileNotFoundError:
        return None

def save_gid(gid):
    with open(GID_FILE, "w") as f:
        f.write(str(gid))

def main():
    last = get_last_gid()
    gid, title, url = fetch_latest()
    if gid != last:
        webhook.send(f"**New Dota 2 Patch Notes:** {title}\n{url}")
        save_gid(gid)

if __name__ == "__main__":
    main()