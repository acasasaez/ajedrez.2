tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
a = open ("./aje.txt","w", encoding="utf-8")
a.write(tablero_inicial)
a.close
tablero = []
def movimiento(fichero):
    for i in tablero_inicial.split("\n"):
        tablero.append(i.split("\t"))
    fichero = open ("./aje.txt","w", encoding="utf-8")
    for i in tablero_inicial:
        fichero.write("/t".join(i) + "/n")
    fichero.close()
    mov = 0
    while True :
        continuar = input("¿Desea hacer otro movimiento?, si o no: ")
        if continuar != "si":
                break
        else:
            fila_inicial = int(input("Introduzca la fila de la ficha que desea mover: "))
            columna_inicial = int(input("Introduzca la columna de la ficha que desea mover: "))
            fila_final = int(input("Introduzca la fila a la que desea mover la ficha: "))
            columna_final = int(input("Introduzca la columna a la que desea mover la ficha: "))
            tablero[fila_final -1][columna_final - 1] = tablero [fila_inicial-1][columna_inicial-1]
            tablero [fila_inicial-1][columna_inicial-1] = " "
        fichero = open ("./aje.txt","w", encoding="utf-8")
        fichero.write ("Movimiento" + str(mov) + "/n")
        fichero.close()
    return
movimiento("aje.txt")
n = int(input("Qué tablero desea comprobar?"))
def tablero (fichero, n):
    fichero = open ("./aje.txt","r", encoding="utf-8")
    tableros = fichero.read().split("/n")
    for i in tableros [n*9:n*9+8]:
        print (i)
    return
tablero ("aje.txt",n)