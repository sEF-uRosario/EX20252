from otree.api import *

author = 'Sara Neff'

doc = """
Cognitive Reflection Test as proposed by Frederick (2005), Journal of Economic Perspectives 19(4). 
Written with the help of oTree code from survey app.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Part3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    questions_correct = models.IntegerField(initial='0')
    crt_Q1 = models.IntegerField(
        label='''
            A bat and a ball cost $1.10 in total.
            The bat costs $1.00 more than the ball.
            How many cents does the ball cost?'''
    )
    crt_Q2 = models.IntegerField(
        label='''
            If it takes 5 machines 5 minutes to make 5 widgets, 
            how many minutes would it take 100 machines to make 100 widgets?
            '''

    )

    crt_Q3 = models.IntegerField(
        label='''
            In a lake, there is a patch of lily pads.
            Every day, the patch doubles in size.
            If it takes 48 days for the patch to cover the entire lake,
            how many days would it take for the patch to cover half of the lake?
            '''
    )


class Instructions(Page):
    pass


class Play(Page):
    form_model = 'player'
    form_fields = ['crt_Q1', 'crt_Q2', 'crt_Q3']


class End(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.crt_Q1 == 5:
            player.payoff += 50
            player.questions_correct += 1
        if player.crt_Q2 == 5:
            player.payoff += 50
            player.questions_correct += 1
        if player.crt_Q3 == 47:
            player.payoff += 50
            player.questions_correct += 1
        session = player.session
        pp = player.participant
        pp.questions_correct = player.questions_correct
        pp.payoff_part3 = player.payoff
        pp.payoff = pp.payoff_part1 + pp.payoff_part2 + pp.payoff_part3
        pp.payment_incentive = pp.payoff.to_real_world_currency(session)
        total_payoff = pp.payoff_plus_participation_fee()
        pp.payment_total = total_payoff.to_real_world_currency(session)


page_sequence = [Instructions, Play, End]


def custom_export(players):
    yield [
        'participant',
        'crt_1',
        'crt_2',
        'crt_3',
        'num_correct',
    ]
    for p in players:
        pp = p.participant
        yield [
            pp.code,
            p.crt_Q1,
            p.crt_Q2,
            p.crt_Q3,
            p.questions_correct,
        ]
