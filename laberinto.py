import time
from proceso import *
import tkinter as tk
from tkinter import filedialog
import csv #importo la librería csv para los archivos
# Inicializa el cuadro de diálogo de Tkinter
root = tk.Tk()
root.withdraw()

# Abre el cuadro de diálogo para que el usuario seleccione un archivo
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

# Verifica si el usuario ha seleccionado un archivo
if file_path:
    with open(file_path, 'r') as File:
        reader = csv.reader(File, delimiter=';')
        # Inicializa la matriz del laberinto
        matriz_laberinto = []
        for fila in reader:
            fila_numeros = [int(valor) for valor in fila]
            # Agrega la fila a la matriz del laberinto
            matriz_laberinto.append(fila_numeros)

        # Ahora la variable 'matriz_laberinto' contiene los datos del archivo CSV seleccionado por el usuario
        print("Laberinto cargado correctamente.")
else:
    print("No se ha seleccionado ningún archivo.")
filaInicial = 0
columnaInicial = 0
contadorfilas = -1
for fila in matriz_laberinto:
    contadorfilas+=1
    contadorcolumnas = -1
    for elemento in fila:
        contadorcolumnas+=1
        if elemento==8:
            filaInicial = contadorfilas
            columnaInicial = contadorcolumnas
mate = Matematica()
mate.fichaInicio(matriz_laberinto,filaInicial,columnaInicial,"c")
lista = mate.listaposicionescamino #una lista para saber las posiciones del camino de salida encontrado
import pygame #instalado desde Python Packages
import sys #sirve para terminar la ejecución
pygame.init() #inicializando la librería
tamaño = (len(matriz_laberinto[0])*40,len(matriz_laberinto)*40) #valores del tamaño de la ventana
#decidí que cada elemento tendrá un cuadrado asignado de 80x80, por eso la operación
pantalla = pygame.display.set_mode(tamaño) #Se crea la ventana con el tamaño especificado
colorfondo = (221, 230, 237) #creo un nuevo color para el fondo
largocuadrado = 40
anchocuadrado = 40
def interfaz(matriz_laberinto):
    while True: #while sin salida inicialmente

            for evento in pygame.event.get(): #recorremos todos los eventos del pygame (clicks,movimientos)
                if evento.type == pygame.QUIT: #si el evento es salir (cerrar)
                    sys.exit() #termina la ejecución
            pantalla.fill(colorfondo) #le asigno a mi fondo el color creado
            # --------------------- ZONA DE DIBUJO ----------------------------#
            x = 0  # Posición inicial en el eje x
            y = 0  # Posición en el eje y
            for fila in range(len(matriz_laberinto)): #recorro las filas del laberinto
                for columna in range(len(matriz_laberinto[fila])): #recorro los elementos de cada fila
                    if matriz_laberinto[fila][columna] == 8: #si el elemento es 8 (inicio)
                        pygame.draw.rect(pantalla, (93, 156, 89), (x, y, largocuadrado, anchocuadrado))
                    if matriz_laberinto[fila][columna] == 1: #si el elemento es 1 (barrera)
                        pygame.draw.rect(pantalla, (0, 0, 0), (x, y, largocuadrado, anchocuadrado))
                    if matriz_laberinto[fila][columna] == 9: #si el elemento es 9 (salida)
                        pygame.draw.rect(pantalla, (223, 46, 56), (x, y, largocuadrado, anchocuadrado))
                    if matriz_laberinto[fila][columna] == "c": #si el elemento es -1 (recorrido)
                        pygame.draw.rect(pantalla, (100, 153, 233), (x, y, largocuadrado, anchocuadrado))
                    x += largocuadrado  # aumento la posicion en x para colocar el cuadrado al lado
                    # Si llegamos al final de la pantalla, mueve a la siguiente fila
                    if x >= pantalla.get_width():
                        x = 0  # Resetea la posición en x a la izquierda
                        y += anchocuadrado  # Muevo hacia abajo en el eje y

            # --------------------- ZONA DE DIBUJO ----------------------------#
            pygame.display.flip() #actualizar la pantalla (mostrará todos los ajustes)
            time.sleep(3)
            break  # Romper el bucle después de la pausa de 8 segundos
interfaz(matriz_laberinto)
interfaz(lista)
