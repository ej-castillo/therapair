from flask import Flask, render_template, request
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
	user_zip = request.form.get('zip')
	return render_template("map.html", zip=user_zip)

if __name__ == '__main__':
	app.run(debug = True)