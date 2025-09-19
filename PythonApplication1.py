import random

historial = []
contador_id = 1
total_victorias = 0
total_Empates = 0


class Partida:
    def __init__(self, IDPartida, GanadorFinal, TableroFinal):
        self.IDpartida = int(IDPartida)
        self.GanadorFinal = GanadorFinal
        self.TableroFinal = [fila[:] for fila in TableroFinal]

    def MostrarResumen(self):
        print(f"ID partida: {self.IDpartida} ")
        print(f"Ganador: {self.GanadorFinal} ")
        print("Tablero Final:")
        for fila in self.TableroFinal:
            print(f"{fila}")
        

def ElBot():
    while True:
        PreguntaBot = input("¿Desea jugar contra el Bot? Y/N ")
        if PreguntaBot.lower() == "y":
            print("Jugando con el bot")
            return True
        elif PreguntaBot.lower() == "n":
            print("Modo dos jugadores")
            return False
        else:
            print("Ingrese un caracter válido")


def TableroBonito(Tablero):
    print(
        f"    0       1       2\n"
        f"0  {Tablero[0][0]}   ║   {Tablero[0][1]}   ║   {Tablero[0][2]}\n"
        f"  ═════╬═══════╬═══════\n"
        f"1  {Tablero[1][0]}   ║   {Tablero[1][1]}   ║   {Tablero[1][2]}\n"
        f"  ═════╬═══════╬═══════\n"
        f"2  {Tablero[2][0]}   ║   {Tablero[2][1]}   ║   {Tablero[2][2]}\n"
    )


def LineaHorizontal(Tablero):
    return any(fila[0] == fila[1] == fila[2] != " " for fila in Tablero)


def LineaVertical(Tablero):
    return any(Tablero[0][i] == Tablero[1][i] == Tablero[2][i] != " " for i in range(3))


def LineaDiagonal(Tablero):
    return (Tablero[0][0] == Tablero[1][1] == Tablero[2][2] != " ") or \
           (Tablero[0][2] == Tablero[1][1] == Tablero[2][0] != " ")


def Empate(Tablero):
    return all(casilla != " " for fila in Tablero for casilla in fila)


def Turno(jugador):
    return not jugador


def seleccionarSimbolo(jugador, BotActivo):
    if jugador == False:
        print("Turno del jugador 1:")
        return "X"
    elif jugador and BotActivo:
        print("Turno del Bot:")
        return "O"
    else:
        print("Turno del jugador 2:")
        return "O"


def jugarPartida(contador_id):
    Tablero = [[" ", " ", " "] for _ in range(3)]
    jugador = False
    hayGanador = False
    ganador = "Empate"
    BotActivo = ElBot()
    global total_victorias, total_empates

    print("Jugador 1 empieza:")
    TableroBonito(Tablero)

    while not hayGanador and not Empate(Tablero):
        try:
            if jugador and BotActivo:
                while True:
                    jugadaX = random.randint(0, 2)
                    jugadaY = random.randint(0, 2)
                    if Tablero[jugadaY][jugadaX] == " ":
                        break
            else:
                jugadaX = int(input("Ingrese la posición X (0-2): "))
                jugadaY = int(input("Ingrese la posición Y (0-2): "))
        except ValueError:
            print("Ingrese un número válido")
            continue

        if jugadaX not in [0, 1, 2] or jugadaY not in [0, 1, 2]:
            print("Esa posición no existe")
            continue

        if Tablero[jugadaY][jugadaX] != " ":
            print("Esa posición ya está ocupada")
            continue

        simbolo = seleccionarSimbolo(jugador, BotActivo)
        Tablero[jugadaY][jugadaX] = simbolo
        TableroBonito(Tablero)

        if LineaHorizontal(Tablero) or LineaVertical(Tablero) or LineaDiagonal(Tablero):
            hayGanador = True
            if simbolo == "X":
                ganador = "Jugador 1 (X)"
            elif BotActivo and simbolo == "O":
                ganador = "Bot"
            else:
                ganador = "Jugador 2 (O)"
            print(f"¡Ha ganado {ganador}!")
            global total_victorias
            total_victorias += 1
            break

        if Empate(Tablero):
            ganador = "Empate"
            print("¡Empate!")
            global total_Empates
            total_Empates+=1
            break

        jugador = Turno(jugador)

    return Partida(contador_id, ganador, Tablero)

while True:

    partida = jugarPartida(contador_id)
    historial.append(partida)
    contador_id += 1

    while True:
        print("\n--- Menú final ---")
        print("1. Ver resultado de esta partida")
        print("2. Seleccionar Partida Guardada (IDs y ganadores)")
        print("3. Jugar otra vez")
        print("4. Salir")
        print("5. Numero de Victorias y Empates")
        opcion = input("Elige una opción: ").strip()

        match opcion:
            case "1":
                historial[-1].MostrarResumen()
            case "2":
                if not historial:
                    print("No hay partidas guardadas.")
                else:
                    print("\nRegistro de Partidas (ID - Ganador):")
                    for p in historial:
                        print(f"  ID {p.IDpartida} - {p.GanadorFinal}")
                try:
                    id_buscar = int(input("Introduce el ID de la partida: "))
                except ValueError:
                    print("ID por número.")
                    continue
                encontrada = next((p for p in historial 
                                   if p.IDpartida == id_buscar), None)
                if encontrada:
                    encontrada.MostrarResumen()
                else:
                    print("No existe")

            case "3":
                 print("Iniciando nueva partida...\n")
                 break 
             
            case "4":
                print("SALIENDO")
                exit()
            case "5":
                print(f"Número de victorias: {total_victorias}")
                print(f"Número de Empates: {total_Empates}")
               
            case _:
                print("Opción no válida")
