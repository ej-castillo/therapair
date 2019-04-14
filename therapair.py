from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///therapists.db'
theradb = SQLAlchemy(app)
theradb.create_all()

@app.route("/")
def Home():
    return render_template("template.html")

if __name__ == '__main__':
	app.run(debug = True)