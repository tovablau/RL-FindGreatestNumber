
import gym
import numpy as np
from gym import error, spaces, utils  # are we using spaces?
from gym.utils import seeding
import scipy as sp
from scipy.stats import poisson

class Find_Greatest_Env:

  def __init__(self):
      self.min = 0
      self.max = 5000

      self.low = np.array([self.min, 0])
      self.high = np.array([self.max, 50000])


      self.observation_space = spaces.Box(self.low, self.high, dtype=np.float32)

      self.action_space = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -2, -5, -4, -3, 200, 45, 67, 92, 100, 30]


  def step(self, action):
      assert 0 <= action <len(self.action_space) , "%r (%s) invalid" % (action, type(action))

      num, round = self.state
      done = bool(round > 200)
      num = self.action_space[action]
      round += 1


      if -10 < num <= 0: reward = 0
      elif  0 < num <= 10: reward = 10
      elif 10 < num <= 20: reward = 20
      elif 20 < num <= 50: reward = 50
      elif 50 < num <= 100: reward = 70
      elif 100 < num <= 150: reward = 100
      elif 150 < num <= 200: reward = 200

      self.state = (num, round)
      return np.array(self.state), reward, done, {}

  def reset(self):
      self.state = np.array([-100, 0])
      return np.array(self.state)



