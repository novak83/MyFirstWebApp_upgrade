from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def index():
    weather_info = "Danes je zelo lep dan"
    current_year = datetime.datetime.now().year

    cities = ["Ljubljana", "Celje", "Maribor", "Ptuj", "Koper"]
    return render_template("index.html", weather_info = weather_info, current_year = current_year, cities = cities)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)