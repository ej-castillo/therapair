from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/therapists")
def therapists():
	return render_template("therapists.html")

@app.route("/map")
def map():
	user_zip = request.form.get("zip")
	return render_template("map.html", zip=user_zip)

if __name__ == "__main__":
	app.run(debug=True)
