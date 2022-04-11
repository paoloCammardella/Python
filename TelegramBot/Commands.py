import Constants as keys
import Scraper as scrap

def startCommand(update, context):
    update.message.reply_text('Scrivi qualcosa per iniziare')
    scrap.check_price('https://www.amazon.it/Scheda-grafica-ZOTAC-GAMING-GEFORCE/dp/B08P7ZKQPP/ref=sr_1_4?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=3070&qid=1620997513&sr=8-4', update)

def helpCommand(update, context):
    update.message.reply_text('Se hai bisogno di aiuto chiedi a ' + keys.author)

def commandsCommand(update, context):
    update.message.reply_text("questi sono i comandi che hai a disposizione.\n /help: fornisce aiuto\n/commands: fornisce la lista dei comandi")