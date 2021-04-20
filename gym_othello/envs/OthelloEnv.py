import numpy as np
import gym
from gym_othello.envs.othello_model.Othello import Othello
from gym_othello.envs.OthelloGUI import OthelloGUI
from gym.spaces import Discrete, Box
from gym.envs.classic_control import rendering
from gym.utils import seeding

import logging

logger = logging.getLogger(__name__)


class OthelloEnv(gym.Env):
    metadata = {'render.modes': ['humans', 'rgb_array']}

    def __init__(self):
        self.board_state = Othello()
        self.board_gui = OthelloGUI()
        self.start = self.board_gui.get_observation()
        self.viewer = None
        self.agent_colour = self.board_state.player1
        self.opponent = self.board_state.player2
        self.action_space = Discrete(len(self.board_state.get_board()) ** 2)
        self.observation_space = Box(low=0, high=255, shape=(self.board_gui.height, self.board_gui.width, 3),
                                     dtype=np.uint8)
        self.seed()
        self.reset()

    def step(self, action):
        reward = 0
        action = self.board_state.action_conversion(action)
        info = {}

        if len(self.board_state.valid_moves(self.agent_colour)) == 0:
            pass

        elif self.board_state.check_move(self.agent_colour, action[0], action[1]) == 0:
            done = True
            reward -= 1
            self.board_gui.game_over()
            observation = self.board_gui.get_observation()
            return observation, reward, done, info

        else:
            self.board_state.move(self.agent_colour, action[0], action[1])

        # Opponent tries to move
        self.board_state.opponent_move(self.opponent)

        self.board_gui.update_board_state(self.board_state)
        observation = self.board_gui.get_observation()

        if self.board_state.game_state():
            done = True
            if self.agent_colour == self.board_state.get_winner():
                reward += 1
            elif self.opponent == self.board_state.get_winner():
                reward -= 1
            self.board_gui.game_over()
            return observation, reward, done, info

    def render(self, mode='human', close='False'):
        img = self.board_gui.get_observation()
        if mode == 'human':
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
        elif mode == 'rgb_array':
            return img

    def reset(self):
        self.board_state = Othello()
        self.board_gui.update_board_state(self.board_state)
        observation = self.board_gui.get_observation()
        return observation

    def seed(self, seed=None):
        np_random, seed = seeding.np_random(seed)
        return [seed]
