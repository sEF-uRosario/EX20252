from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'juego_decision'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2

class Subsession(BaseSubsession): pass
class Group(BaseGroup): pass

class Player(BasePlayer):
    choice = models.StringField(choices=['A', 'B'])
    payoff_points = models.IntegerField()

class Decision(Page):
    form_model = 'player'
    form_fields = ['choice']

    def before_next_page(player, timeout_happened):
        if player.choice == '':
            player.payoff_points = 100
        else:
            if player.round_number == 2:
                player.payoff_points = 200
            else:
                player.payoff_points = 50

class Results(Page):
    def vars_for_template(player):
        return dict(pago=player.payoff_points)

page_sequence = [Decision, Results]
