from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("[index()] - call successful")
    
    data = None
    if request.method == 'POST':
        print("[index()]: ", request.method)
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']

        data = get_weather(city, state, country)
    return render_template('index.html', data=data)

if __name__ == "__main__":
    print("app.py - call successful")
    app.run(port=1440, debug=True)