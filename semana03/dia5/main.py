from flask import Flask,jsonify,request
from flask_mysqldb import MySQL


app = Flask(__name__)

#CONEXION A LA BASE DE DATOS MYSQL
app.config['MYSQL_HOST'] = 'localhost'  ##IP- EN ESTE CASO ES LOCAL
app.config['MYSQL_USER'] = 'root'  ##usuario
app.config['MYSQL_PASSWORD'] = '' ##PASSWORD
app.config['MYSQL_DB'] = 'db_colegio' ##NOMBRE DE LA BASE DE DATOS

mysql = MySQL(app)

@app.route('/')
def index():
    return jsonify({
        'status':'ok',
        'mensaje':'Bienvenido a la API de la aplicacion'
    })

@app.route('/alumno', methods=['GET'])
def getAlumno():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_alumno")
    data = cur.fetchall()
    cur.close()
    
    print(data)
    """ alumnos = []
    for alumno in data:
        alumnos.append({
            'id':alumno[0],
            'nombre':alumno[1],
            'apellido':alumno[2],
            'edad':alumno[3]
        }) """
    return jsonify({
        'status':'ok',
        'mensaje':'Listado de alumnos',
        'alumno':data
    })

@app.route('/alumno', methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    celular = request.json['celular']
    github = request.json['github']
    
    cursor = mysql.connection.cursor()
    
    cursor.execute("insert into tbl_alumno(alumno_nombre,alumno_celular,alumno_github) values('"+ nombre +"','"+ celular +"','"+ github +"')")
    
   # cursor.execute("insert into tbl_alumno(alumno_nombre,alumno_celular,alumno_github) values('"+ nombre +"','"+ celular +"','"+ github +"')")
    
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({
        "ok":True,
        "mensaje":"Alumno agregado"
    })


if __name__ == '__main__':
    app.run(debug=True,port=5000)