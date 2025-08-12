from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(400), nullable= False)
    email = db.Column(db.String(400), nullable= False)
    address = db.Column(db.String(400), nullable= False)
    password_hash =  db.Column(db.String(400), nullable= False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  

    def __repr__(self):
        return '<users %r>' % self.id

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created!")
    app.run(debug=True)