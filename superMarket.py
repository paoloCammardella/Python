import time

def stampaInventario(inventario):
    for i in inventario:
        print(i)

#--------------------------------------------------------------------

def stampaCarrello(carrello):
    for i in carrello:
        print(i)

#--------------------------------------------------------------------

def inserimentoCarrello(inventario, carrello):
     carrello.insert(len(carrello), selezionaOggetto(inventario, carrello))

#--------------------------------------------------------------------

def selezionaOggetto(inventario, carrello):
    stampaInventario(inventario)
    print("")
    selezione = input("Cosa desidera?\n")
    
    return selezione

def caricamento():
    time.sleep(1)
    print('\\|')
    time.sleep(1)
    print("\\/")
    time.sleep(1)

#---------------------------Main--------------------------------
    carrello = []
    inventario = {
            "pane",
            "carote",
            "patate",
            "monster",
            "acqua",
            "kinder paradiso",
            "vino",
            "broccoli",
            "the",
            "maiale"
        }
    inserimentoCarrello(inventario, carrello)
    print(len(carrello))
    stampaCarrello(carrello) 
    
