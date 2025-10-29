from otree.api import Bot, Submission
from . import *

class PlayerBot(Bot):
    def play_round(self):
        yield Decision, {'choice': ''}

        yield Results
