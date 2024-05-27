from pyswip import Prolog
from collections import Counter
import random

prolog = Prolog()
#prolog.consult("bbdd.pl")
prolog.consult("C:/Users/Bruno/Desktop/IA_BD/MIA/Quien_es_quien/src/bbdd.pl")

personajes = []
personajes_restantes = []
todas_las_caracteristicas = []
caracteristicas = set()

# Obtenemos una lista con todos los nombres de los personajes del tablero con los que vamos a jugar (suponemos que las características ya se saben).
def tablero():
    resultado_query = list(prolog.query("personaje(Nombre,_)"))
    for resultado in resultado_query:
        personajes.append(resultado["Nombre"])

    return personajes

# Esta función nos devuelve un personaje aleatorio del tablero (con sus respectivas caracteristicas), el cuál va a ser el que deberemos adivinar.
def eleccion_personaje():
    resultado_query = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    personaje = random.choice(resultado_query)

    return personaje


# Obtenemos una lista con todas la características distintas que aparecen en las diversas listas de características de cada uno de los personajes.
def lista_caracteristicas():
    resultado_query = list(prolog.query("personaje(_, Caracteristicas)"))
    for resultado in resultado_query:
        for c in resultado["Caracteristicas"]:
            caracteristicas.add(c)

    return caracteristicas

# def pregunta():
#     lista_caracteristicas = lista_caracteristicas()

#     resultado_query = list(prolog.query("personaje(_, Caracteristicas)"))
#     for resultado in resultado_query:
#         todas_las_caracteristicas.extend(resultado["Caracteristicas"])
    
#     contador_caracteristicas = Counter(todas_las_caracteristicas)
#     caracteristica_mas_usada = contador_caracteristicas.most_common(1)[0][0] # Devuelve una lista don una tupla de [Característica, Número de veces que aparece], de ahí que solo acceda a la posición de la caracterítica
#     print(caracteristica_mas_usada)

#     consulta = f"personaje(Nombre, Caracteristicas), member({caracteristica}, Caracteristicas)"
#     for resultado_query in prolog.query(consulta):
#         personajes_restantes.append(resultado_query["Nombre"])
    
#     return personajes_restantes


# result = list(prolog.query("personaje(herman, X)"))

#for solution in result:
#    print("Hombre:", solution["X"])

def main():
    personajes = tablero()
    print("Personajes del tablero: ")
    print(personajes)

    personaje_a_adivinar = eleccion_personaje()
    print(personaje_a_adivinar)

    
    #for p in personajes:
    #    print(f"\t{p}")

main()
