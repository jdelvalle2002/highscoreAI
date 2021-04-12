import gym
import random
import numpy as np

from gym import spaces
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class CustomEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self):
    super(CustomEnv, self).__init__()

env = gym.make('CartPole-v0')

env.reset()
steps = 100
score_req = 35
initial = 500
def jugar():    
    for i_episode in range(steps):
        observation = env.reset()
        for t in range(100):
            env.render()
            print(observation)
            action = env.action_space.sample() # acción al azar
            observation, reward, done, info = env.step(action)
            #recibimos los resultados de la acción 
            if done:
                print(f"Episode finished after {t+1} timesteps")
                break
    env.close()

def model_data_preparation():
    training_data = []
    choices = []
    scores = []
    for game in range(initial):
        score = 0
        #game_memo = []
        previous = []
        for step in range(steps):
            env.render()
            if len(previous) == 0:
                action = random.randrange(0,2)
            else:    
                action = np.argmax(train_model.predict(previous.reshape(-1,len(previous))))
            
            choices.append(action)
            new_observation, reward, done, info = env.step(action)
            previous = new_observation
            score+=reward
            if done:
                break

    env.reset()
    scores.append(score)
    
    print(scores)
    print("Avg:",sum(scores)(len(scores)))
    return training_data

# algo de una red neuronal
def build_model(in_size,out_size):
    model = Sequential()
    model.add(Dense(128, input_dim=in_size, activation="relu"))
    model.add(Dense(52, activation="relu"))
    model.add(Dense(out_size, activation="linear"))
    model.compile(loss="mse", optimizer=Adam())
    return model

def train_model(t_data):
    x = np.array([i[0] for i in t_data]).reshape(-1,len(t_data[0][0]))
    y = np.array([i[1] for i in t_data]).reshape(-1,len(t_data[0][1]))
    model = build_model(in_size=len(x[0]),out_size=len(y[0]))
    model.fit(x,y,epochs=10)
    return model


d = model_data_preparation()

tt = train_model(d)
