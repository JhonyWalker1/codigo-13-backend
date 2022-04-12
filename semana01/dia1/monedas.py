# PROGRAMA PARA CONVERTIR MONEDAS
# VERSION 1.0 - CONVERSION DE MONEDAS
#INPUTS - ENTRADAS
montoOrigen = input("Ingrese el monto ")
# PROCESOS
"""opcion = input("que tipo de moneda desea convertir? (1)Dolares (2)Euros: ")"""
opcion = ""
while(opcion == ""):
        print("opcion 1 - soles a dolares")
        print("opcion 2 - dolares a soles")
        print("opcion 3 - euros a soles")
        print("opcion 4 - soles a euros")
        opcion = input("eliga una opcion: ")    
        if (opcion == "1"):
            montoDolares = float(montoOrigen) / 3.80
            montoDolaresFormato = "${:,.2f}".format(montoDolares)
            #OUTPUTS - SALIDAS
            print("El monto en soles es: " + str(montoDolaresFormato))
            salir= "0"
            while(salir == "0"):
                salir = input("Desea continuar? (1)Si (2)No : ")  
                if (salir == "1"):
                  opcion = ""
                elif (salir == "2"):
                  print("Gracias por usar el programa")
                  break
                else:
                  print("Eleccion no válida")
                  salir= "0"
                  
        elif(opcion == "2"):
            montoSoles = float(montoOrigen) * 3.80
            montoSolesFormato = "S/{:,.2f}".format(montoSoles)
            #OUTPUTS - SALIDAS
            print("El monto en dolares es: ", montoSolesFormato)
            salir= "0"
            while(salir == "0"):
                salir = input("Desea continuar? (1)Si (2)No : ")  
                if (salir == "1"):
                  opcion = ""
                elif (salir == "2"):
                  print("Gracias por usar el programa")
                  break
                else:
                  print("Eleccion no válida")
                  salir= "0"

        elif (opcion == "3"):
            montoEuros = float(montoOrigen) * 4.05
            montoEurosFormato = "S/{:,.2f}".format(montoEuros)
            #OUTPUTS - SALIDAS
            print("El monto en soles es: " + str(montoEurosFormato))
            salir= "0"
            while(salir == "0"):
                salir = input("Desea continuar? (1)Si (2)No : ")  
                if (salir == "1"):
                  opcion = ""
                elif (salir == "2"):
                  print("Gracias por usar el programa")
                  break
                else:
                  print("Eleccion no válida")
                  salir= "0"

        elif(opcion == "4"):
            montoSoles = float(montoOrigen) / 4.05
            montoSolesFormato = "€{:,.2f}".format(montoSoles)
            #OUTPUTS - SALIDAS
            print("El monto en euros es: ", montoSolesFormato)
            salir= "0"
            while(salir == "0"):
                salir = input("Desea continuar? (1)Si (2)No : ")  
                if (salir == "1"):
                  opcion = ""
                elif (salir == "2"):
                  print("Gracias por usar el programa")
                  break
                else:
                  print("Eleccion no válida")
                  salir= "0"

        else:
            print("opcion no valida")
            opcion=""
            break


"""  print("El monto en dolares es: " , montoDolaresFormato)"""
