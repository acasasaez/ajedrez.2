tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
fichero = open ("./aje.txt","w", encoding="utf-8")
fichero.write(tablero_inicial)
fichero.close()
tablero = []
def movimiento():
    for i in tablero_inicial.split("\n"):
        tablero.append(i.split("\t"))
    fichero
    for i in tablero:
        fichero.write("/t".join(i) + "n")
    fichero.close()
    