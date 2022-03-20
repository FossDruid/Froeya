import requests
import configparser
from flask import Flask, render_template, request, session, redirect
import requests, configparser
#import configparser
import pandas as pd
import numpy as np
from pandas import DataFrame, read_csv
from dataDriver import *

app = Flask(__name__)

#df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
#                   'B': [5, 6, 7, 8, 9],
#                   'C': ['a', 'b', 'c--', 'd', 'e']})

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/pdTest', methods=['POST', 'GET'])
def html_table():
    rows = []
    csvDataFile = "testData/peopleJobPay.csv"
    csvData = dataReadFile(rows, csvDataFile)
    df = pd.DataFrame(csvData)
    print(csvData.row)

    #def dataFrameMaker()

    return render_template('pdTest.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']
    country_code = request.form['countryCode']
    
    api_key = get_api_key()
    data = get_weather_results(zip_code,country_code, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('results.html', location=location, temp=temp, feels_like=feels_like, weather=weather)

def get_api_key():
    config = configparser.ConfigParser()
    config.read('src/config.ini')
    return config['openweathermap']['api']

def get_weather_results(zip_code, country_code, api_key):
    api_url = "http://api.openweathermap.org/" \
    "data/2.5/weather?zip={},{}&units=metric&appid={}".format(zip_code, country_code, api_key)
    r = requests.get(api_url)
    print(api_url)
    return r.json()

# Test
#print (get_weather_results("1570", "NO", get_api_key()))

if __name__ == '__main__':
    app.run()