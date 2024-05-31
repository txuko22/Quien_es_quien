import pytest
from pyswip import Prolog

from src.main import tablero, eleccion_personaje, caracteristica, pregunta

prolog = Prolog()
prolog.consult('src/bbdd.pl')

# lista = [{'Nombre': 'herman', 'Caracteristicas': ['hombre', 'pelirrojo', 'calva', 'nariz_grande', 'ojos_marrones', 'cejas_gruesas']}, 
#          {'Nombre': 'maria', 'Caracteristicas': ['mujer', 'pelo_largo', 'sombrero', 'pendientes', 'pelo_castanho', 'ojos_marrones', 'boca_pequenha', 'cejas_finas', 'nariz_pequenha']}, 
#          {'Nombre': 'claire', 'Caracteristicas': ['mujer', 'gafas', 'sombrero', 'pelirrojo', 'ojos_marrones', 'boca_pequenha', 'nariz_pequenha']}, 
#          {'Nombre': 'charles', 'Caracteristicas': ['hombre', 'bigote', 'pelo_rubio', 'ojos_marrones', 'labios_gruesos', 'boca_grande', 'orejas_grandes', 'raya_al_lado', 'nariz_pequenha']}, 
#          {'Nombre': 'richard', 'Caracteristicas': ['hombre', 'calva', 'barba', 'ojos_marrones', 'orejas_grandes', 'bigote', 'cara_alargada', 'nariz_pequenha']}, 
#          {'Nombre': 'eric', 'Caracteristicas': ['hombre', 'pelo_rubio', 'gorra', 'sombrero', 'ojos_marrones', 'boca_grande', 'nariz_pequenha']}, 
#          {'Nombre': 'alex', 'Caracteristicas': ['hombre', 'bigote', 'pelo_negro', 'ojos_marrones', 'boca_grande', 'labios_gruesos', 'orejas_grandes', 'pelo_corto', 'nariz_pequenha']}, 
#          {'Nombre': 'peter', 'Caracteristicas': ['hombre', 'canas', 'pelo_blanco', 'nariz_grande', 'ojos_azules', 'cejas_gruesas', 'labios_gruesos', 'boca_grande', 'raya_al_lado']}, 
#          {'Nombre': 'philip', 'Caracteristicas': ['hombre', 'barba', 'pelo_negro', 'ojos_marrones', 'orejas_grandes', 'mofletes', 'mejillas_sonrosadas', 'cejas_finas', 'pelo_corto', 'nariz_pequenha']}, 
#          {'Nombre': 'joe', 'Caracteristicas': ['hombre', 'gafas', 'pelo_rubio', 'ojos_marrones', 'boca_pequenha', 'pelo_corto', 'nariz_pequenha']}, 
#          {'Nombre': 'paul', 'Caracteristicas': ['hombre', 'gafas', 'pelo_blanco', 'canas', 'ojos_marrones', 'boca_pequenha', 'orejas_grandes', 'cejas_gruesas', 'raya_al_lado', 'nariz_pequenha']}, 
#          {'Nombre': 'david', 'Caracteristicas': ['hombre', 'barba', 'pelo_rubio', 'ojos_marrones', 'orejas_grandes', 'raya_al_lado', 'nariz_pequenha']}, 
#          {'Nombre': 'george', 'Caracteristicas': ['hombre', 'cara_triste', 'sombrero', 'pelo_blanco', 'canas', 'ojos_marrones', 'boca_grande', 'nariz_pequenha']}, 
#          {'Nombre': 'frans', 'Caracteristicas': ['hombre', 'pelo_corto', 'cejas_gruesas', 'pelirrojo', 'ojos_marrones', 'boca_pequenha', 'nariz_pequenha']}, 
#          {'Nombre': 'alfred', 'Caracteristicas': ['hombre', 'bigote', 'barba', 'pelirrojo', 'ojos_azules', 'boca_pequenha', 'orejas_grandes', 'pelo_largo', 'raya_al_medio', 'nariz_pequenha']}, 
#          {'Nombre': 'bernard', 'Caracteristicas': ['hombre', 'pelo_castanho', 'sombrero', 'ojos_marrones', 'boca_pequenha', 'cejas_finas', 'nariz_grande']}, 
#          {'Nombre': 'bill', 'Caracteristicas': ['hombre', 'barba', 'pelirrojo', 'ojos_marrones', 'orejas_grandes', 'mofletes', 'mejillas_sonrosadas', 'calva', 'boca_pequenha', 'nariz_pequenha']}, 
#          {'Nombre': 'anita', 'Caracteristicas': ['mujer', 'pelo_largo', 'pelo_rubio', 'ojos_marrones', 'boca_pequenha', 'mofletes', 'mejillas_sonrosadas', 'raya_al_medio', 'nariz_pequenha']}, 
#          {'Nombre': 'robert', 'Caracteristicas': ['hombre', 'cara_triste', 'pelo_castanho', 'ojos_azules', 'orejas_grandes', 'nariz_grande', 'raya_al_lado', 'cara_alargada', 'mofletes', 'mejillas_sonrosadas']}, 
#          {'Nombre': 'anne', 'Caracteristicas': ['mujer', 'pelo_corto', 'pendientes', 'pelo_negro', 'ojos_marrones', 'boca_pequenha', 'nariz_grande']}, 
#          {'Nombre': 'sam', 'Caracteristicas': ['hombre', 'gafas', 'calva', 'pelo_blanco', 'canas', 'ojos_marrones', 'boca_pequenha', 'nariz_pequenha']}, 
#          {'Nombre': 'tom', 'Caracteristicas': ['hombre', 'gafas', 'calva', 'pelo_negro', 'ojos_azules', 'boca_pequenha', 'cara_alargada', 'nariz_pequenha']}, 
#          {'Nombre': 'susan', 'Caracteristicas': ['mujer', 'pelo_largo', 'pelo_blanco', 'canas', 'ojos_marrones', 'labios_gruesos', 'mofletes', 'mejillas_sonrosadas', 'nariz_pequenha', 'raya_al_lado']}, 
#          {'Nombre': 'max', 'Caracteristicas': ['hombre', 'bigote', 'pelo_negro', 'ojos_marrones', 'boca_grande', 'labios_gruesos', 'nariz_grande', 'orejas_grandes', 'pelo_corto']}]
        
