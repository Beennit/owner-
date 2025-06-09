frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
print(frutas)
for fruta in frutas:
    print(fruta)
print("RECORRIENDO POSICIONES")
for i in range(len(frutas)):
    print(frutas[i])

#PRIMER ELEMENTO DE LA LISTA
print(frutas[0])

#el ultimo elemento de la lista
print(frutas[-1])

#desde el segundo hasta el 4
print(frutas[1:4])

for i in range(len(frutas)):
    if i >0 and i <=3:
        print(frutas[i])
#modificar listas
frutas[1] = "kiwi"
print(frutas)
"""
for i in range(len(frutas)):
    if frutas[i] == "banana":
        frutas[i] = "kiwi"
print(frutas)
"""
#agregar naranja
frutas.append("naranja")
print(frutas)
#insertar uva
frutas.insert(1,"uva")
print(frutas)

#Eliminar cereza
"""
frutas.remove("cereza")
print(frutas)
"""
for i in range(len(frutas)):
    if frutas[i] == "cereza":
        num = i
frutas.pop(num)
print(frutas)

#operaciones con listas
numeros = [10, 20, 30, 40, 50]
#suma de todos los numeros
print(sum(numeros))
suma = 0
for numero in numeros:
    suma += numero
print(suma)
#numero mas grande de la lista de numeros
print(max(numeros))
max =0
for numero in numeros:
    if numero > max:
        max = numero
print(max)

#minimo
print(min(numeros))

min=100
for numero in numeros:
    if numero < min:
        min = numero
print(min)

#lista duplicada multiplicada en 2
numeros_duplicados = numeros.copy()
for i in range(len(numeros_duplicados)):
    numeros_duplicados[i]= numeros_duplicados[i]*2
print(numeros_duplicados)

# 4 comprobar existencia de un elemento en una lista
colores = ["rojo", "verde", "azul", "amarillo"]
if "verde" in colores:
    print("si esta")
else:
    print("no esta el verde")

flag = False
for color in colores:
    if color == "verde":
        flag = True
if flag:
    print("existe el verde")
else:
    print("no esta el verde")

flag = False
for color in colores:
    if color == "negro":
        flag = True
if flag:
    print("existe el negro")
else:
    print("no esta el negro")

dias_semana = ['lunes', 'martes', 'miercoles', 'jueves','viernes','sabado','domingo']
print(len(dias_semana))

#DICCIONARIO
estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "curso": "Ingeniería",
    "promedio": 8.5
}
print(estudiante)
print(estudiante["nombre"])
print(estudiante["curso"])
estudiante["edad"]=23
print(estudiante)
estudiante["universidad"] = "Universidad XYZ"
print(estudiante)
del estudiante["promedio"]
print(estudiante)

#3 operaciones con diccionarios
producto = {
    "nombre": "Laptop", 
    "precio": 1200, 
    "stock": 15
}  
producto["stock"] += 5
print(producto)
producto["precio"] = int(producto["precio"]*0.9)
print(producto)

capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}

for capital in capitales:
    print(capital)
    if capital == "Francia":
        print("Francia se encuentra en el diccionario")
        break
if "Alemania" in capitales:
    print("Alemania es una clave del diccionario")
else:
    print("Alemania no se encuentra en el diccionario")

#5 obtener claves, valores e items
lista_claves = []
for capital in capitales:
    lista_claves.append(capital)

print(lista_claves)

lista_valores = []
for capital in capitales:
    valor = capitales[capital]
    lista_valores.append(valor)

print(lista_valores)

lista_items = []
for capital in capitales:
    item = capital+' : '+capitales[capital]
    lista_items.append(item)
print(lista_items)

numeros = [1, 2, 2, 3, 1, 4, 2, 5, 1, 2]
frecuencias={}
flag = False
for numero in numeros:
    if numero in frecuencias:
        frecuencias[numero]+=1
    else:
        frecuencias[numero]=1

print(frecuencias)