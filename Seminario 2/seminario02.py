#####################################################################################################
# GRUPO 27                                                                                          #
#                                                                                                   #
# Componentes:                                                                                      #
# Adrian Garrido Adriano                                                                            #
# Jose Alberto Jimenez Serrano                                                                      #
#                                                                                                   #
# Vamos a desarrollar el programa de Python que nos permita, a partir de una lista de               #
# palabras, encontrar la lista mas larga posible de palabras de manera que la ultima letra de       #
# una palabra coincida con la primera de la siguiente palabra. Para probar el programa la lista     #
# de palabras con las que vamos a trabajar son la que encontramos en el fichero pokemon.txt         #
#####################################################################################################

#NOTA: Los comentarios no pueden tener acentos debido a que da error al compilar.

#Definimos las funciones que vamos a usar para realizar el ejercicio
def contarPokemons():
    maximo = 0;
    #Creamos un bucle para probar empezando desde cada uno de los diferentes pokemons de la lista
    for i in range(0, len(lista)-1, 1):
        #Seleccionamos el pokemon actual como actual, y lo introducimos en la lista de vistas, para que no vuelva a ser contemplado en esta iteracion
        actual = lista[i]
        vistas = [actual]
        #Llamamos a la funcion recurrente que cuenta todas las palabras encadenadas a partir de dicho pokemon
        nuevo = 1 + funcionrecurrente(actual[len(actual)-1], 1, vistas)
        #Si la nueva lista es mayor que la anterior, guardamos el maximo
        if(nuevo > maximo):
            maximo = nuevo
        #Por ultimo guardamos la lista para mostrarla posteriormente
        #Como no sabemos cual va a ser la lista mas grande, guardamos todas, para posteriormente filtrarlas al mostrarlas.
        listavistas.append(vistas)
    #Devolvemos el numero de elementos que posee la lista mas grande al final del bucle
    return maximo
    
#Definimos la funcion recurrente que se encargara del proceso.
def funcionrecurrente(letra, i, vistas):
    #Debemos de comprobar primero, que no se le pase un indice fuera del rango de la lista. Si se hace, la funcion devolvera 0.
    if(i<len(lista)):
        #Si es elemento existente lo seleccionamos como actual.
        actual = lista[i]
        #Si la letra coincide segun el criterio, y aun no esta marcado como vista, lo marcamos como vista, y llamamos de nuevo a la funcion
        #para buscar el siguiente elemento de la lista, que empezara desde el principio a buscar
        if(letra == actual[0] and (actual in vistas) == 0):
            vistas.append(lista[i])
            #Como se acordo, no se explora el resto de la lista, solo se coge el primer elemento que se encuentre.
            return 1 + funcionrecurrente(actual[len(actual)-1], 0, vistas)
        #Si no, seguimos con el mismo pokemon anterior, buscando en la siguiente posicion de la lista.
        else:
            return funcionrecurrente(letra, i+1, vistas)
    else:
        return 0
        
#Una vez en el programa principal, leemos la lista del fichero "pokemon.txt"
file = open("pokemon.txt", "r")
data = file.readlines()
file.close()

#Inicializamos las diferentes variables que vamos a necesitar
contador = 0
lista = []
listavistas = []

#Pasamos la lista de pokemons a una estructura de datos de tipo lista.
for linea in data:
    for palabra in linea.split(' '):
        lista.append(palabra)
        contador += 1

#Llamamos a la funcion para realizar el proceso.
solucion = contarPokemons()

#Mostramos por pantalla el resultado
print "La lista mas larga tiene" , solucion, "elementos, y puede ser una de las siguientes opciones:\n"

#Mostramos las diferentes listas validas
for i in range(0, len(listavistas), 1):
    if(len(listavistas[i]) == solucion):
        print listavistas[i]