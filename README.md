# Dota Patch Notifier

A small Python script that fetches the latest Dota 2 patch notes from Steam’s API and posts them to a Discord channel via webhook.

## Setup

1. Install Python 3 and `pip`.
2. `pip install requests discord.py`
3. Edit `dota_patch_bot.py`, pasting your Discord webhook URL.
4. Create an empty `last_gid.txt` in the same folder.

## Usage

```powershell
python .\dota_patch_bot.py

## Scheduling

- **Program:** `powershell.exe`  
- **Arguments:** `-NoProfile -WindowStyle Hidden -Command "cd 'C:\Users\YourName\dota_patch_bot'; python .\dota_patch_bot.py"`  
- **Trigger:** repeat every 1 hour (Indefinitely)