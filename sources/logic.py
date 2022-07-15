from flask import Flask, request
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from data import Liquid


@app.route('/')
def index():
    return 'liquids ver.1.0'


@app.route('/liquids', methods=['GET'])
def get_liquids():
    liquids = Liquid.query.all()
    output = []

    for liquid in liquids:
        data = {
            'name': liquid.name,
            'description': liquid.description,
        }
        output.append(data)
    return {'liquids': output}


@app.route('/liquids/<id>', methods=['GET'])
def get_liquid(id):
    liquid = Liquid.query.get_or_404(id)
    return {'name': liquid.name, 'description': liquid.description}


@app.route('/liquids', methods=['POST'])
def add_liquid():
    new_liquid = Liquid(name=request.json['name'], description=request.json['description'])
    try:
        db.session.add(new_liquid)
        db.session.commit()
        return {'id': new_liquid.id}
    except:
        return {'error': 'unique name required'}


@app.route('/liquids/delete/<id>', methods=['DELETE'])
def delete_liquid(id):
    liquid = Liquid.query.get(id)
    if liquid == None:
        return {'error': 'not found'}
    try:
        db.session.delete(liquid)
        db.session.commit()
        return {'response': f"{liquid.name} has been deleted"}
    except:
        return {'error': 'error'}


@app.route('/liquids/update/', methods=['PUT'])
def update_liquid():
    id = request.json['id']
    liquid = Liquid.query.get(id)
    
    if liquid == None:
        return {'error': 'not found'}
    
    liquid.name = request.json['name']
    liquid.description = request.json['description']
    
    try:
        db.session.commit()
        return {'response': f"{liquid.name} has been updated"}
    except:
        return {'error': 'error'}

