from sys import argv, exit
from LEGENDX import bot
from LEGENDX import TOKEN
import LEGENDX.events

try:
    bot.start(bot_token=TOKEN)
except Exception:
    print("Network Error !")
    exit(1)

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
