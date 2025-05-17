Dota Patch Notifier
Fetches the latest Dota 2 patch notes from the Steam API and posts them to a Discord channel via webhook.

Setup
Install Python 3 and pip

Install dependencies:
pip install requests discord.py

Ensure the script reads the webhook URL from the DISCORD_WEBHOOK_URL environment variable (no hard-coded URLs)

Create an empty file named last_gid.txt in this folder

Scheduling (Windows Task Scheduler)
Set your webhook URL as a user environment variable:
setx DISCORD_WEBHOOK_URL "https://discord.com/api/webhooks/<NEW_ID>/<NEW_TOKEN>"
Restart PowerShell to load it

In Task Scheduler, create or edit a task with:
• Program/script: C:\Users<You>\AppData\Local\Programs\Python\Python39\pythonw.exe
• Arguments: C:\Users<You>\dota_patch_bot\dota_patch_bot.py
• Start in: C:\Users<You>\dota_patch_bot
• Trigger: Daily, repeat every 1 hour indefinitely

Run the task once to confirm it posts silently to Discord

Note: Using pythonw.exe prevents any console window from appearing.