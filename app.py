from flask import Flask, render_template, request
from weather import main as weather_result
# basically the same main function is called by using weather_result()

app = Flask(__name__)

@app.route( "/", methods = ["GET", "POST"])
def index():
    data = None 
    error = "" 
    # must add this line^ or else data will not exist / pg dont load
    try:
        if request.method == "POST":
            city = request.form["cityName"]
            data = weather_result(city)
    except:
        return f"Enter a valid city name!"
    
    else: 
        pass
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

