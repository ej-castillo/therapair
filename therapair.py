from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///therapists.db'
therapistsdb = SQLAlchemy(app)

@app.route("/")
def Home():
    return render_template("template.html")

if __name__ == '__main__':
	app.run(debug = True)