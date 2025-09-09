from flask import Flask, request, redirect, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__, template_folder="templates")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(400), nullable=False)
    address = db.Column(db.String(400), nullable=False)
    password_hash = db.Column(db.String(400), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  

    def __repr__(self):
        return '<users %r>' % self.id

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstname']
        email = request.form['email']
        address = request.form['address']
        password_hash = request.form['password_hash']

        hashed_password = generate_password_hash(password, method='sha256')


        try:
            new_user = Users(
                firstname=first_name,
                email=email,
                address=address,
                password_hash=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect('/register')
        except:
            return 'There was an issue adding the User'
    else:
        fname = Users.query.order_by(Users.date_created).all()
        return render_template('registration.html', fname=fname)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        email = request.form['email']
        password_hash = request.form['password_hash']

        user = Users.query.filter_by(email=email, password_hash=password).first()

        if
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created!")
    app.run(debug=True)
