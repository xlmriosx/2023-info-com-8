# b = 0
# tupla = ([1,2], b, ['2', '43']) # posiciones[#0, #1, #2, #3]
# print(tupla)
# tupla[0].append(32)
# print(tupla)
# tupla[0].pop(1)
# print(tupla)
#tupla[2][1]=44 # tupla[2] -> ['2', '43'][1] -> '43'
#print(tupla)

# suma = str(tupla[0][0]) + tupla[2][1]
# print("concatenacion", suma)
# suma = tupla[0][0] + int(tupla[2][1])
# print("suma de verdad", suma)

### EJERCICIO 18
# print("Nombre:", input("Ingrese su nombre: "), "Residencia:", input("Ingrese su residencia: "), "Edad:", input("Ingrese su edad: "))
# datos_personales=input('ingrese su nombre , edad y ciudad de residencia: ')
# nombre, edad, residencia=map(str, datos_personales.split(','))

# datos_personales = input('ingrese su nombre , edad y ciudad de residencia: ')
# nombre, edad, residencia = datos_personales.split(',') # "Lucas, 13, Resistencia" -> Lucas | 13 | Resistencia -> nombre="Lucas" | edad="13" | residencia="Resitencia"
# print('nombre: '+str(nombre)+' edad: '+str(edad)+' años'+' residenci: '+str(residencia))

# Respuesta
# print("Nombre:", input("Ingrese su nombre: "), "Edad:", input("Ingrese su edad: "), "Residencia:", input("Ingrese su residencia: "))

### EJERCICIO 12
# Objetivo: Obtener mi edad por medio de mi fecha de nacimiento
# en formato de dd/mm/yyyy -> day, month, year
import datetime
print('Ingrese su fecha de nacimiento dd/mm/aaaa')
fecha_nac = input()
dia, mes, anio = map(int, fecha_nac.split('/'))

fecha_act = datetime.date.today()
anio_hoy = fecha_act.year
mes_hoy = fecha_act.month
dia_hoy = fecha_act.day

edad = anio_hoy - anio

if(mes > mes_hoy): # estructura condicional multiple
    edad = edad - 1
    print('Tu edad actual es de '+str(edad)+' años')
elif((mes == mes_hoy) and (dia == dia_hoy)):
    print("feliz cumple numero", edad, "pirulos")
elif((mes == mes_hoy) and (dia < dia_hoy)):
    print("feliz cumple numero", edad, "atrasado")
elif((mes == mes_hoy) and (dia <= dia_hoy+3)):
    print("falta poco para tu cumple numero", edad)

# if(): condicional simple
# if() else: condicional alternativo

lista = ['palbra', 'palabra2', 'palabra3', 'palabra4']
# lista[0], lista[-1]
lista = lista.reverse()
