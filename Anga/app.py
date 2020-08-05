from flask import Flask, redirect, url_for, render_template,request,flash
import json,requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"
api_key = "da2b913513d21c808ccb02adf676f12b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'Nairobi,KE'
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    result = requests.get(complete_url)
    x = result.json()
    weather={
        'city':city,
        'temp':x['main']['temp'],
        'description':x['weather'][0]['description'],
        'icon':x['weather'][0]['icon'],
        'pressure':x['main']['pressure'],
        'humidity':x['main']['humidity'],
        'visibility': x['visibility'],
        }
    return render_template("index.html",weather=weather)
    
    

if __name__ == "__main__":
    app.run(debug=True)
