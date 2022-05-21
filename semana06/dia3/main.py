
from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson.json_util import dumps

import json

cliente = MongoClient('localhost',27017)
db=cliente['colegio']

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'status': True,
        'message': 'Bienvenido a la API de la base de datos con MongoDB'
    })
    
@app.route('/alumno')
def getAlumno():
    
    colAlumnos = db['alumno']
    
    
    context = {
        'status': True,
        'content': json.loads(dumps(colAlumnos.find({},{"nombre":1,"email":1,"_id":0})))
    }
    
    
    return jsonify(context)

app.run(debug=True, port=5000)