# BitcoinTelegramBot
Periodically post Bitcoin price updates to a group.

NOTE: This bot is in active development. Installation instructions may not work from time to time.

# How to use

## Step 1
Set up secrets
- Send the `/newbot` command to [BotFather](https://t.me/BotFather) through Telegram and follow the instructions to set up your bot however you want.
- Copy the HTTP API token into the `launch.bash` file, replacing `<YOUR BOT TOKEN HERE>`.
- Get the [group chat ID](http://stackoverflow.com/a/32572159) or [user ID](https://stackoverflow.com/questions/31078710/how-to-obtain-telegram-chat-id-for-a-specific-user)
- Copy this ID into the `<YOUR CHAT ID HERE>` field of `launch.bash`. The ID might contain a minus (`-`) sign, that's OK, don't remove it.

## Step 2
Install dependencies
- If necessary, [install pip](https://pip.pypa.io/en/stable/installing/).
- Run `pip3 install python-telegram-bot --upgrade --user` from a commandline or [follow the official documentation](https://github.com/python-telegram-bot/python-telegram-bot)

## Step 3
Test the bot
- Run `bash launch.bash` in a terminal. If everything is correctly set up, your bot should have delivered the message to the chat ID you've set up.

## Step 4 (optional)
Set up automatic updates
- On a Unix system, you can use `crontab` to run the script at regular intervals and deliver updated prices. You can consult [this file](http://man7.org/linux/man-pages/man5/crontab.5.html) for examples on setting up a crontab file.