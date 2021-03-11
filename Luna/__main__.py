from sys import argv, exit
from Luna import tbot
from Luna import TOKEN

# IDK WHY IT'S SO IMPORTANT, JUST DON'T REMOVE THIS
import Luna.events

try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Network Error !")
    exit(1)

if len(argv) not in (1, 3, 4):
    tbot.disconnect()
else:
    tbot.run_until_disconnected()
