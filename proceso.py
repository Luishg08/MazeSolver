class Matematica():
    listaposicionescamino = []
    def fichaInicio(self,laberinto,filaInicial,columnaInicial,jugadas):
        if self.juego(laberinto,filaInicial,columnaInicial,jugadas,False):
            print("Laberinto con solución")
        else:
            print("ouch")
    def juego(self,laberinto,x,y,jugadas,salida):
        solucion = False
        if(salida):
            print(laberinto)
            matriz_copiada = [fila[:] for fila in laberinto]
            self.retornarlaberintoresuelto(matriz_copiada)
            return True
        if (solucion!=True) and (x-1>=0) and (laberinto[x-1][y]==0 or laberinto[x-1][y]==9):
            if laberinto[x-1][y]==9:
                salida = True
            if laberinto[x-1][y]!=9:
                laberinto[x-1][y]=jugadas
            solucion=self.juego(laberinto,x-1,y,jugadas,salida)
            if laberinto[x-1][y]!=9:
                laberinto[x-1][y]=0
        if (solucion!=True) and (x+1< len(laberinto)) and ((laberinto[x+1][y]==0) or laberinto[x+1][y]==9):
            if laberinto[x+1][y]==9:
                salida = True
            if laberinto[x+1][y]!=9:
                laberinto[x+1][y]=jugadas
            solucion = self.juego(laberinto,x+1,y,jugadas,salida)
            if laberinto[x+1][y]!=9:
                laberinto[x+1][y]= 0
        if (solucion!=True) and (y+1< len(laberinto)) and ((laberinto[x][y+1]==0) or laberinto[x][y+1]==9):
            if laberinto[x][y+1]==9:
                salida = True
            if laberinto[x][y+1]!=9:
                laberinto[x][y+1]=jugadas
            solucion = self.juego(laberinto,x,y+1,jugadas,salida)
            if laberinto[x][y+1]!=9:
                laberinto[x][y+1]=0
        if (solucion!=True) and (y-1>0) and ((laberinto[x][y-1]==0) or laberinto[x][y-1]==9):
            if laberinto[x][y-1]==9:
                salida = True
            if laberinto[x][y-1]!=9:
                laberinto[x][y-1]=jugadas
            solucion = self.juego(laberinto,x,y-1,jugadas,salida)
            if laberinto[x][y-1]!=9:
                laberinto[x][y-1]=0
        return solucion

    def retornarlaberintoresuelto(self,lista):
        self.listaposicionescamino = lista