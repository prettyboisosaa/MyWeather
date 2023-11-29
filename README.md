# WeatherApp

Questa è un'applicazione meteo che utilizza l'API da WeatherApi.com per recuperare dati in formato JSON e organizzarli in una tabella creata con getbootstrap e altre tecnologie.

L'app è fondamentalmente divisa in 2 parti:

* Presentazione (CSS + HTML)
* Recupero delle informazioni (Python + Flask)

[WeatherApi](https://www.weatherapi.com/docs/) fornisce dati in due tipi: .xml e .json. In questo progetto ho utilizzato .json.

# Code

1. Per la parte di codifica, il recupero viene effettuato utilizzando l'URL fornito da WeatherApi. È necessario effettuare l'accesso per ottenere la chiave API; senza di essa, non è possibile recuperare i dati. Nel mio codice, per implementare questa funzione, ho usato questo pezzo di codice. I parametri per la query vanno in questo dizionario:

```python
url = f"http://api.weatherapi.com/v1/current.json"
        params = {
            'key' : api_key,
            'q' : city
        }
```


2. Per effettuare effettivamente la query e il comando HTTP GET, è necessario utilizzare la libreria requests di Python:

```python
response = requests.get(url, params=params)
data = response.json()

```

3. una volta che i dati vengono restituiti l'elaborazione e la presentazione sarà fatta dal template Jinja2, lascio sotto un esempio che ho utilizzato per il metodo /astro


``` html
{% if data %}
    <table>
      <tr>
        <th>Name</th>
        <th>Region</th>
        <th>Country</th>
        <th>localtime</th>
        <th>sunrise</th>
        <th>sunset</th>
        <th>moonrise</th>
        <th>moonset</th>
        <th>moon_phase</th>
      </tr>
      <tr>
          <td>{{ data['location']['name'] }}</td>
          <td>{{ data['location']['region']}}</td>
          <td>{{ data['location']['country']}}</td>
          <td>{{ data['location']['localtime'] }}</td>
          <td>{{ data['astronomy']['astro']['sunrise'] }}</td>
          <td>{{ data['astronomy']['astro']['sunset'] }}%</td>
          <td>{{ data['astronomy']['astro']['moonrise'] }}</td>
          <td>{{ data['astronomy']['astro']['moonset'] }}</td>
          <td>{{ data['astronomy']['astro']['moon_phase'] }}</td>
        
      </tr>
  </table>
    {% endif %}
```

 # How to use

 nella pagina home abbiamo 3 pulsanti che indicano 3 funzioni diverse che sono 2 filtri e un riferimento alla repository github del progetto

 * Meteo
 * Astro
 * Source


 ## /meteo

 bisogna inserire nella barra di richerca una città e restituira il meteo al momento in cui è stato misurato, e verrà specificato, i dati si aggiornano ogni tot ore(limite che non supera 2 ore), tra i vari attributi abbiamo la regione l'ora corrente, il meteo, un icona che indica il meteo.

 ## /astro

 bisogna inserire una città e alla data corrente ritornera i dati 'astrologici' che semplicemente si riferisce a quando sorge il sole, una previsione di quando tramonterà quando è salita la luna, e quando è scesa, oltre che la fase lunare corrente

 ## /source

 non è una funzione ma ben si un riferimento alla mia repository pubblica di github con dentro il progetto alla versione corrente  