import tabulate
from libAlumnos import buscarAlumno, menu,cargarAlumnos
##############################
""" #########FUNCIONES#######################################
def buscarAlumno(valorBusqueda, alumnos):
    indexAlumno = -1
    for i in range(len(alumnos)):
        if(alumnos[i]['email'] == valorBusqueda):
            indexAlumno = i
            break

    return indexAlumno
####################################################### """


# PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D
menu()
opcion = 0
#alumnos = [{'nombre': 'cesar mayta', 'email':'cesarmayta@gmail.com','celular':'232323'}]
##alumnos=[]
#cargamos datos del archivo de texto
f = open('alumnos.txt','r')
strAlumnos= f.read()
alumnos = cargarAlumnos(strAlumnos)
f.close
while(opcion != 5):
    opcion = int(input("INGRESE OPCIÓN DEL MENU :"))
    if(opcion == 1):
        print("NUEVO ALUMNO ")
        nombre = input("NOMBRE  : ")
        email = input("EMAIL   : ")
        celular = input("CELULAR : ")
        dictAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
        alumnos.append(dictAlumno)
        print("ALUMNO REGISTRADO CON EXITO!!!")
    elif(opcion == 2):
        print("RELACIÓN DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros, cabeceras))
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
        # PASO 1 BUSCAR EL ALUMNO A EDITAR
        valorBusqueda = input("INGRESE EL EMAIL DEL ALUMNO A EDITAR : ")
        indexAlumno = buscarAlumno(valorBusqueda, alumnos)
        #print("el alumno esta en el indice : " +str(indexAlumno))
        #print ("datos del alumno:" +str(alumnos[indexAlumno]))
        # PASO 2 INGRESAR NUEVOS VALORES A EDITAR
        if(indexAlumno == -1):
            print("EL ALUMNO NO EXISTE")
        else:
            nombre = input("NOMBRE  : ")
            email = input("EMAIL   : ")
            celular = input("CELULAR : ")
            dictAlumno = {
                'nombre': nombre,
                'email': email,
                'celular': celular
            }
            # PASO 3 ACTUALIZAR EL ALUMNO
            alumnos[indexAlumno] = dictAlumno
            print("ALUMNO ACTUALIZADO CON EXITO!!!")

    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
        valorBusqueda = input("INGRESE EL EMAIL DEL ALUMNO A ELIMINAR : ")
        indexAlumno = buscarAlumno(valorBusqueda, alumnos)
        if(indexAlumno == -1):
            print("EL ALUMNO NO EXISTE")
        else:
            alumnos.pop(indexAlumno)
            print("ALUMNO ELIMINADO CON EXITO!!!")
    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")
