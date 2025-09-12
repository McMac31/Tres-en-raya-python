print("Tres en raya")
jugador = False
hayGanador = False

Tablero = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

def TableroBonito():
    print(
        f"    0       1       2\n"
        f"0  {Tablero[0][0]}   |   {Tablero[0][1]}   |   {Tablero[0][2]}\n"
        f"  -----------------------\n"
        f"1  {Tablero[1][0]}   |   {Tablero[1][1]}   |   {Tablero[1][2]}\n"
        f"  -----------------------\n"
        f"2  {Tablero[2][0]}   |   {Tablero[2][1]}   |   {Tablero[2][2]}")

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
        print("El Turno del jugador 1 fue: ")
    else:
        simbolo = "O"
        print("El Turno del jugador 2 fue: ")
    return simbolo

print("Jugador 1 Empieza:")
TableroBonito()

while hayGanador == False:
    try:
       
        jugadaX = int(input("Ingrese la posicion X a jugar (0-2): "))
        jugadaY = int(input("Ingrese la posicion Y a jugar (0-2): "))
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
        ganador = "Primer jugador (X)" if simbolo == "X" else "Segundo jugador (O)"
        print(f"¡Ha ganado el {ganador}!")
        break

    if Empate():
        print("Empate")
        break

    jugador = Turno(jugador)
