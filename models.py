from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(50), nullable=True, unique=True)
    phone = db.Column(db.String(15), nullable=True, unique=False)

    def __repr__(self):
        return '<Doctors %r>' % self.name

class Patient(db.Model):
    __tablename__ = 'patients'

    P_id = db.Column(db.Integer, primary_key=True)
    P_name = db.Column(db.String(80), nullable=False)
    P_surname = db.Column(db.String(100), nullable=True)
    P_email = db.Column(db.String(50), nullable=True, unique=True)
    P_phone = db.Column(db.String(15), nullable=True, unique=False)

    def __repr__(self):
        return '<Patients %r>' % self.P_name
  
