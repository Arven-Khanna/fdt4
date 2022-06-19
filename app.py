from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://imperial:imperial-fdt-online-2019-colossal-shelf@imperial-2021.ckp3dl3vzxoh.eu-west-2.rds.amazonaws.com:5432/dvdrental'
db = SQLAlchemy(app)

class Countries(db.Model):
    __tablename__ = "country"
    country_id = db.Column(db.Integer,primary_key=True)
    country = db.Column(db.String(70))
    last_update = db.Column(db.DateTime)

column_names = Countries.__table__.columns.keys()

@app.route("/")
def index():
    print(column_names)
    return render_template('index.html',column_names=column_names)