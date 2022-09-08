# def imprimir_mensaje():
   # print("mensaje especial:  ")
  #  print("!Estoy aprendiendo funciones que fino");

# imprimir_mensaje()

# imprimir_mensaje()

# imprimir_mensaje() 


def conversacion(mensaje):
    print("hola")
    print("como estas")
    print(mensaje)
    print("Adios")

opcion = int(input("elije una opcion (1, 2, 3): ") )

if opcion == 1:
    conversacion("elegiste la pcion 1")
    
elif opcion == 2:
    conversacion("elegiste la pcion 2")
elif opcion == 3:
    conversacion("elegiste la pcion 3")
else:
    print("elije una opcin valida")

