from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "ciao", "ue"):
        return "Ciao bello come va?"
    
    if user_message in ("cosa puoi fare", "comandi", "come funziona?"):
        return "Posso:\n-Dirti l'orario\n-rispondere ad un tuo saluto\n-dirti cosa posso fare\n- puoi provare i seguenti comandi\n /start\n/help" 

    if user_message in ("time", "orario", "ora"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M")

        return str(date_time)
    
    return "Non ho capito, puoi ripetere?"