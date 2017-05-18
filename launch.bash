#!/bin/bash

# Telegram Bot token
export telegramToken="<YOUR BOT TOKEN HERE>"
# Telegram chat ID
export telegramChatId="<YOUR CHAT ID HERE>"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

/usr/local/bin/python3 python/bitcoin.py
