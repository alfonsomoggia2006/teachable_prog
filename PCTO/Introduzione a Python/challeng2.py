def leggi_file(file_path):
    #Legge il file e restituisce le righe come una lista di tuple.
    with open(file_path, 'r') as file:
        return [tuple(riga.strip().split()) for riga in file]

def calcola_punteggio_scelta(giocatore):
    #Restituisce il punteggio associato alla scelta del giocatore.
    punteggi_scelta = {'X': 1, 'Y': 2, 'Z': 3}
    return punteggi_scelta.get(giocatore, 0)

def calcola_punteggio_risultato(avversario, giocatore):
    #Restituisce i punti ottenuti dal risultato della partita.
    risultati = {
        ('A', 'X'): (0, 1),
        ('A', 'Y'): (6, 2),
        ('A', 'Z'): (3, 3),
        ('B', 'X'): (0, 1),
        ('B', 'Y'): (3, 2),
        ('B', 'Z'): (6, 3),
        ('C', 'X'): (6, 1),
        ('C', 'Y'): (0, 2),
        ('C', 'Z'): (3, 3),
    }
    return risultati.get((avversario, giocatore), (0, 0))[0]

def calcola_punteggio(file_path):
    #Calcola il punteggio totale dalle righe del file.
    punteggio_totale = 0
    partite = leggi_file(file_path)

    for avversario, giocatore in partite:
        punteggio_totale += calcola_punteggio_scelta(giocatore)
        punteggio_totale += calcola_punteggio_risultato(avversario, giocatore)

    return punteggio_totale

# Percorso del file
file_path = 'input2.txt'  # Modifica con il percorso corretto se necessario
punteggio = calcola_punteggio(file_path)
print(f"Punteggio totale: {punteggio}")