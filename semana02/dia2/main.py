from multiprocessing import context
from flask import Flask, render_template, request, request 

app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Hello World!</h1>'
    
    
    nombre = request.args.get('nombre', '')
    
    context= {
        'nombre': nombre,
    }
    
    return render_template('index.html',**context)

@app.route('/peliculas')
def peliculas():
    listaPeliculas = ['Spiderman', 'Batman', 'Superman']
    
    context = {
        'peliculas': listaPeliculas
    }
    return render_template('peliculas.html', **context)

app.run(debug=True)