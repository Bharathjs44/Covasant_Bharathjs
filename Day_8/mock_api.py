# Question-11:
# Weather mock API 
# format comes from below endpoint 
    # Parse format, if xml, show xml, 
    # if none, show json 
    # Put all random temp 
    # City name may change based on PATH param 
    # (currently not implemented in demo api endpoint)
    


from flask import Flask, request,jsonify, Response
import random

app = Flask(__name__)

temperature = list(range(15,36))
wind_speed = list(range(1,20))
condition = ["foggy", "cloudy","Dry","Humid","Hot", "pleasant","rainy","sunny"]


cities = ["mumbai","Delhi","chennai","kolkata","Bengaluru","Hyderabad",
          "thiruvananthapuram", "nagpur","bhopal", "guwahati", "vadodara",
          "Guwahati","surat","vijayawada","jaipur","lucknow", "indore",
          "pune","patna","kerala"]

def create_weather():
    return {
    "city": random.choice(cities),
    "temperature":random.choice(temperature),
    "condition":random.choice(condition),
    "wind_speed":random.choice(wind_speed),
    "rain_probability": random.randint(0,100)
    }
    
weather_data = [create_weather() for _ in range(20)]

def find_weather(city_name):
    for city in weather_data:
        if city["city"].lower() == city_name.lower():
            return city
    return None

@app.route("/weather/<string:city_name>", methods=["GET"])
def get_weather(city_name):
    format_type = request.args.get("format","json").lower()
    weather = find_weather(city_name)
    
    if not weather:
        return Response("City not found", status=404)
        
    if format_type == "xml":
        xml_output = f"""<?xml version="1.0" encoding="UTF-8"?>
    <data>
        <city>{weather['city']}</city>
        <temperature>{weather['temperature']}</temperature>
        <condition>{weather['condition']}</condition>
        <wind_speed>{weather['wind_speed']}</wind_speed>
        <rain_probability>{weather['rain_probability']}</rain_probability>
    </data> """
        return Response(xml_output, mimetype="application/xml")
    
    return jsonify(weather)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
#Output Urls:
    #http://localhost:5000/weather/hyderabad
    #http://localhost:5000/weather/hyderabad?format=xml