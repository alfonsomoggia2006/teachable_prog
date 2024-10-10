import requests

# Inserisci qui la tua chiave API di GNEWS
apikey = "inserisci qua la tua chiave"
base_url = "https://gnews.io/api/v4/top-headlines"

# Parametri della richiesta
category = "sports"  # Categoria di notizie
country = "it"  # Codice del paese (es. "it" per Italia)
lang = "it"  # Lingua (es. "it" per italiano)
maximum = "2"  # Numero massimo di articoli da ottenere

# Creazione dell'URL di richiesta
url = f"{base_url}?category={category}&lang={lang}&country={country}&max={maximum}&apikey={apikey}"

# Esecuzione della richiesta GET
response = requests.get(url)

# Controllo dello stato della risposta
if response.status_code == 200:
    articles = response.json()["articles"]

    # Stampa degli articoli
    for article in articles:
        print(article["title"])
        print(article["url"])
        print()  # Riga vuota per separare gli articoli
else:
    print('Errore nella richiesta:', response.status_code)

