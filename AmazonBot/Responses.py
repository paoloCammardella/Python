from datetime import datetime
import scraper as scrap

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "ciao", "ue"):
        return scrap.check_price('https://www.amazon.it/Scheda-grafica-ZOTAC-GAMING-GEFORCE/dp/B08P7ZKQPP/ref=sr_1_4?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=3070&qid=1620997513&sr=8-4')
    
    if user_message in ("cosa puoi fare", "comandi", "come funziona?"):
        return "Posso:\n-Dirti l'orario\n-rispondere ad un tuo saluto\n-dirti cosa posso fare\n- puoi provare i seguenti comandi\n /start\n/help" 

    if user_message in ("time", "orario", "ora"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M")

        return str(date_time)
    
    return "Non ho capito, puoi ripetere?"