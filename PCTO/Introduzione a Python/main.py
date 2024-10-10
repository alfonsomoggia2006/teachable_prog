def calcola_punteggio(file_path):
    punteggio_totale = 0

    # Definire i punteggi per le scelte
    punteggi_scelta = {'X': 1, 'Y': 2, 'Z': 3}  # le tue scelte
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

    # Leggi il file e calcola il punteggio
    with open(file_path, 'r') as file:
        for riga in file:
            avversario, giocatore = riga.strip().split()
            punti_scelta = punteggi_scelta[giocatore]
            punti_risultato, _ = risultati[(avversario, giocatore)]
            punteggio_totale += punti_scelta + punti_risultato

    return punteggio_totale


file_path = 'input2.txt'  # Modifica con il percorso corretto se necessario
punteggio = calcola_punteggio(file_path)
print(f"Punteggio totale: {punteggio}")



