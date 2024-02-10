from tgpt2 import TGPT
bot = TGPT()

while True:
    print(bot.chat(input(">>")))