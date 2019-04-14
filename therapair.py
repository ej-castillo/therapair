from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/therapists")
def Therapists():
	return render_template("therapists.html")

@app.route("/map")
def Map():
	return render_template("map.html")

if __name__ == '__main__':
	app.run(debug = True)