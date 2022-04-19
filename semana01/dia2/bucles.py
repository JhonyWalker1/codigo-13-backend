#bucle es algo que se va a volver a repetir
#entrada
tabla = int(input("ingresa la tabla de multiplicar que desea mostrar: "))
#proceso
valor1 = tabla * 1;
valor2 = tabla * 2;
valor3 = tabla * 3;
#salida
print(str(tabla) + " * 1 = " + str(valor1))
print(str(tabla) + " * 2 = " + str(valor2))
print(str(tabla) + " * 3 = " + str(valor3))


#tabla de multiplicar usando for
print("tabla usando for")
#range(num1, num2, num3) => num1 es el valor inicial, num2 es el valor final y no cuenta el ultimo, es el numero de salto, de 1 en 1 de 2 en 2 etc
for contador in range(1,11):
    print(str(tabla) + " * " + str(contador) + " = " + str(tabla*contador))