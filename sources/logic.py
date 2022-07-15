from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from data import Drink

@app.route('/')
def index():
    return 'liquids ver.1.0'

@app.route('/drinks')
def drinks():
    return {
        "drinks":"drink data",
    }

