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

initial = 200
intentos = 150
#### EMPECEMOS A IMPLEMENTAR EL Q-ALG
ptjs = []
max_p = []
'''
def jugada(env):
    action = random.sample(env.coord,1)
    return action[0]
'''
rewards_all = []
def jugar(initial):
    end = 0
    exploration_rate = 0.5
    for episode in range(initial):   
        valor, puesto = env.reset()
        reward_current = 0
        for j in range(intentos): # con 150 tuve 10/10
            # Exploration-exploitation trade-off
            exploration_rate_threshold = random.uniform(0, 1)
            if exploration_rate_threshold > exploration_rate:
                #action = np.argmax(q_table[state,:])
                action = "c3" 
                pass
            else:
                action = random.choice(env.coordenadas)            
            
            #action = jugada(coordis)
            valor, reward, puesto, info = env.step(action)
            if not puesto:
                reward = -5
                #print("###MALA###")
            if reward > 7:    
                print("reward:",reward)    
            reward_current += reward
            if tablero_listo(env.matriz):
                end +=1
                print("TERMINADO")
                puntaje = env.contar_puntos()
                ptjs.append(puntaje)
                break
        
        env.render()
        
        rewards_all.append(reward)
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
