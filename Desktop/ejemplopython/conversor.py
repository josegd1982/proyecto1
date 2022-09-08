menu = """
bienvenido al conversor de monedas 😊 🤑💵

1 - pesos colombianos
2 - pesos aargentinos
3 - bolivares VE

elie una opcion:

"""
opcion = input(menu)

if opcion == "1":
    pesos = input ("cuantos pesos colombianos tiene ? ")
    pesos = float(pesos)
    valor_dolar = 4492 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")

elif opcion == "2":
    pesos = input ("cuantos pesos argentinos tiene ? ")
    pesos = float(pesos)
    valor_dolar = 52 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
   
    

elif opcion == "3":
    pesos = input ("cuantos bolivares tiene ? ")
    pesos = float(pesos)
    valor_dolar = 0.774
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")


else:
    print("ingrese una opcion valida")












