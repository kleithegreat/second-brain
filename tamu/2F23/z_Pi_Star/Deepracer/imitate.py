"""This is a simple example demonstrating how to clone the behavior of an expert.

Refer to the jupyter notebooks for more detailed examples of how to use the algorithms.
"""

import gym
import numpy as np
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import DummyVecEnv

from imitation.algorithms import bc
from imitation.data import rollout
from imitation.data.wrappers import RolloutInfoWrapper
from stable_baselines3.common import torch_layers
from stable_baselines3.common import policies
from imitation.data.types import TransitionsMinimal
import csv
import cv2 as cv

from model_car_env import ModelCar

env = ModelCar()
rng = np.random.default_rng(0)

def linear_schedule(initial_value: float):
    """
    Linear learning rate schedule.

    :param initial_value: Initial learning rate.
    :return: schedule that computes
      current learning rate depending on remaining progress
    """
    def func(progress_remaining: float) -> float:
        """
        Progress will decrease from 1 (beginning) to 0.

        :param progress_remaining:
        :return: current learning rate
        """
        return initial_value

    return func

import torch.nn as nn
policyy = policies.ActorCriticCnnPolicy(env.observation_space, env.action_space, linear_schedule(0.001), activation_fn=nn.ReLU)

# observations, acts = [], []
# with open('labels.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in  reader:
#
#         imagee = cv.imread('./data/'+row[0])
#         imagee = cv.cvtColor(imagee, cv.COLOR_BGR2GRAY)
#         scale_percent = 25  # percent of original size
#         width = int(imagee.shape[1] * scale_percent / 100)
#         height = int(imagee.shape[0] * scale_percent / 100)
#         dim = (width, height)
#         imagee = cv.resize(imagee, dim, interpolation=cv.INTER_AREA)
#
#         imagee = np.expand_dims(imagee, axis=0)
#         observations.append(imagee)
#         acts.append([float(row[1]), float(row[2])])
#
#
# observations = np.asarray(observations)
# acts = np.asarray(acts)
# transitions = TransitionsMinimal(obs=observations,  acts=acts, infos=acts)



# bc_trainer = bc.BC(
#     observation_space=env.observation_space,
#     action_space=env.action_space,
#     demonstrations=transitions,
#     rng=rng,
#     policy=policyy,
#     ent_weight=0.0,
#     batch_size=128
# )

# print("Training a policy using Behavior Cloning")
# n_epochs = 0
# while n_epochs < 100000:
#     bc_trainer.train(n_epochs=100)
#     n_epochs += 100
#     bc_trainer.save_policy('bc_policy'+str(n_epochs)+'.imitate')

bc_trained = bc.reconstruct_policy('bc_policy2200.imitate')
reward, _ = evaluate_policy(
    bc_trained,  # type: ignore[arg-type]
    env,
    n_eval_episodes=1,
    render=True,
)
# print(f"Reward after training: {reward}")