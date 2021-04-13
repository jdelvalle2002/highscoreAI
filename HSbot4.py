
from HighAI.High_AI.envs.high_env import HighEnv
from ray import tune
from ray.rllib.agents.dqn import DQNTrainer
from ray.tune.registry import register_env

#import High_AI

register_env("high_v1", HighEnv)

config = {
    "env": "high_v1"
}

stop = {
    "info/num_steps_trained": 100000
    }



tune.run("DQN", config=config, stop=stop)


