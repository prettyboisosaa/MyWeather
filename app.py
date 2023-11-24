from flask import Flask, render_template, request
import requests
from datetime import datetime

#https://www.weatherapi.com/docs/

app = Flask(__name__)

api_key = 'f6c164a0f6744f94982171505232311'


@app.route('/')
def main():
    return render_template("index.jinja")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    data = None
    if request.method == 'POST':
        city = request.form['message']
        url = f"http://api.weatherapi.com/v1/current.json"
        params = {
            'key' : api_key,
            'q' : city
        }

        response = requests.get(url, params=params)
        data = response.json()

    return render_template("meteo.jinja", data=data)

@app.route('/astro', methods=['GET', 'POST'])
def astro():
    data = None
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    if request.method == 'POST':
        city = request.form['message']
        url = f"http://api.weatherapi.com/v1/astronomy.json"
        params = {
            'key' : api_key,
            'q' : city,
            'dt' : formatted_date
        }

        response = requests.get(url, params=params)
        data = response.json()

    return render_template("astro.jinja", data=data)



if __name__ == '__main__':
    app.run()
