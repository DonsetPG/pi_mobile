import gym
import keyboard
import numpy        as np
import time 

from gym            import spaces

from camera_handler import PiCamera
from car            import Car 

WIDTH,HEIGHT,CHANNEL = 224,224,3
LATENCE_START = 2.0
TIME_STEP = 0.5
TIME_BETWEEN_EPISODE = 10

class CarEnv(gym.Env):
    metadata = {'render.modes' :['human']}

    def __init__(self):

        self.n_envs = 1 
        super(CarEnv,self).__init__()

        self.car = Car()
        self.camera = PiCamera(latence_start= LATENCE_START,width=WIDTH, height=HEIGHT)

        self.current_step = 0
        self.episode = 1
        self.current_chrono = time.now()

        self.time_step = TIME_STEP
        self.time_between_episode = TIME_BETWEEN_EPISODE

        self.action_space = spaces.MultiDiscrete([3,2])

        self.training = True 

        self.observation_space = spaces.Box(low=-1.0, high=1.0, shape=(WIDTH,HEIGHT,CHANNEL), dtype=np.float16)

    def _next_observation(self):

        obs = self.camera._get_current_video()
        return obs

    def _take_action(self,action):

        steering = action[0]
        speed = action[1]

        if steering == 0:
            self.car._reset_steer()
        elif steering == 1:
            self.car._steer_right()
        else: 
            self.car._steer_left()

        if speed == 0:
            self.car._fast_forward()
        else:
            self.car._slow_forward()

    def step(self,action):

        self._take_action(action)
        time.sleep(self.time_step)
        self.current_step += 1 

        if keyboard.is_pressed('s'):
            print('s pressed: Stopping episode because of a failure. You now have 30 seconds to replace the car.')
            print('This episode lasted for {} seconds'.format((time.now() - self.current_chrono)))
            print('Reward := {}'.format(-1))
            done = True
            reward = -1
        elif keyboard.is_pressed('e'):
            print('e pressed: Ending episode because of a success. You now have 30 seconds to replace the car.')
            print('This episode lasted for {} seconds'.format((time.now() - self.current_chrono)))
            done = True 
            reward = 10. - (time.now() - self.current_chrono)/100.
            print('Reward := {}'.format(reward))
        else:
            done = False
            reward = 0.1

        #####
        #% How to handle the reward computation?
        #####
        reward = None 

        obs = self._next_observation()
        if done: print('You can now move the car')
        return obs, reward, done, {}

    def reset(self):

        self.current_step = 0
        self.episode += 1 

        self.current_chrono = time.now()
        self.car = Car()
        time.sleep(self.time_between_episode)
        return self._next_observation()

