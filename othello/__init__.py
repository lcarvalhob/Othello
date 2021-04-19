import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='othello-v0',
    entry_point='othello.env:OthelloEnv')
