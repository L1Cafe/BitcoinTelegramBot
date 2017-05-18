import requests     #API
import re           # regex
import os           # environment variables for secrets
from telegram import Bot as telegramBot
from telegram import ParseMode as telegramParseMode

# Settings saved in environmental variables for security
telegramToken = os.environ["telegramToken"] #Bot token
telegramChatId = os.environ["telegramChatId"]

bitcoinApiEndpoint = "http://api.coindesk.com/v1/bpi/currentprice.json"

# Bitcoin get prices
request = requests.get(bitcoinApiEndpoint)
regex = "([\d\.\ ]*,[\d][\d])"
bitcoinCurrentPriceUsd = re.search(regex, request.json()["bpi"]["USD"]["rate"].replace(",", "").replace(".", ",")).group(0)
bitcoinCurrentPriceEur = re.search(regex, request.json()["bpi"]["EUR"]["rate"].replace(",", "").replace(".", ",")).group(0)

# Telegram
telegramText = "Currently, 1 #Bitcoin #XBT equals:" + "\n" + "`" + bitcoinCurrentPriceEur + " #EUR" + "`" + "\n" + "`" + bitcoinCurrentPriceUsd + " #USD" + "`" + "\n" + "#ExchangeRates"

telegramBitcoin = telegramBot(token=telegramToken)
telegramBitcoin.send_message(chat_id=telegramChatId, text=telegramText, parse_mode=telegramParseMode.MARKDOWN, disable_web_page_preview=True)

