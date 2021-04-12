import gym
import random
import numpy as np

from gym import spaces

import High_AI

from time import time


start = time()


env = gym.make('high-v0')

initial = 5000

ptjs = []
max_p = []
def jugar(initial):

    for i in range(initial):   
        env.reset()
        reward = 0
        for j in range(25):
            env.d = env.dado()
            n = random.randint(0,len(env.pos_lugares)-1)
            action = env.pos_lugares.pop(n)
            pos, r, done, tablero = env.step(action)
            reward += r
        #print(t.msj)
        #print(f"Jugada {i}: {p} puntos")
        #t.print_tablero()
        ptjs.append(reward)
        if reward == max(ptjs):
            max_p.append([reward,env.msj,i])

jugar(initial) 
max_p.sort(key= lambda x:-x[0])
mejor = max_p[0]
peor = min(ptjs)
line = ""
for lines in mejor[1]:
    line += lines + "\n"


#print("Puntajes: ")

#print(ptjs)
print("N:", initial)
print(f"Promedio: {sum(ptjs)/len(ptjs)}")
print(f"Máximo: {max(ptjs)}")
print(f"Mínimo: {peor}")
print(line)
print(f"Tiempo: {time()-start}")
