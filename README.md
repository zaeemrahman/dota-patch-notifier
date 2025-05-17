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

## Scheduling (using python to run program with no terminal window popping up)

- Create new task in Task Scheduler

- **Program:**  
  `C:\Users\YourName\AppData\Local\Programs\Python\Python312\pythonw.exe`

- **Arguments:**  
  `C:\Users\YourName\dota_patch_bot\dota_patch_bot.py`

- **Start in:**  
  `C:\Users\YourName\dota_patch_bot`

- **Trigger:**  
  Repeat every **1 hour** (Indefinitely)