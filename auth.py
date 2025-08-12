from flask import Flask, request, redirect, render_template
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

@app.route('/' method=['POST', 'GET'])
def index():
    if request.methods == 'POST':
        first_name = request.form['firstname']
        new_name = Users(firstname=first_name)

        try:
            db.session.add(first_name)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the task'
    else
    fname = Users.query.order_by(Todo.date_created).all()
    return render_template('registration.html', fname=fname)




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created!")
    app.run(debug=True)