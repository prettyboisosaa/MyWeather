from flask import Flask, render_template, request
import requests

#https://www.weatherapi.com/docs/

app = Flask(__name__)

api_key = 'f6c164a0f6744f94982171505232311'

@app.route('/')
def main():
    return render_template("index.jinja")

@app.route('/submit', methods=['POST'])
def submit():
    city = request.form['message']
    url = f"http://api.weatherapi.com/v1/current.json"
    params = {
        'key' : api_key,
        'q' : city
    }

    response = requests.get(url, params=params)
    data = response.json()

    return render_template("index.jinja", data=data)

if __name__ == '__main__':
    app.run()
