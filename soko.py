"""
    Author: Salvador Hernández Mendoza
    Date: 19/Mar/2024
    Items:

    0 -> Personaje
    1 -> Caja
    2 -> Meta
    3 -> Pared
    4 -> Piso
    5 -> Personaje_meta
    6 -> Caja_meta

    Description: Juego Sokoban en una versión retro para consola.
"""


class Soko:
    """
    Clase base para jugar sokoban
    """

    def __init__(self):
        """_summary_:Configura el juego"""
        # Define el mapa de juego
        self.mapa = [
            [3, 3, 3, 3, 3, 3, 3],
            [3, 4, 4, 4, 4, 4, 3],
            [3, 4, 0, 4, 1, 2, 3],
            [3, 4, 4, 4, 4, 4, 3],
            [3, 3, 3, 3, 3, 3, 3],
        ]

        # Se define la posicion inicial del personaje
        # Nota: Para cada nivel la posición inicial del personaje cambia
        self.personaje_columna = 2
        self.personaje_fila = 2

        # Se definen los elementos del juego como constantes
        self.PERSONAJE = 0
        self.CAJA = 1
        self.META = 2
        self.PARED = 3
        self.PISO = 4
        self.PERSONAJE_META = 5
        self.CAJA_META = 6

    def imprimir_mapa(self):
        """_summary_: Este método imprime el mapa del juego como un array bidimensional"""
        for filas in self.mapa:
            print(filas)  # Imprime cada fila del mapa

    def derecha(self):
        """_summary_: Este metodo es llamado cuando se va a mover a la derecha
        en este caso se utilizaran los numeros de los elementos, a diferencia de
        el metodo izquierda, en el que se usaran las CONSTANTES.
        Ambas formas son validas

        Nota: Cada if es un movimiento, en total hay 44 movimientos validos en el juego.
        Nota: Revisar el README con la lista de movimientos validos.
        """
        # Movimiento 5 (personaje, piso) -> (piso, personaje):
        # [0,4] -> [4,0]
        if (
            self.mapa[self.personaje_fila][self.personaje_columna]
            == 0  # posicion personaje
            and self.mapa[self.personaje_fila][self.personaje_columna + 1]
            == 4  # posicion del piso
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Donde estaba el piso pone al personaje
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            # Actualiza la posicion del personaje
            self.personaje_columna += 1
        # PROGRAMAR LOS SIGUIENTES ELIF QUE CORRESPONDEN A CADA UNO DE LOS MOVIMIENTOS VALIDOS
        # Movimiento 6 (personaje, meta) -> (piso, personaje_meta):
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == self.PERSONAJE
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == self.META
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = self.PERSONAJE_META
            self.personaje_columna += 1
        # Movimiento 7 (personaje, caja) -> (caja, personaje):
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == self.PERSONAJE
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == self.CAJA
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = self.CAJA
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = self.PERSONAJE
            self.personaje_columna += 1
        # TODO: Movimiento 8
        # TODO: Movimiento 9
        # TODO: Movimiento 10
        # TODO: Movimiento 11
        # TODO: Movimiento 12
        # TODO: Movimiento 13
        # TODO: Movimiento 14
        # TODO: Movimiento 15
        # TODO: Movimiento 16

    def izquierda(self):
        """_summary_: Este método se llama cuando se va a mover a la izquierda
        en este caso se utilizan las CONSTANTES definidas con los elementos del juego
        en lugar de los números de los elementos, es otra forma de programar cada uno de los movimientos.

        Nota: Cada if es un movimiento, en total hay 44 movimientos validos en el juego.
        Nota: Revisar el README con la lista de movimientos validos.
        """
        # Movimiento 17 (personaje, piso) -> (piso, personaje)::
        # [4,0] -> [0,4]
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == self.PERSONAJE
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == self.PISO
        ):
            # Donde estaba el piso pone al personaje
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = self.PERSONAJE
            # Donde estaba el personaje pone el piso
            self.mapa[self.personaje_fila][self.personaje_columna] = self.PISO
            # Actualiza la posicion del personaje
            self.personaje_columna -= 1
        # PROGRAMAR LOS SIGUIENTES ELIF QUE CORRESPONDEN A CADA UNO DE LOS MOVIMIENTOS VALIDOS
        # TODO: Movimiento 18
        # TODO: Movimiento 19
        # TODO: Movimiento 20
        # TODO: Movimiento 21
        # TODO: Movimiento 22
        # TODO: Movimiento 23
        # TODO: Movimiento 24
        # TODO: Movimiento 25
        # TODO: Movimiento 26
        # TODO: Movimiento 27
        # TODO: Movimiento 28

    def abajo(self):
        """_summary_: Metodo que se llama cuando se mueve hacia abajo"""
        # Movimiento 41 (personaje, piso) -> (piso, personaje)::
        # [0] -> [4]
        # [4] -> [0]
        if (
            self.mapa[self.personaje_fila][self.personaje_columna]
            == 0  # Posicion del personaje
            and self.mapa[self.personaje_fila + 1][self.personaje_columna]
            == 4  # Posicion del piso
        ):
            # Donde estaba el personaje se pone un piso
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Donde estaba el piso se pone al personaje
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            # Se actualiza la fila del personaje
            self.personaje_fila += 1
        # PROGRAMAR LOS SIGUIENTES ELIF QUE CORRESPONDEN A CADA UNO DE LOS MOVIMIENTOS VALIDOS
        # TODO: Movimiento 42
        # TODO: Movimiento 43
        # TODO: Movimiento 44
        # TODO: Movimiento 45
        # TODO: Movimiento 46
        # TODO: Movimiento 47
        # TODO: Movimiento 48
        # TODO: Movimiento 49
        # TODO: Movimiento 50
        # TODO: Movimiento 51
        # TODO: Movimiento 52

    def arriba(self):
        """_summary_: Metodo que se llama cuando se mueve hacia arriba"""
        # Movimiento 29 (personaje, piso) -> (piso, personaje)::
        # [4] -> [0]
        # [0] -> [4]
        if (
            self.mapa[self.personaje_fila][self.personaje_columna]
            == 0  # Posicion del personaje
            and self.mapa[self.personaje_fila - 1][self.personaje_columna]
            == 4  # Posicion del piso
        ):
            # Donde estaba el personaje se pone un piso
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Donde estaba el piso se pone al personaje
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            # Se actualiza la fila del personaje
            self.personaje_fila -= 1
        # PROGRAMAR LOS SIGUIENTES ELIF QUE CORRESPONDEN A CADA UNO DE LOS MOVIMIENTOS VALIDOS
        # TODO: Movimiento 30
        # TODO: Movimiento 31
        # TODO: Movimiento 32
        # TODO: Movimiento 33
        # TODO: Movimiento 34
        # TODO: Movimiento 35
        # TODO: Movimiento 36
        # TODO: Movimiento 37
        # TODO: Movimiento 38
        # TODO: Movimiento 39
        # TODO: Movimiento 40

    def jugar(self):
        """_summary_: Metodo que controla el flujo del juego, lee las indicaciones
        del usuario y llama a los movimientos correspondientes
        """
        while True:
            # Imprime el mapa
            self.imprimir_mapa()
            # Pide al usuario el movimiento
            movimiento = input("Selecciona el movimiento: ")
            # Moverse a la derecha
            if (
                movimiento == "d" or movimiento == "D"
            ):  # La letra d indida movimiento a la derecha
                self.derecha()  # Invoca al método derecha
            # Moverse a la izquerda
            elif movimiento in [
                "a",
                "A",
            ]:  # Otra forma para validar minúsculas ó mayúsculas
                self.izquierda()  # Invoca al método izquierda
            # Moverse hacia abajo
            elif movimiento == "s":
                self.abajo()  # Invoca al método abajo
            # Moverse hacia arriba
            elif movimiento == "w":
                self.arriba()  # Invoca al método arriba


soko = Soko()  # Crea un objeto de la clase Soko
soko.jugar()  # Llama al método jugar
