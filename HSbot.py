import gym
import random
import numpy as np

from gym import spaces

import High_AI

from time import time


start = time()

def tablero_listo(tablero):
    for line in tablero:
        if 0 in line:
            return False
    return True


env = gym.make('high-v0')

initial = 5

ptjs = []
max_p = []
coordis = env.pos_lugares[:]
rewards = []
def jugada(env):
    action = random.sample(coordis,1)
    return action[0]


def jugar(initial):
    end = 0
    for episode in range(initial):   
        valor, puesto = env.reset()
        reward = 0
        for j in range(250): # con 150 tuve 10/10
            action = jugada(coordis)
            valor, r, puesto, info = env.step(action)
            
            if not puesto:
                r = -5
                #print("###MALA###")
            print("reward:",r)    
            reward += r
            if tablero_listo(env.matriz):
                end +=1
                print("TERMINADO")
                puntaje = env.contar_puntos()
                ptjs.append(puntaje)
                break
        
        env.render()
        
        rewards.append(reward)
        #if reward == max(ptjs):
        #    max_p.append([reward,env.msj])
    return end

e = jugar(initial) 
#max_p.sort(key= lambda x:-x[0])
#mejor = max_p[0]
peor = min(ptjs)
line = ""
#for lines in mejor[1]:
#    line += lines + "\n"


#print("Puntajes: ")

#print(ptjs)
print("N:", initial)
print("terminados:", e)
print(f"Promedio: {sum(ptjs)/len(ptjs)}")
print(f"Máximo: {max(ptjs)}")
#print(f"Mínimo: {peor}")
#print(line)
print(f"Tiempo: {time()-start}")
