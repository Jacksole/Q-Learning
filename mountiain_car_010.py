import numpy as np

import gym

env = gym.make("MountainCar-v0")
state = env.reset()

done = False
while not done:
    action = 2
    new_state, reward, done, _ = env.step(action)
    print(reward, new_state)
    print(env.observation_space.high)
    print(env.observation_space.low)

q_table = np.random.uniform(
    low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))
