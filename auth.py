from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.bd'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=true)
    firstname = db.Column(db.String(400), nullable= False)
    email = db.Column(db.String(400), nullable= False)
    address = n(db.String(400), nullable= False)
    
