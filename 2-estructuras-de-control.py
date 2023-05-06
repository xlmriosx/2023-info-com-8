# estructuras condicionales
# ... codigo, condicional simple
# if(a==b): # si pasa esto, hace lo que esta debajo
#     print("b y a son iguales")
# else: # si no pasa lo de arriba hace esto
#     print("b y a NO son iguales")

# # condicional multiple
# if(a==b):
#     print("b y a son iguales")
# elif(a*3==30):
#     print("a es igual a 10")
# elif(a/20 == 10):
#     print("")
# else:
#     print("")

# estructuras repetitivas
# repetitiva con contador, rep. con condicional a priori, rep. con condicional posteriori
# for X in range(1,10):
#     print(X)

# for X in "hola como estas":
#     print(X)
a = 0
while(a!=10):
    print(a) # para cortar un programa que no para se usa: CTRL+C
    a += 1

# for i in range(1,11):
#     print("Numero", i)
#     if(i == 5):
#         break

# for j in range(1,4):
#     print("Numero", j)
# intentos = 0
# while True:
#     password = input('Ingrese su contraseña: ')
#     intentos += 1
#     if(password == 'root'):
#         print("Bienvenido a su cuenta")
#         break
#     elif(intentos == 3):
#         print("Tuviste muchos intentos fallidos. Se bloqueo tu cuenta.")
#         break
#     else:
#         print(f"Intente denuevo. Quedan {3-intentos} intentos")


# cont = 0
# continua = input('Continuamos?. Ingrese 1 para continuar: ')
# while continua=='1':
#     cont += 1
#     print(f"Continuamos {cont} veces")
#     continua = input('Continuamos?. Ingrese 1 para continuar: ')
