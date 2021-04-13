import gym
import random
import numpy as np
from ray import tune
from ray.rllib.agents.dqn import DQNTrainer

import High_AI

from time import time



start = time()


env = gym.make('high-v0')

initial = 100
intentos = 150
ptjs = []
max_p = []

rewards_all = []
def jugar(initial):
    end = 0
    exploration_rate = 0.99
    for episode in range(initial):   
        valor, puesto = env.reset()
        reward_current = 0
        for j in range(intentos): # con 150 tuve 10/10
            # Exploration-exploitation trade-off
            exploration_rate_threshold = random.uniform(0, 1)
            if exploration_rate_threshold > exploration_rate:
                #action = np.argmax(q_table[state,:])
                action = (2,2) 
                pass
            else:
                action = (random.randint(0,4), random.randint(0,4))            
            
            #action = jugada(coordis)
            valor, reward, done, puesto  = env.step(action)
            ''''
            if reward > 7:    
                print("reward:",reward)
            '''
            '''
            if done:
                env.render()
            '''        
            reward_current += reward
        
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