lista = list(prolog.query("personaje(Nombre,Caracteristicas)"))

@pytest.mark.tablero
def test_tablero(capfd):
    tablero(lista)

    out, err = capfd.readouterr()

    resultado_esperado = '''herman: ['hombre', 'pelirrojo', 'calva', 'nariz_grande', 'ojos_marrones', 'cejas_gruesas']
maria: ['mujer', 'pelo_largo', 'sombrero', 'pendientes', 'pelo_castanho', 'ojos_marrones', 'boca_pequenha', 'cejas_finas', 'nariz_pequenha']
claire: ['mujer', 'gafas', 'sombrero', 'pelirrojo', 'ojos_marrones', 'boca_pequenha', 'nariz_pequenha']
charles: ['hombre', 'bigote', 'pelo_rubio', 'ojos_marrones', 'labios_gruesos', 'boca_grande', 'orejas_grandes', 'raya_al_lado', 'nariz_pequenha']
richard: ['hombre', 'calva', 'barba', 'ojos_marrones', 'orejas_grandes', 'bigote', 'cara_alargada', 'nariz_pequenha']
eric: ['hombre', 'pelo_rubio', 'gorra', 'sombrero', 'ojos_marrones', 'boca_grande', 'nariz_pequenha']
alex: ['hombre', 'bigote', 'pelo_negro', 'ojos_marrones', 'boca_grande', 'labios_gruesos', 'orejas_grandes', 'pelo_corto', 'nariz_pequenha']
peter: ['hombre', 'canas', 'pelo_blanco', 'nariz_grande', 'ojos_azules', 'cejas_gruesas', 'labios_gruesos', 'boca_grande', 'raya_al_lado']
philip: ['hombre', 'barba', 'pelo_negro', 'ojos_marrones', 'orejas_grandes', 'mofletes', 'mejillas_sonrosadas', 'cejas_finas', 'pelo_corto', 'nariz_pequenha']
joe: ['hombre', 'gafas', 'pelo_rubio', 'ojos_marrones', 'boca_pequenha', 'pelo_corto', 'nariz_pequenha']
paul: ['hombre', 'gafas', 'pelo_blanco', 'canas', 'ojos_marrones', 'boca_pequenha', 'orejas_grandes', 'cejas_gruesas', 'raya_al_lado', 'nariz_pequenha']
david: ['hombre', 'barba', 'pelo_rubio', 'ojos_marrones', 'orejas_grandes', 'raya_al_lado', 'nariz_pequenha']
george: ['hombre', 'cara_triste', 'sombrero', 'pelo_blanco', 'canas', 'ojos_marrones', 'boca_grande', 'nariz_pequenha']
frans: ['hombre', 'pelo_corto', 'cejas_gruesas', 'pelirrojo', 'ojos_marrones', 'boca_pequenha', 'nariz_pequenha']
alfred: ['hombre', 'bigote', 'barba', 'pelirrojo', 'ojos_azules', 'boca_pequenha', 'orejas_grandes', 'pelo_largo', 'raya_al_medio', 'nariz_pequenha']
bernard: ['hombre', 'pelo_castanho', 'sombrero', 'ojos_marrones', 'boca_pequenha', 'cejas_finas', 'nariz_grande']
bill: ['hombre', 'barba', 'pelirrojo', 'ojos_marrones', 'orejas_grandes', 'mofletes', 'mejillas_sonrosadas', 'calva', 'boca_pequenha', 'nariz_pequenha']
anita: ['mujer', 'pelo_largo', 'pelo_rubio', 'ojos_marrones', 'boca_pequenha', 'mofletes', 'mejillas_sonrosadas', 'raya_al_medio', 'nariz_pequenha']
robert: ['hombre', 'cara_triste', 'pelo_castanho', 'ojos_azules', 'orejas_grandes', 'nariz_grande', 'raya_al_lado', 'cara_alargada', 'mofletes', 'mejillas_sonrosadas']
anne: ['mujer', 'pelo_corto', 'pendientes', 'pelo_negro', 'ojos_marrones', 'boca_pequenha', 'nariz_grande']
sam: ['hombre', 'gafas', 'calva', 'pelo_blanco', 'canas', 'ojos_marrones', 'boca_pequenha', 'nariz_pequenha']
tom: ['hombre', 'gafas', 'calva', 'pelo_negro', 'ojos_azules', 'boca_pequenha', 'cara_alargada', 'nariz_pequenha']
susan: ['mujer', 'pelo_largo', 'pelo_blanco', 'canas', 'ojos_marrones', 'labios_gruesos', 'mofletes', 'mejillas_sonrosadas', 'nariz_pequenha', 'raya_al_lado']
max: ['hombre', 'bigote', 'pelo_negro', 'ojos_marrones', 'boca_grande', 'labios_gruesos', 'nariz_grande', 'orejas_grandes', 'pelo_corto']
'''

    assert out == resultado_esperado

@pytest.mark.caracteristica
def test_caracteristica():
    personajes = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    assert caracteristica(personajes) == 'labios_gruesos'

@pytest.mark.pregunta
def test_pregunta():
    personaje = eleccion_personaje()
    caract = caracteristica(lista)

    if pregunta(personaje, caract):
        assert True
    
@pytest.mark.eleccion_personaje
def test_eleccion_personaje():
    personaje_secreto = eleccion_personaje()

    if personaje_secreto in lista:
        assert True