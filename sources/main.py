from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

        

@app.route('/')
def index():
    return 'liquids ver.1.0'

@app.route('/drinks')
def drinks():
    return {
        "drinks":"drink data",
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')