import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Othello-v0',
    entry_point='gym_othello.envs:OthelloEnv')

register(
    id='Classroom-v0',
    entry_point='gym_othello.envs:ClassroomEnv')
