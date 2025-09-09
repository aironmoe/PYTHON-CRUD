from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(400), nullable=False, unique=True)
    address = db.Column(db.String(400), nullable=False)
    password_hash = db.Column(db.String(400), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  

    def __repr__(self):
        return f'<User {self.email}>'

# 🏠 Default home route
@app.route('/')
def home():
    return redirect('/register')

# 📝 Registration
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstname']
        email = request.form['email']
        address = request.form['address']
        password = request.form['password_hash']

        # Hash password properly
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

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
        except Exception as e:
            return f'There was an issue adding the User: {e}'
    else:
        fname = Users.query.order_by(Users.date_created).all()
        return render_template('registration.html', fname=fname)

# 🔑 Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password_hash']  # plain password from form

        user = Users.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            return f"Welcome, {user.firstname}!"
        else:
            return "Invalid email or password."

    return render_template('login.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created!")
    app.run(debug=True)
