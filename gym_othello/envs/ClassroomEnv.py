import numpy as np
import gym
from gym_othello.envs.othello_model.Othello import Othello
from gym_othello.envs.OthelloGUI import OthelloGUI
from gym.spaces import Discrete, Box
from gym.utils import seeding

import logging

logger = logging.getLogger(__name__)


class InteractiveEnv(gym.Env):

    def __init__(self):
        self.board_state = Othello()
        self.board_gui = OthelloGUI()
        self.agent_colour = self.board_state.player2
        self.opponent = self.board_state.player1
        self.action_space = Discrete(len(self.board_state.get_board()) ** 2)
        self.observation_space = Box(low=0, high=255, shape=(self.board_gui.height, self.board_gui.width, 3),
                                     dtype=np.uint8)
        self.seed()
        self.reset()

    def step(self, action):
        reward = 0
        action = self.board_state.action_conversion(action)
        info = {}
        done = False

        # Player tries to move
        self.board_gui.get_player_move(self.opponent)
        self.board_gui.update_board_state(self.board_state)

        # Agents attempts a move
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
            self.board_gui.update_board_state(self.board_state)

        if self.board_state.game_state():
            done = True
            if self.agent_colour == self.board_state.get_winner():
                reward += 1
            elif self.opponent == self.board_state.get_winner():
                reward -= 1
            self.board_gui.game_over()

        observation = self.board_gui.get_observation()

        return observation, reward, done, info

    def render(self, custom_msg=None, close='False'):
        self.board_gui.draw_board()

    def reset(self):
        self.board_state = Othello()
        self.board_gui.update_board_state(self.board_state)
        observation = self.board_gui.get_observation()
        return observation

    def seed(self, seed=None):
        np_random, seed = seeding.np_random(seed)
        return [seed]
