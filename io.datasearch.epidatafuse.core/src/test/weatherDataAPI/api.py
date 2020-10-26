from flask import Flask, request, jsonify
from datetime import datetime
import weatherScrapper 


app = Flask(__name__)

@app.route("/")
def hello_world():
   return ("Hello World")

@app.route("/weatherdata")
def hello_test():
   print("Executed!")
   res = {
       "StationName":"Cinnamon Lake Side Hotel",
       "Latitude":"6.929543",
       "Longitude":"79.8492668",
       "dtg":"20130526",
       "ObservedValue":"0.6"
   }
   return jsonify(res)

@app.route("/weatherstations")
def hello_weather():
   print("Executed!")
   res = {
       "StationName":"Cinnamon Lake Side Hotel",
       "Latitude":"6.929543",
       "Longitude":"79.8492668"
   }
   return jsonify(res)

@app.route("/weather")
def weather():
   dateString = request.args.get('date')
   date = datetime.strptime(dateString.strip(), '%Y/%m/%d').date()
   print(date.month, date.year)
   data = weatherScrapper.getPercipitation(date.day, date.month, date.year)
   return (str(data))

@app.route("/temp")
def temperature():
    res = {
           "sensorId":"01CB068A",
           "temperature":50.5
    }
    return jsonify(res)

@app.route("/sweet")
def sweet():
    res = {
        "name": "TestName",
        "temperature": 56.5
    }
    return jsonify(res)

if __name__ == '__main__':
   app.run()