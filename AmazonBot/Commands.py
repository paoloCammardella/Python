import Constants as keys
import scraper as scrap

def startCommand(update, context):
    update.message.reply_text('Scrivi qualcosa per iniziare')

def helpCommand(update, context):
    update.message.reply_text('Se hai bisogno di aiuto chiedi a ' + keys.author)

def commandsCommand(update, context):
    update.message.reply_text("questi sono i comandi che hai a disposizione.\n /help: fornisce aiuto\n/commands: fornisce la lista dei comandi")