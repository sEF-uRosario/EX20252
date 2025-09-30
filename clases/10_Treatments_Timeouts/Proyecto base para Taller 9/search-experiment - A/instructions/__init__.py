import random
import itertools

from otree.api import *


author = 'Sara Neff'

doc = """
"""

BLANK = ' '


def get_decision_turns_a(treatment):
    # set of treatments: T = {1,2,3,4,5,6}
    # set of SSPs: S = {2,5,10} where s in S is an SSP with s decision turns
    # each participant plays each SSP once
    # each participant plays app_a first followed by app_b followed by app_c
    # each participant is assigned to one treatment t in T which varys order in which participant plays the SSPs
    # t: a,b,c = s,s',s'' means treatment t assigns SSP s to app_a, s' to app_b, and s'' to app_c
    #   1: a,b,c = 2,5,10
    #   2: a,b,c = 2,10,5
    #   3: a,b,c = 5,2,10
    #   4: a,b,c = 5,10,2
    #   5: a,b,c = 10,2,5
    #   6: a,b,c = 10,5,2
    if treatment == 1 or treatment == 2:
        x = 2
    else:
        if treatment == 3 or __________:
            x = 5
        else:
            x = 10
    return x


def get_decision_turns_b(treatment):
    if treatment == 3 or treatment == 5:
        x = 2
    else:
        if treatment == 1 or treatment == 6:
            x = 5
        else:
            x = 10
    return x


def get_decision_turns_c(treatment):
    if treatment == 4 or treatment == 6:
        x = 2
    else:
        if treatment == 2 or treatment == 5:
            x = 5
        else:
            x = 10
    return x


class C(BaseConstants):
    NAME_IN_URL = 'Part1_Instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    SQUARES = 16


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def creating_session(subsession: Subsession):
    treatments = itertools.cycle([1, 2, 3, 4, 5, 6])
    for p in subsession.get_players():
        p.symbol = 'X'

        # creating_session gets executed each round independently
        # and our experiment has apps which each have multiple rounds
        # to prevent treatment getting executed each app/round, we assign treatment at the participant level
        pp = p.participant
        pp.__________ = next(treatments)
        pp.decision_turns_a = get_decision_turns_a(pp.treatment)
        pp.decision_turns_b = get_decision_turns_b(pp.treatment)
        pp.decision_turns_c = get_decision_turns_c(pp.treatment)

        #
        p.DECISION_TURNS_A = pp.decision_turns_a
        p.DECISION_TURNS_B = pp.decision_turns_b
        p.DECISION_TURNS_C = pp.decision_turns_c
        p.decisions_remaining_a = p.DECISION_TURNS_A
        p.decisions_remaining_b = p.DECISION_TURNS_B
        p.decisions_remaining_c = p.DECISION_TURNS_C

        # grid values for instructions page
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

        # grid values for practice round of Task A
        p.value_0_a = random.randint(0, 100)
        p.value_1_a = random.randint(0, 100)
        p.value_2_a = random.randint(0, 100)
        p.value_3_a = random.randint(0, 100)
        p.value_4_a = random.randint(0, 100)
        p.value_5_a = random.randint(0, 100)
        p.value_6_a = random.randint(0, 100)
        p.value_7_a = random.randint(0, 100)
        p.value_8_a = random.randint(0, 100)
        p.value_9_a = random.randint(0, 100)
        p.value_10_a = random.randint(0, 100)
        p.value_11_a = random.randint(0, 100)
        p.value_12_a = random.randint(0, 100)
        p.value_13_a = random.randint(0, 100)
        p.value_14_a = random.randint(0, 100)
        p.value_15_a = random.randint(0, 100)

        # grid values for practice round of Task B
        p.value_0_b = random.randint(0, 100)
        p.value_1_b = random.randint(0, 100)
        p.value_2_b = random.randint(0, 100)
        p.value_3_b = random.randint(0, 100)
        p.value_4_b = random.randint(0, 100)
        p.value_5_b = random.randint(0, 100)
        p.value_6_b = random.randint(0, 100)
        p.value_7_b = random.randint(0, 100)
        p.value_8_b = random.randint(0, 100)
        p.value_9_b = random.randint(0, 100)
        p.value_10_b = random.randint(0, 100)
        p.value_11_b = random.randint(0, 100)
        p.value_12_b = random.randint(0, 100)
        p.value_13_b = random.randint(0, 100)
        p.value_14_b = random.randint(0, 100)
        p.value_15_b = random.randint(0, 100)

        # grid values for practice round of Task C
        p.value_0_c = random.randint(0, 100)
        p.value_1_c = random.randint(0, 100)
        p.value_2_c = random.randint(0, 100)
        p.value_3_c = random.randint(0, 100)
        p.value_4_c = random.randint(0, 100)
        p.value_5_c = random.randint(0, 100)
        p.value_6_c = random.randint(0, 100)
        p.value_7_c = random.randint(0, 100)
        p.value_8_c = random.randint(0, 100)
        p.value_9_c = random.randint(0, 100)
        p.value_10_c = random.randint(0, 100)
        p.value_11_c = random.randint(0, 100)
        p.value_12_c = random.randint(0, 100)
        p.value_13_c = random.randint(0, 100)
        p.value_14_c = random.randint(0, 100)
        p.value_15_c = random.randint(0, 100)


