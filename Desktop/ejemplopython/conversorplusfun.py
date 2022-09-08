
def conversor(tipo_moneda, valor_dolar):
    pesos = input ("cuantos dinero " + tipo_moneda + "tienes? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")



menu = """
bienvenido al conversor de monedas 😊 🤑💵


1 - pesos colombianos
2 - pesos aargentinos
3 - bolivares VE

elie una opcion:

"""
opcion = input(menu)

if opcion == "1":
    conversor("colombianos ", 4492 )

elif opcion == "2":
    conversor("Argentinos ",  44 )
   

elif opcion == "3":
    conversor("Bolivares ",  0.575 )

else:
    print("ingrese una opcion valida")












