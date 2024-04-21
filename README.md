# **Quién es quién**
Práctica del curso de especialización de IA y Big Data - IES de Teis (Bruno Álvarez Darriba)

Este proyecto consiste en establecer una estrategia propia para poder resolver una partida del juego conocido como **"Quién es quién"**, usando *Prolog* y *Python*. Prolog será utilizado para poder establecer la base de datos, en la cual se establecerán los distintos personajes del panel y sus correspondientes características diferenciadoras, y también para desarrollar todo el código que permita simular la ejecución del juego. Python será empleado para todo el desarrollo y ejecución de los casos test (pytest).

 * [¿**"Quién es quién"** juego de *Optimización* o *Búsqueda*?](#¿"Quién-es-quién"-juego-de-Optimización-o-Búsqueda?)

 * [Entorno del agente](#Entorno-del-agente)

 * [Algoritmo](#Algoritmo)

 * [Estrutura del agente](#Estructura-del-agente)
 
 * [Uso del paradigma de programación lógica](#Uso-del-paradigma-de-programación-lógica)

 * [Prolog para la representación de la base de datos](#Prolog-para-la-representación-de-la-base-de-datos)

 * [Bibliografía](#Bibliografía)


## ¿**"Quién es quién"** juego de *Optimización* o *Búsqueda*?
Para poder primero decidir y defender una postura acerca de que tipo de problema es este que vamos a tratar, vamos a centrarnos en entender de que se trata cada uno de los problemas mencionados en el enunciado y sus principales diferencias: 

- **Problemas de optimización**: estos hacen referencia a aquellos problemas cuyo objetivo es encontrar el mejor estado según una función objetivo. En estos casos, no hay ningún tipo de \<test objetivo> ni tampoco \<coste de camino>.
Lo único importante es la configuración o estado final.

- **Problemas de búsquedas**: estos sin embargo hacen referencia a aquellos problemas los cuales han sido diseñados para explorar de manera sistemática los espacios de búsqueda, manteniendo en memoria uno o más caminos registrando los puntos que hayan sido explorados con anterioridad. Estos tipos de búsquedas son usados cuando importa el camino al objetivo. 


Como podemos observar, el problema con el que nos encontramos en el **"Quién es quién"** es claramente un problema de optimización. El objetivo principal de dicho juego es encontrar el personaje que le tocó a la otra persona en el menor número de preguntas posibles, por lo que el camino hasta llegar al resultado final de la partida nos da igual ya que lo que va a decidir quien gana es el hecho de hacer las mínimas preguntas y acertar el personaje. En otras palabras, buscamos minimizar la función objetivo que mide el número de preguntas necesarias para identificar al personaje. 

## Entorno del agente

Entorno de tareas | Completamente / parcialmente Observable| Agentes | Determinista / Estocástico | Episódico / Secuencial | Estático / Dinámico | Discreto / Continuo
:---: | :---: | :---: | :---: | :---: | :---: | :---: |
 Quién es quién | Parcialmente observable | Multiagente | Determinista | - | Estático | Discreto |

 <br>
 
 - **Parcialmente observable:** los jugadores solo pueden ver su propio tablero, por lo que no conocen ni el tablero ni el personaje que tiene el rival el cual se tiene que adivinar descartando personajes de su propio tablero.

 - **Multiagente:** se trata de un agente multiagente ya que a la hora de estar jugando hay una relación directa con otro agente (a la hora de hacer las preguntas para poder descartar personajes en el tablero) pero no es adversario, la lucha es contra el propio juego, ya que el otro agente no está intentando minimizar tus acciones para poder lograr tu objetivo.

- **Determinista:** las preguntas que haces al otro agente van a tener respuestas concretas de si o no. No hay incertidumbre a la hora de responderlas.

- 

- **Estático:** es estático ya que a la hora de estar pensando la pregunta que le vas a hacer al otro agente ni el entorno, ni el tablero ni el personaje a adivinar cambia.

- **Discreto:** los agentes tienen un número finito de personajes en su tablero. Al igual que las caracteríticas de los personajes y las respuestas de las preguntas tienen un número finito de posibilidades.

## Algoritmo








## Estructura del agente










## Uso del paradigma de programación lógica
Este juego es un buen ejemplo de problema para ser resuelto mediante el uso de la programación lógica por varios motivos: 

- Tiene unas reglas claras y definidas, lo cual es perfecto para el uso de reglas lógicas para modelar su funcionamiento. 

- Las preguntas se formulan en términos de características y relaciones entre los personajes, estas se pueden representar fácilmente mediante predicados y relaciones en lógica.

- El juego implica sacar conclusiones a partir de las respuestas a las preguntas planteadas por el otro agente. Por ejemplo, si se pregunta: "¿Tu personaje tiene el pelo negro?" y el otro agente recibe te da una respuesta negativa, entonces se puede deducir que todos los personajes con pelo negro pueden ser descartados de las opciones posibles. Dichas deducciones se expresan en la programación lógica mediante reglas.

- Toda la información sobre las características de cada personaje se puede almacenar y expresar mediante el uso de reglas lógicas también, ya que el propio paradigma es capaz de analizar, razonar y tratar dicha información para responder cualquier tipo de pregunta a cerca de la misma (devolviendo valores booleanos, personajes que cumplen las preguntas formuladas, listas...).

- Permite también aumentar las características y/o los personajes sin ningún tipo de problema de forma fácil e intuitiva. Aparte de que también es una buena opción para tratar con una cantidad razonable de información.


## Prolog para la representación de la base de datos


## Bibliografía
@dfleta. "quienesquien". _github_. https://github.com/dfleta/quienesquien.git

Inteligencia Artificial un enfoque moderno, 2da Ed (Stuart Russell y Peter Norvig)


