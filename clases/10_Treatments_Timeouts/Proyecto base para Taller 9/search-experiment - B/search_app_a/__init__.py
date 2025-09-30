import random
import time

from otree.api import *

author = 'Sara Neff'

doc = """
Sequential Search Decision Problem (SSP). Written with the help of oTree code from tictactoe app.
"""

BLANK = ' '


class C(BaseConstants):
    NAME_IN_URL = 'Part1_TaskA'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    SQUARES = 16


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        pp = p.participant
        p.DECISION_TURNS = pp.decision_turns_a
        p.decisions_remaining = pp.decision_turns_a
        p.symbol = 'X'
        p.value_0 = random.randint(0, 100)
        p.value_1 = random.randint(0, 100)
        p.value_2 = random.randint(0, 100)
        p.value_3 = random.randint(0, 100)
        p.value_4 = random.randint(0, 100)
        p.value_5 = random.randint(0, 100)
        p.value_6 = random.randint(0, 100)
        p.value_7 = random.randint(0, 100)
        p.value_8 = random.randint(0, 100)
        p.value_9 = random.randint(0, 100)
        p.value_10 = random.randint(0, 100)
        p.value_11 = random.randint(0, 100)
        p.value_12 = random.randint(0, 100)
        p.value_13 = random.randint(0, 100)
        p.value_14 = random.randint(0, 100)
        p.value_15 = random.randint(0, 100)


class Player(BasePlayer):
    board_state = models.LongStringField(initial=BLANK * C.SQUARES)
    symbol = models.StringField()
    DECISION_TURNS = models.IntegerField()
    square = models.IntegerField()
    max_known_value = models.IntegerField()
    decisions_remaining = models.IntegerField()
    decision_turn = models.IntegerField(initial='1')
    search = models.BooleanField(initial=True)
    first_turn = models.BooleanField(initial=True)
    round_complete = models.BooleanField(initial=False)
    all_rounds_complete = models.BooleanField(initial=False)
    for j in range(0, C.SQUARES):
        locals()['value_' + str(j)] = models.IntegerField()


class Choices(ExtraModel):
    player = models.Link(Player)
    round = models.IntegerField()
    turn = models.IntegerField()
    max_known_value = models.IntegerField()
    choice_value = models.IntegerField()
    choice_square = models.IntegerField()
    search = models.BooleanField()
    time = models.FloatField()


class Play(Page):

    @staticmethod
    def vars_for_template(player: Player):
        next_round = player.round_number + 1
        return dict(
            next_round=next_round,
        )

    @staticmethod
    def live_method(player: Player, data: dict):
        board = list(player.board_state)
        broadcast = {}
        if 'move' in data:
            move = data['move']

            if player.round_complete:
                return

            if player.first_turn:
                player.max_known_value = player.value_0
                if move == 0:
                    player.search = False
            else:
                if not board[move] == BLANK:
                    player.search = False

            board[move] = player.symbol
            player.board_state = ''.join(board)
            player.square = move
        if 'value' in data:
            value = data['value']

            click_time = time.time()

            Choices.create(player=player,
                           round=player.round_number,
                           turn=player.decision_turn,
                           max_known_value=player.max_known_value,
                           choice_value=value,
                           choice_square=player.square,
                           search=player.search,
                           time=click_time,
                           )

            player.payoff += value
            player.decision_turn += 1
            x = player.max_known_value
            player.max_known_value = max(x, value)
            player.decisions_remaining = player.DECISION_TURNS - player.decision_turn + 1
        if player.decision_turn > player.DECISION_TURNS:
            player.round_complete = True
        if player.round_number == C.NUM_ROUNDS:
            player.all_rounds_complete = True
        if player.decision_turn > 1:
            player.first_turn = False
        player.search = True
        broadcast['board_state'] = board
        broadcast['decisions_remaining'] = player.decisions_remaining
        broadcast['first_turn'] = player.first_turn
        broadcast['round_complete'] = player.round_complete
        broadcast['all_rounds_complete'] = player.all_rounds_complete
        return {0: broadcast}

    @staticmethod
    def before_next_page(player: Player, __________):
        pp = player.participant
        if player.round_number == C.NUM_ROUNDS:
            random_round_part1_a = random.randint(1, C.NUM_ROUNDS)
            pp.random_round_part1_a = random_round_part1_a
            player_in_selected_round = player.in_round(random_round_part1_a)
            pp.payoff_part1_a = player_in_selected_round.payoff


class Begin(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class End(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Begin, Play, End]


def custom_export(players):
    yield [
        'participant',
        'treat',
        'T',
        'round',
        't',
        'x_bar',
        'action',
        'square',
        'payoff',
        'time',
    ]
    for p in players:
        pp = p.participant
        for choices in Choices.filter(player=p):
            yield [
                pp.code,
                pp.treatment,
                pp.decision_turns_a,
                choices.round,
                choices.turn,
                choices.max_known_value,
                choices.search,
                choices.choice_square,
                choices.choice_value,
                choices.time,
            ]
