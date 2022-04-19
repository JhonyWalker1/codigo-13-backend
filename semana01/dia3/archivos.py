
f= open('alumnos.txt','w')
f.write('Juan Perez, juan@gmail.com, 123132132\n')
f.write('Ana Perez, ana@gmail.com, 123132132\n')
f.write('Pepe Perez, pepe@gmail.com, 123132132\n')

f=open('alumnos.txt','r')
alumnos = f.read()
print(alumnos)

listaAlumnos= alumnos.splitlines()
print(listaAlumnos)