class Player(BasePlayer):
    board_state_a = models.LongStringField(initial=BLANK * C.SQUARES)
    board_state_b = models.LongStringField(initial=BLANK * C.SQUARES)
    board_state_c = models.LongStringField(initial=BLANK * C.SQUARES)
    symbol = models.StringField()
    DECISION_TURNS_A = models.IntegerField()
    DECISION_TURNS_B = models.IntegerField()
    DECISION_TURNS_C = models.IntegerField()
    decisions_remaining_a = models.IntegerField()
    decisions_remaining_b = models.IntegerField()
    decisions_remaining_c = models.IntegerField()
    decision_turn_a = models.IntegerField(initial='1')
    decision_turn_b = models.IntegerField(initial='1')
    decision_turn_c = models.IntegerField(initial='1')
    first_turn_a = models.BooleanField(initial=True)
    first_turn_b = models.BooleanField(initial=True)
    first_turn_c = models.BooleanField(initial=True)
    round_complete_a = models.BooleanField(initial=False)
    round_complete_b = models.BooleanField(initial=False)
    round_complete_c = models.BooleanField(initial=False)
    for j in range(0, C.SQUARES):
        locals()['value_' + str(j)] = models.IntegerField()
        locals()['value_' + str(j) + '_a'] = models.IntegerField()
        locals()['value_' + str(j) + '_b'] = models.IntegerField()
        locals()['value_' + str(j) + '_c'] = models.IntegerField()


class PracticeA(Page):
    @staticmethod
    def live_method(player: Player, data: dict):
        board = list(player.board_state_a)
        broadcast = {}
        if 'move' in data:
            move = data['move']

            if player.round_complete_a:
                return

            board[move] = player.symbol
            player.board_state_a = ''.join(board)
            player.decision_turn_a += 1
            player.decisions_remaining_a = player.DECISION_TURNS_A - player.decision_turn_a + 1
        if player.decision_turn_a > player.DECISION_TURNS_A:
            player.round_complete_a = True
        if player.decision_turn_a > 1:
            player.first_turn_a = False
        broadcast['board_state'] = board
        broadcast['decisions_remaining'] = player.decisions_remaining_a
        broadcast['first_turn'] = player.first_turn_a
        broadcast['round_complete'] = player.round_complete_a
        return {0: broadcast}


class PracticeB(Page):
    @staticmethod
    def live_method(player: Player, data: dict):
        board = list(player.board_state_b)
        broadcast = {}
        if 'move' in data:
            move = data['move']

            if player.round_complete_b:
                return

            board[move] = player.symbol
            player.board_state_b = ''.join(board)
            player.decision_turn_b += 1
            player.decisions_remaining_b = player.DECISION_TURNS_B - player.decision_turn_b + 1
        if player.decision_turn_b > player.DECISION_TURNS_B:
            player.round_complete_b = True
        if player.decision_turn_b > 1:
            player.first_turn_b = False
        broadcast['board_state'] = board
        broadcast['decisions_remaining'] = player.decisions_remaining_b
        broadcast['first_turn'] = player.first_turn_b
        broadcast['round_complete'] = player.round_complete_b
        return {0: broadcast}


class PracticeC(Page):
    @staticmethod
    def live_method(player: Player, data: dict):
        board = list(player.board_state_c)
        broadcast = {}
        if 'move' in data:
            move = data['move']

            if player.round_complete_c:
                return

            board[move] = player.symbol
            player.board_state_c = ''.join(board)
            player.decision_turn_c += 1
            player.decisions_remaining_c = player.DECISION_TURNS_C - player.decision_turn_c + 1
        if player.decision_turn_c > player.DECISION_TURNS_C:
            player.round_complete_c = True
        if player.decision_turn_c > 1:
            player.first_turn_c = False
        broadcast['board_state'] = board
        broadcast['decisions_remaining'] = player.decisions_remaining_c
        broadcast['first_turn'] = player.first_turn_c
        broadcast['round_complete'] = player.round_complete_c
        return {0: broadcast}


class Instructions(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # we can't manipulate variables (add and subtract) in template html code
        # instead we calculate new variables that are functions of existing template variables here
        # which will pass these new variables to the template
        pp = player.participant
        total_decisions_a = 5 * pp.decision_turns_a
        total_decisions_b = 5 * pp.decision_turns_b
        total_decisions_c = 5 * pp.decision_turns_c
        return dict(
            total_decisions_a=total_decisions_a,
            total_decisions_b=total_decisions_b,
            total_decisions_c=total_decisions_c
        )


class Begin(Page):
    pass


class End(Page):
    pass


page_sequence = [Begin, Instructions, PracticeA, PracticeB, PracticeC]
