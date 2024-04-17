# **Quién es quién**
Práctica del curso de especialización de IA y Big Data - IES de Teis (Bruno Álvarez Darriba)

Este proyecto consiste en establecer una estrategia propia para poder resolver una partida del juego conocido como **"Quién es quién"**, usando *Prolog* y *Python*. Prolog será utilizado para poder establecer la base de datos que vamos a usar a la hora de simular la partida, en la cual se establecerán los distintos personajes del panel y sus correspondientes características diferenciadoras. Python será empleado para todo el desarrollo y ejecución de los casos test (pytest).

## ¿**"Quién es quién"** juego de *Optimización* o *Búsqueda*?
Para poder primero decidir y defender una postura acerca de que tipo de problema es este que vamos a tratar, vamos a centrarnos en entender de que se trata cada uno de los problemas mencionados en el enunciado y sus principales diferencias: 

- **Problemas de optimización**: estos hacen referencia a aquellos problemas cuyo objetivo es encontrar el mejor estado según una función objetivo. En estos casos, no hay ningún tipo de \<test objetivo> ni tampoco \<coste de camino>.
Lo único importante es la configuración o estado final.

- **Problemas de búsquedas**: estos sin embargo hacen referencia a aquellos problemas los cuales han sido diseñados para explorar de manera sistemática los espacios de búsqueda, manteniendo en memoria uno o más caminos registrando los puntos que hayan sido explorados con anterioridad. Estos tipos de búsquedas son usados cuando importa el camino al objetivo. 


Como podemos observar, el problema con el que nos encontramos en el **"Quién es quién"** es claramente un problema de optimización. El objetivo principal de dicho juego es encontrar el personaje que le tocó a la otra persona en el menor número de preguntas posibles, por lo que el camino hasta llegar al resultado final de la partida nos da igual ya que lo que va a decidir quien gana es el hecho de hacer las mínimas preguntas y acertar el personaje. En otras palabras, buscamos minimizar la función objetivo que mide el número de preguntas necesarias para identificar al personaje. 