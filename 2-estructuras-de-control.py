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
# a = 0
# while(a!=10):
#     print(a) # para cortar un programa que no para se usa: CTRL+C
#     a += 1

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

# Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 7 
# numero = int(input("Ingrese un numero: "))
# fib = [0, 1]
# while True:
#     suma_ant = fib[-2] + fib[-1]
#     if(suma_ant > numero):
#         print("El numero anterior de la secuencia de Fib a ese num es:", fib[-1])
#         break
#     elif(suma_ant == numero):
#         print("El numero de la secuencia de Fib correspondiente a ese num es:", suma_ant)
#         break
#     else:
#         fib.append(suma_ant)

# pasos = int(input("Ingrese la cantidad de pasos de Fib que quiere hacer"))
# num_ant_1 = 0 # paso 1
# num_ant_2 = 1 # paso 2

# if pasos == 1:
#     print("Para el paso 1 el numero de Fib equivalente es:", num_ant_1)
# elif pasos == 2:
#     print("Para el paso 2 el numero de Fib equivalente es:", num_ant_2)
# else:
#     for pasos_realizados in range(2, pasos):
#         paso_actual = num_ant_1 + num_ant_2
#         num_ant_1 = num_ant_2
#         num_ant_2 = paso_actual
#     print(f"Para el paso {pasos} el numero de Fib equivalente es:", paso_actual)

# suma = 0
# suma1 = 1
# fibo = 0
# contador = 0
# n = int(input("Ingrese un número: "))
# print("La secuencia de Fibonacci para el número ingresado es: ")
# print(0)
# print(1)

# while contador<=(n-2):
#     fibo = suma+suma1
#     suma = suma1
#     suma1 = fibo
#     contador+=1
#     print(fibo)
