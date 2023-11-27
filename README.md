# WeatherApp

this is a Weather app that uses api from WeatherApi.com to retrive datas in a json format and order them in a table created with getbootstrap and other tecnologies

the app is basically divided into 2 parts:

* Presentation (css + html)
* Retrival of information (Python + flask)

[WeatherApi](https://www.weatherapi.com/docs/) website gives data in 2 types you can have .xml and .json, in this project i used .json

# Code

1. for the coding part the retrival is done by using the url that WeatherApi gives you, you must sing in to get the API key without it you can't retrive data, in my code to implement this function i used this piece of code, also the parameters for the query goes in this dict


```
url = f"http://api.weatherapi.com/v1/current.json"
        params = {
            'key' : api_key,
            'q' : city
        }
```

2. to make the actual query and http GET command you must use the python's request library

```
    response = requests.get(url, params=params)
    data = response.json()

```

