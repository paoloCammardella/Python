from telegram.ext import *
import Constants as keys
import Responses as R
import Commands as comm
import Handles as hand


print("Bot started..")

def main():
  
    updater = Updater(keys.APYKey, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", comm.startCommand))
    dp.add_handler(CommandHandler("help", comm.helpCommand))
    dp.add_handler(CommandHandler("commands", comm.commandsCommand))

    dp.add_handler(MessageHandler(Filters.text, hand.handleMessage))
    dp.add_error_handler(hand.error)

    updater.start_polling()
    updater.idle()


main()