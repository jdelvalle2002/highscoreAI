import random
import json
import gym
from gym import spaces
import pandas as pd
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding

class HighEnv(gym.Env):
    """An enviroment to play Highscore"""
    metadata = {'render.modes': ['human']}
    def __init__(self):
        self.puesto = True
        self.p = 0 # puntaje
        self.matriz = []
        self.msj = []
        self.coordenadas = ["a1","a2","a3","a4","a5","b1","b2","b3","b4","b5","c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5", "e1", "e2", "e3", "e4", "e5"]
        self.pa = 0 #puntaje anterior
        self.d = 0
    def dado(self):
        a = random.randint(1,6)
        b = random.randint(1,6)
        valor = a+b
        return valor        
    def reset(self):
        self.coordenadas = ["a1","a2","a3","a4","a5","b1","b2","b3","b4","b5","c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5", "e1", "e2", "e3", "e4", "e5"]
        self.pa = 0
        self.p = 0
        self.puesto = True
        xd = []
        a = [0,0,0,0,0]
        i = 0
        while i < 5:
            xd.append(a[:])
            i += 1
        self.matriz = xd
        return self.dado(), self.puesto

    def render(self):
        def fill(s):
            if len(s) < 2:
                return " "+s
            else:
                return s    
        t = self.matriz[:]
        top = "#"*16
        second = "    a  b  c  d  e"
        print(top)
        print(second)
        co = 1
        for l in t:
            for i in range(len(l)):
                f = lambda x : fill(str(x))
                c = l[i]
                l[i] = f(c)

            s = "|".join(l)
            s = str(co) + ") |"+s+"|"
            print(s)
            co += 1
        print(top)   
    def contar_puntos(self):

        tablero = self.matriz
        mensajes = []
        # funciones aux
        puntos = 0
        def escalas_7():
            lista = []
            for i in range(3,8):
                esc = range(i,i+5)
                lista.append(list(esc))
            return lista
        def escalas_no7():
            lista = []
            for i in [2,8]:
                esc = range(i,i+5)
                lista.append(list(esc))
            return lista
        def full_f(lista):
            full = False
            for x in lista:
                if lista.count(x) == 3 and x != 0:
                    for y in lista:
                        if lista.count(y) == 2 and y != 0:
                            full = True
            return full
        def five(lista):
            for el in lista:
                if lista.count(el) == 5 and el != 0:
                    return True
            return False
        def poker(lista):
            for el in lista:
                if lista.count(el) == 4 and el != 0:
                    return True
            return False
        def trio(lista):
            for el in lista:
                if lista.count(el) == 3 and el != 0:
                    return True
            return False                        
        def dospar(lista):
            full = False
            for x in lista:
                if lista.count(x) == 2 and x != 0:
                    for y in lista:
                        if lista.count(y) == 2 and x != y and (y != 0):
                            full = True
            return full
        def par(lista):
            for x in lista:
                if lista.count(x) == 2 and x != 0:
                    return True
            return False            
        e7 = escalas_7()
        en7 = escalas_no7()
        
        # filas
        quintetos = tablero[:]
        for i in range(5):
            columna = []
            for j in range(5):
                columna.append(tablero[j][i]) ##### .strip()
            quintetos.append(columna)    
        diag = []
        line = []
        line2 = []
        for i in range(5):
            p = tablero[i][i]#.strip()
            p2 = tablero[-(i+1)][i]#.strip()
            line.append(p)
            line2.append(p2)    
        diag.append(line)
        diag.append(line2)
        for fila in quintetos:
            f  = sorted(list(map(int,fila)))
            # ojo, acá importa el orden en q se llaman las funciones
            pts = 0
            if f in e7:
                pts = 8
                puntos += pts   
            elif f in en7:
                pts = 12
                puntos += pts
            elif full_f(f): # acá los full 
                pts = 8
                puntos += pts
            elif five(f):
                pts = 10
                puntos += pts
            elif poker(f):
                pts = 6
                puntos += pts
            elif trio(f):
                pts = 3
                puntos += pts
            elif dospar(f):
                pts = 3
                puntos += pts
            elif par(f):
                pts = 1
                puntos += pts
            m = f"La fila/columna {fila} suma {pts} pts"    
            mensajes.append(m)                   
        # diagonales
        for fila in diag:
            f  = sorted(list(map(int,fila)))
            # ojo, acá importa el orden en q se llaman las funciones
            pts = 0
            if f in e7:
                pts = 16
                puntos += pts   
            elif f in en7:
                pts = 24
                puntos += pts
            elif full_f(f): # acá los full 
                pts = 16
                puntos += pts
            elif five(f):
                pts = 20
                puntos += pts
            elif poker(f):
                pts = 12
                puntos += pts
            elif trio(f):
                pts = 6
                puntos += pts
            elif dospar(f):
                pts = 6
                puntos += pts
            elif par(f):
                pts = 2
                puntos += pts
            m = f"La diagonal {fila} suma {pts} pts"
            mensajes.append(m)

        self.msj = mensajes
        return puntos    
    def step(self,action):
        num = self.d
        col = action[0]
        fil = int(action[1])
        col = "abcde".find(col)
        #print("col",col,"fil",fil)
        if self.matriz[fil-1][col] != 0:
            self.puesto = False
        else:
            self.matriz[fil-1][col] = num
            self.puesto = True
            self.d = self.dado()
        p = self.contar_puntos()
        reward =  p-self.pa
        self.pa = self.contar_puntos()
        return self.d, reward, self.puesto, self.matriz 
    
    #######################################
