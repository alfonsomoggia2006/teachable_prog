def leggi_file(file_path):
    #Legge il file e restituisce il contenuto suddiviso per macchinette.
    with open(file_path, 'r') as file:
        contenuto = file.read().strip().split('\n\n')  # Divido per righe vuote
    return contenuto

def calcola_calorie(macchinetta):
    #Calcola il totale delle calorie per una macchinetta.
    return sum(int(caloria) for caloria in macchinetta.split() if caloria.isdigit())

def calcola_macchinette(file_path):
    #Calcola le calorie totali per ciascuna macchinetta.
    contenuto = leggi_file(file_path)
    calorie_totali = [calcola_calorie(macchinetta) for macchinetta in contenuto]
    return calorie_totali

def macchinette_caloriche(calorie_totali):
    #Trova le tre macchinette più caloriche e restituisce la somma delle loro calorie e i loro indici.
    indici = sorted(range(len(calorie_totali)), key=lambda i: calorie_totali[i], reverse=True)[:3]
    somma_top_3 = sum(calorie_totali[i] for i in indici)
    return somma_top_3, indici

def stampa_risultati(somma_top_3, indici_top_3, calorie_totali):
    #Stampa i risultati delle macchinette più caloriche.
    print("Indici delle 3 macchinette più caloriche e le loro calorie:")
    print(f"La somma delle calorie delle 3 macchinette più caloriche è: {somma_top_3}")

    for indice in indici_top_3:
        print(f"Macchinetta {indice + 1}: {calorie_totali[indice]} calorie")

# Percorso del file
file_path = 'input1.txt'
calorie_totali = calcola_macchinette(file_path)
somma_top_3, indici_top_3 = macchinette_caloriche(calorie_totali)

# Stampa dei risultati
stampa_risultati(somma_top_3, indici_top_3, calorie_totali)













