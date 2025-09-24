from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'intercambio'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    SUELDO_EMPLEADO = 30
    SUELDO_EMPLEADOR = 70



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    intercambio = models.IntegerField(label='Ingrese el aporte que desea reconocerle a su empleado:')


class Player(BasePlayer):
    agree = models.BooleanField()
    correcta_empleado = models.IntegerField()
    fallos_empleado = models.IntegerField()
    payoff_complete = models.IntegerField()
    payoff_total = models.IntegerField()


def creating_session(self):
    for group in self.get_groups():
        for player in group.get_players():
            if (player.id_in_group == 1):
                player.agree = random.choice([True, False])
            else:
                player.agree = not player.get_others_in_group()[0].agree

# PAGES

class ResultsWaitPage_RE(WaitPage):
    pass

class Intercambio(Page):
    form_model = 'group'
    form_fields = ['intercambio']

    @staticmethod
    def is_displayed(player: Player):
        return player.agree 
    
    def vars_for_template(player: Player):
        empleado = next(p for p in player.group.get_players() if not p.agree)
        correcta_empleado = empleado.participant.vars.get('num_correct', 0)
        # Recibir los intentos fallidos
        
        return {
            'correcta_empleado': correcta_empleado,
            'fallos_empleado': fallos_empleado,
        }
    
    def before_next_page(player: Player, timeout_happened):
        pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        empleador = next(p for p in group.get_players() if p.agree)
        empleado = next(p for p in group.get_players() if not p.agree)

        empleado.payoff_complete = C.SUELDO_EMPLEADO + group.intercambio
        empleador.payoff_complete = C.SUELDO_EMPLEADOR - group.intercambio


class Results(Page):
    timeout_seconds = 15
    form_model = 'player'
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Sumar la ganancia del intercambio al acumulado oficial
        

    @staticmethod
    def vars_for_template(player: Player):
        payoff_complete = player.payoff_complete
        payoff_total = player.participant.payoff + cu(payoff_complete)
        return {
            'payoff_complete': payoff_complete,
            'payoff_total': payoff_total
        }


page_sequence = [ResultsWaitPage_RE, Intercambio, ResultsWaitPage, Results]
