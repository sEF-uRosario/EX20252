import random

from otree.api import *

doc = """
mpl experiment proposed by Holt/Laury (2002), American Economic Review 92(5). Uses oTree code from choice_list app.
"""

BLANK = ' '


class C(BaseConstants):
    NAME_IN_URL = 'Part2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    DECISIONS = 8
    TABLE_TEMPLATE = __name__ + '/table.html'


def read_csv():
    import csv

    f = open(__name__ + '/stimuli.csv', encoding='utf-8-sig')
    rows = list(csv.DictReader(f))

    return rows


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        stimuli = read_csv()
        for stim in stimuli:
            Trial.create(player=p, **stim)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    chose_lottery = models.BooleanField(initial=False)
    won_lottery = models.BooleanField(initial=False)
    for j in range(1, C.DECISIONS+1):
        locals()['mpl_' + str(j)] = models.BooleanField()


class Trial(ExtraModel):
    player = models.Link(Player)
    sure_payoff = models.CurrencyField()
    lottery_high = models.CurrencyField()
    lottery_low = models.CurrencyField()
    probability_percent = models.IntegerField()
    chose_lottery = models.BooleanField()
    is_selected = models.BooleanField(initial=False)


class Play(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(trials=Trial.filter(player=player))

    @staticmethod
    def live_method(player: Player, data):
        [trial] = Trial.filter(player=player, id=data['trial_id'])
        trial.chose_lottery = data['chose_lottery']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        choices = []
        for p in range(20, 100, 10):
            [trial] = Trial.filter(player=player, probability_percent=p)
            choices.append(trial.chose_lottery)
        player.mpl_1 = choices[0]
        player.mpl_2 = choices[1]
        player.mpl_3 = choices[2]
        player.mpl_4 = choices[3]
        player.mpl_5 = choices[4]
        player.mpl_6 = choices[5]
        player.mpl_7 = choices[6]
        player.mpl_8 = choices[7]
        pp = player.participant
        trials = Trial.filter(player=player)
        selected_trial = random.choice(trials)
        pp.random_round_part2 = int(selected_trial.probability_percent / 10 - 1)
        pp.lottery_percent = selected_trial.probability_percent
        selected_trial.is_selected = True
        player.chose_lottery = selected_trial.chose_lottery
        pp.chose_lottery = player.field_maybe_none('chose_lottery')
        if player.field_maybe_none('chose_lottery'):
            player.won_lottery = selected_trial.probability_percent > (random.randint(1, 100))
            pp.won_lottery = player.won_lottery
            if player.won_lottery:
                payoff = selected_trial.lottery_high
            else:
                payoff = selected_trial.lottery_low
        else:
            payoff = selected_trial.sure_payoff
        player.payoff = payoff
        pp.payoff_part2 = player.payoff


class Instructions(Page):
    pass


class End(Page):
    pass


page_sequence = [Instructions, Play, End]


def custom_export(players):
    yield [
        'participant',
        'mpl_1',
        'mpl_2',
        'mpl_3',
        'mpl_4',
        'mpl_5',
        'mpl_6',
        'mpl_7',
        'mpl_8'
    ]
    for p in players:
        pp = p.participant
        yield [
            pp.code,
            p.mpl_1,
            p.mpl_2,
            p.mpl_3,
            p.mpl_4,
            p.mpl_5,
            p.mpl_6,
            p.mpl_7,
            p.mpl_8
        ]
