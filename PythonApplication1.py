
import random
print("Tres en raya")
jugador = False
hayGanador = False


Tablero = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]


def ElBot():
    while True:
            PreguntaBot= input("Desea jugar contra el Bot? Y/N ")
            if PreguntaBot == "Y" or PreguntaBot== "y":
                print("Jugando con el bot")
                return True
            elif PreguntaBot =="N" or PreguntaBot== "n":
                print("Cambiando a modo dos jugadores... ")
                return False
            else:
                print("Ingrese un caracter valido")


   



def TableroBonito():
    print(
        f"    0       1       2\n"
        f"0  {Tablero[0][0]}   ║   {Tablero[0][1]}   ║   {Tablero[0][2]}\n"
        f"  ═════╬═══════╬═══════\n"
        f"1  {Tablero[1][0]}   ║   {Tablero[1][1]}   ║   {Tablero[1][2]}\n"
        f"  ═════╬═══════╬═══════\n"
        f"2  {Tablero[2][0]}   ║   {Tablero[2][1]}   ║   {Tablero[2][2]}\n")

def verTablero():
    for casilla in Tablero:
        print(casilla)

def LineaHorizontal():
    for fila in Tablero:
        if fila[0] == fila[1] == fila[2] != " ":
            return True
    return False

def LineaVertical():
    for i in range(3):
        if Tablero[0][i] == Tablero[1][i] == Tablero[2][i] != " ":
            return True
    return False

def LineaDiagonal():
    if Tablero[0][0] == Tablero[1][1] == Tablero[2][2] != " ":
        return True
    if Tablero[0][2] == Tablero[1][1] == Tablero[2][0] != " ":
        return True
    return False

def Empate():
    for casilla in Tablero:
        for i in casilla:
            if i == " ":
                return False
    return True

def Turno(jugador):
    return not jugador

def seleccionarSimbolo(jugador):
    if jugador == False:
        simbolo = "X"
        print("El Turno del jugador 1 fue: \n")
    elif jugador and BotActivo == True:
        simbolo="O"
        print("El turno del Bot fue: \n")
    else:
        simbolo = "O"
        print("El Turno del jugador 2 fue: \n")
    return simbolo

BotActivo=ElBot()


print("Jugador 1 Empieza:")
TableroBonito()



while hayGanador == False:
    try:
        if jugador and BotActivo:
            while True:
                            jugadaX= random.randint(0,2)
                            jugadaY= random.randint(0,2)
                            if Tablero[jugadaY][jugadaX]== " ":
                                break
        else:
       
            jugadaX = int(input("Ingrese la posicion X a jugar (0-2): \n"))
            jugadaY = int(input("Ingrese la posicion Y a jugar (0-2): \n "))
    except ValueError:
            print("Ingrese un valor numerico")
            continue

    if jugadaX > 2 or jugadaX < 0 or jugadaY > 2 or jugadaY < 0:
        print("Esa posicion no existe")
        continue

    if Tablero[jugadaY][jugadaX] != " ":
        print("Esa posicion ya esta ocupada")
        continue

    simbolo = seleccionarSimbolo(jugador)
    Tablero[jugadaY][jugadaX] = simbolo

    TableroBonito()

    if LineaHorizontal() or LineaVertical() or LineaDiagonal():
        hayGanador = True
        if simbolo == "X":
            ganador="Primer jugador (X) "
        elif BotActivo and simbolo=="O":
            ganador="Bot "
        else:
            ganador="Segundo jugador (O)"
        print(f"¡Ha ganado el {ganador}!")
        TableroBonito()
        break

    if Empate():
        print("Empate")
        break

    jugador = Turno(jugador)
