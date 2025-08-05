from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[SQLALCHEMY_DATABASE_URl] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.model):
    id = db.Column(db.Integer, primary_key = true)
    content = db.Column(db.String(200), nullable = flase)
    commpleted = db.Column(db.Integer, default = 0)

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)