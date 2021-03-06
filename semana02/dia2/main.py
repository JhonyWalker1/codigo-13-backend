
from pydoc import doc
from flask import Flask, render_template, request
import requests 

URL= 'https://api.github.com/users/JhonyWalker1'



import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("tokenfirebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)

@app.route('/')
def index():
    #nombre = request.args.get('nombre', '')
    
    data=requests.get(URL)
    context = data.json()
    print(context)
 
    
    return render_template('home.html',**context)

@app.route('/peliculas')
def peliculas():
    listaPeliculas = ['Spiderman', 'Batman', 'Superman']
    nombre = request.args.get('nombre', '')
    
    context = {
        'nombre': nombre,
        'peliculas': listaPeliculas
    }
    return render_template('peliculas.html', **context)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/about')
def about():
    return render_template('acercade.html')

@app.route('/portafolio')
def portafolio():
    colProyectos= db.collection('proyectos')
    docProyectos = colProyectos.get() 
   # print(docProyectos)
      
    lstProyectos = []
    for doc in docProyectos:
        print(doc.to_dict())
        dicProyecto = doc.to_dict()
        lstProyectos.append(dicProyecto)
    context = {
        'proyectos': lstProyectos
    }    
    
    return render_template('portafolio.html',**context)

app.run(debug=True)