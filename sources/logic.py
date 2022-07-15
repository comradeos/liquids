from flask import Flask, request
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from data import Drink


@app.route('/')
def index():
    return 'liquids ver.1.0'


@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()
    output = []

    for drink in drinks:
        data = {
            'name': drink.name,
            'description': drink.description,
        }
        output.append(data)
    return {'drinks': output}


@app.route('/drinks/<id>', methods=['GET'])
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {'name': drink.name, 'description': drink.description}


@app.route('/drinks', methods=['POST'])
def add_drink():
    new_drink = Drink(name=request.json['name'], description=request.json['description'])
    try:
        db.session.add(new_drink)
        db.session.commit()
        return {'id': new_drink.id}
    except:
        return {'error': 'unique name required'}


@app.route('/drinks/delete/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink == None:
        return {'error': 'not found'}
    try:
        db.session.delete(drink)
        db.session.commit()
        return {'response': f"{drink.name} has been deleted"}
    except:
        return {'error': 'error'}


@app.route('/drinks/update/', methods=['PUT'])
def update_drink():
    id = request.json['id']
    drink = Drink.query.get(id)
    
    if drink == None:
        return {'error': 'not found'}
    
    drink.name = request.json['name']
    drink.description = request.json['description']
    
    try:
        db.session.commit()
        return {'response': f"{drink.name} has been updated"}
    except:
        return {'error': 'error'}

