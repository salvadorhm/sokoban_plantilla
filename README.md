# SOKOBAN

## 1. Objetivo

### 1.1 General

Programar el juego Sokoban en una versión retro para consola.

### 1.2 Específicos

- Aplicar los conocimientos básicos de programación orientada a objetos con Python (Clases, Objetos, Métodos, Variables, Arrays, Bucles, Leer desde teclado, Decisiones, etc.).

- Utilizar ingeniería de software para analizar, diseñar y desarrollar el juego.

- Utilizar Kanban para dar seguimeinto a las actividades a realizar ToDo, Doing, Done.

- Utilizar Hitos (Milestones) para cada una de las etapas del desarrollo.

- Documentar el código generado.

## 2. Reglas del juego

El juego sokoban consiste en recorrer un mapa en forma de laberinto para empujar cajas que estan repartidas en el mapa, hacia puntos determinados por las metas, y tiene las siguientes reglas:

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja hacia arriba, abjo, izquierda o derecha.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar todas las cajas sobre las metas.
5. Cada nivel tiene distinto número de cajas y metas.
6. El nivel de dificultad no está determinado necesariamente por la cantidad de cajas y metas.

## 3. Elementos del juego

Sokoban tiene 2 partes principales de juego, el mapa donde se va jugar y los elementos (personaje, cajas, metas, paredes y piso).

### 3.1 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando números para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

````code
mapa = [
            [3,3,3,3,3,3,3],
            [3,4,4,4,4,4,3],
            [3,4,0,4,1,2,3],
            [3,4,4,4,4,4,3],
            [3,3,3,3,3,3,3]
        ]
````

### 3.2 Lista de elementos

- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Pesonaje meta
- 6 - Caja meta

## 4. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover:

- a -> Izquierda
- s -> Derecha
- w -> Arriba
- s -> Abajo

Nota: El proceso es que se muestra el mapa y se solicita al usuario que escriba la letra hacia donde se quiere mover, despúes de colocar la letra se preciona enter y se actualiza el mapa, este proceso se repite de forma infinita.


## 5. Funciones a implementar

Para llevar un mejor control del avance del desarrollo llenar Kanban con los siguientes elementos (ToDo, Doing y Done).

### 5.1 Funciones generales
| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | - | - |
| 1. | Repetir el juego hasta terminar el nivel. | - | - |
| 2. | Imprimir mapa.| - | - |
| 3. | Leer el movimiento. | - | - |
| 4. | Evaluar el movimiento del usuario. | - | - |

### 5.2 Derecha

Ejemplo de movimientos Inicio y Fin:

- Personaje, Espacio [0,4] -> Espacio, Personaje [4,0] |


| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, espacio  | - | [      ] | [     ] | - |
| 6. | Personaje, meta  | - | [      ] | [      ] |- |
| 7. | Personaje, caja, espacio | - | [      ] | [      ] | - |
| 8. | Personaje, caja,  meta | - | [      ] | [      ] | - |
| 9. | Personaje, caja_meta, espacio | - | [] | [] | - |
| 10. |Personaje, caja_meta, meta | - | [] | [] | - |
| 11. | Personaje_meta, espacio | - | [] | [] | - |
| 12. | Personaje_meta, meta | - | [] | [] | - |
| 13. | Personaje_meta, caja, espacio | - | [] | [] | - |
| 14. | Personaje_meta, caja, meta | - | [] | [] | - |
| 15. | Personaje_meta, caja_meta, espacio | - | [] | [] | - |
| 16. | Personaje_meta, caja_meta, meta | - | [] | [] | - |

### 5.3 Izquierda

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 17. | Personaje, espacio | - | [] | [] | - |
| 18. | Personaje, meta | - | [] | [] | - |
| 19. | Personaje, caja, espacio | - | [] | [] | - |
| 20. | Personaje, caja, meta | - | [] | [] | - |
| 21. | Personaje, caja_meta, espacio | - | [] | [] | - |
| 22. | Personaje, caja_meta, meta | - | [] | [] | - |
| 23. | Personaje_meta, espacio | - | [] | [] | - |
| 24. | Personaje_meta, meta | - | [] | [] | - |
| 25. | Personaje_meta, caja, espacio | - | [] | [] | - |
| 26. | Personaje_meta, caja, meta | - | [] | [] | - |
| 27. | Personaje_meta, caja_meta, espacio | - | [] | [] | - |
| 28. | Personaje_meta, caja_meta, meta | - | [] | [] | - |

### 5.4 Arriba

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 29. | Personaje, espacio | - | [][] | [][] | - |
| 30. | Personaje, meta | - | [][] | [][] | - |
| 31. | Personaje, caja, espacio | - | [][] | [][] | - |
| 32. | Personaje, caja, meta | - | [][] | [][] | - |
| 33. | Personaje, caja_meta, espacio | - | [][] | [][] | - |
| 34. | Personaje, caja_meta, meta | - | [][] | [][] | - |
| 35. | Personaje_meta, espacio | - | [][] | [][] | - |
| 36. | Personaje_meta, meta | - | [][] | [][] | - |
| 37. | Personaje_meta, caja, espacio | - | [][] | [][] | - |
| 38. | Personaje_meta, caja, meta | - | [][] | [][] | - |
| 39. | Personaje_meta, caja_meta, espacio | - | [][] | [][] | - |
| 40. | Personaje_meta, caja_meta, meta | - | [][] | [][] | - |

### 5.5 Abajo

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 41. | Personaje, espacio | - | [][] | [][] | - |
| 42. | Personaje, meta | - | [][] | [][] | - |
| 43. | Personaje, caja, espacio | - | [][] | [][] | - |
| 44. | Personaje, caja, meta | - | [][] | [][] | - |
| 45. | Personaje, caja_meta, espacio | - | [][] | [][] | - |
| 46. | Personaje, caja_meta, meta | - | [][] | [][] | - |
| 47. | Personaje_meta, espacio | - | [][] | [][] | - |
| 48. | Personaje_meta, meta | - | [][] | [][] | - |
| 49. | Personaje_meta, caja, espacio | - | [][] | [][] | - |
| 50. | Personaje_meta, caja, meta | - | [][] | [][] | - |
| 51. | Personaje_meta, caja_meta, espacio | - | [][] | [][] | - |
| 52. | Personaje_meta, caja_meta, meta | - | [][] | [][] | - |

### 5.6 Determina si se completo el nivel

Está función determina si todas las cajas estan en una meta, cuando esto sucede se debe cargar el siguiente nivel de juego.

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado (Esto sucede cuando todas las cajas estan sobre las metas), SI el nivel esta terminado cargar el siguiente nivel (Los niveles de juego estarán en archivos de texto independiente). | - | - |
| 54. | Reiniciar el mapa (Con la letra r, se vuelve a cargar el nivel que se esta jugando) | - | - |

### 5.7 Función extra

Como parte del reto de programar un Sokoban, hay que agregar alguna función especial al juego, como por ejemplo bajo ciertas condiciones empujar 2 cajas, colocar un temporizador por nivel, etc.

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 55. | Función adicional o powerup (descripción). | - | - |

