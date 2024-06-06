import safe_mo_mujoco as gym

import json
import os
import time


env = gym.make("Ant-v4")
# env = gym.make("Ant-v4", render_mode="human") # render environments

observation, info = env.reset(seed=42)
for i in range(1000):
    action = env.action_space.sample()
    observation, reward1, reward2, cost, terminated, truncated, info = env.step(action)
    # env.render() # render environments
    if terminated or truncated:
        observation, info = env.reset()
env.close()
