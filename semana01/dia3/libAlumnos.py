#LIBRERIA DE ALUMNOS
#########FUNCIONES#######################################
def menu():
    print("-" * 50)
    print("|" + " " * 9 + "MATRICULA DE ALUMNOS EN CODIGO " + " " * 8 + "|")
    print("-" * 50)
    print("|" + " " * 9 + "MENU DE OPCIONES     " + " " * 18 + "|")
    print("|" + " " * 9 + "[1] REGISTRAR ALUMNO " + " " * 18 + "|")
    print("|" + " " * 9 + "[2] MOSTRAR ALUMNOS  " + " " * 18 + "|")
    print("|" + " " * 9 + "[3] ACTUALIZAR ALUMNO" + " " * 18 + "|")
    print("|" + " " * 9 + "[4] ELIMINAR ALUMNO  " + " " * 18 + "|")
    print("|" + " " * 9 + "[5] SALIR            " + " " * 18 + "|")
    print("-" * 50)

def buscarAlumno(valorBusqueda, alumnos):
    indexAlumno = -1
    for i in range(len(alumnos)):
        if(alumnos[i]['email'] == valorBusqueda):
            indexAlumno = i
            break

    return indexAlumno
#######################################################
def cargarAlumnos(strAlumnos):
    alumnos = []
    ##proceso para convertir una cadena string a una lista de diccionario
    ##el splitlines() guarda toda la info separando por lineas
    listaAlumnos = strAlumnos.splitlines()
    for l in listaAlumnos:
        alumnoData = l.split(',')
        dictAlumno = {
            'nombre': alumnoData[0],
            'email': alumnoData[1],
            'celular': alumnoData[2],
        }
        alumnos.append(dictAlumno)
    return alumnos


def grabarAlumnos(alumnos):
    ##convierte una lista de diccionarios a una cadena string
    strAlumnos= ""
    c=1
    for l in alumnos:
        for clave,valor in l.items():
            strAlumnos += str(valor)
            if clave != 'celular':
                strAlumnos += ','