from pyswip import Prolog
from collections import Counter
import random

prolog = Prolog()
#prolog.consult("bbdd.pl")
prolog.consult("C:/Users/Bruno/Desktop/IA_BD/MIA/Quien_es_quien/src/bbdd.pl")

personajes = []
personajes_restantes = []
todas_las_caracteristicas = []

# Imprimimos la lista de personajes que se nos pasa por parámetro (nombre y características).
def tablero(lista_personajes):
    for personaje in lista_personajes:
        print(f"{personaje["Nombre"]}: {personaje["Caracteristicas"]}")


# Esta función nos devuelve un personaje aleatorio del tablero (con sus respectivas caracteristicas), el cuál va a ser el que deberemos adivinar.
def eleccion_personaje():
    resultado_query = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    personaje = random.choice(resultado_query)

    return personaje

# Devuelve la característica a preguntar siguiendo nuestro algoritmo (explicado en el README.md).
def caracteristica(lista):
    contador_caracteristicas = 0
    todas_las_caracteristicas = []

    for p in lista:
        for c in p["Caracteristicas"]:
            todas_las_caracteristicas.append(c)
    
    contador_caracteristicas = Counter(todas_las_caracteristicas)
    contador_caracteristicas = sorted(contador_caracteristicas.items(), key=lambda i: i[1], reverse=True)

    return contador_caracteristicas[int(len(contador_caracteristicas)/2)][0]

# Devuelve un booleano sobre si el personaje que se tiene que adivinar tiene la caracteristica que se le pasa o no.
def pregunta(personaje_secreto, caract):
    if caract in personaje_secreto["Caracteristicas"]:
        return True
    return False


def main():
    preguntas = 0

    # Obtenemos el personaje a adivinar.
    personaje_a_adivinar = eleccion_personaje()
    print(f"El personaje a adivinar es: {personaje_a_adivinar["Nombre"]}({personaje_a_adivinar["Caracteristicas"]})")

    # Realizamos una consulta prolog para sacar todos los personajes del tablero según iniciamos la partida y los imprimimos.
    resultado_query = list(prolog.query("personaje(Nombre,Caracteristicas)"))
    print("\n\n<----------------------------------------------------->")
    print("Personajes del tablero: ")

    # Repetimos el bucle hasta que solo quede un único personaje.
    while(len(resultado_query) != 1):
        
        tablero(resultado_query)
        personajes_temp = []

        # Sacamos la característica que tenemos que preguntar.
        caracteristica_a_preguntar = caracteristica(resultado_query)
        print(f"\nTu personaje tiene {caracteristica_a_preguntar}?")


        # Usamos una nueva lista para añadir los personajes que si o no tengan la característica que se pregunta.
        if pregunta(personaje_a_adivinar, caracteristica_a_preguntar):
            print(f"Si, tiene {caracteristica_a_preguntar}\n")
            for p in resultado_query:
                if caracteristica_a_preguntar in p['Caracteristicas']:
                    personajes_temp.append(p)
        else:
            print(f"No, no tiene {caracteristica_a_preguntar}\n")
            for p in resultado_query:
                if caracteristica_a_preguntar not in p['Caracteristicas']:
                    personajes_temp.append(p)

        # Imprimos la nueva lista resultante después de realizar la pregunta
        resultado_query = personajes_temp
        preguntas += 1

    print(f"El personaje es: {resultado_query}")
    print(f"Número de preguntas: {preguntas}")

main()
