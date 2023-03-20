from ast import Num
from otree.api import *
from settings import SESSION_CONFIG_DEFAULTS, SESSION_CONFIGS, PARTICIPANT_FIELDS, LANGUAGE_CODE

author = "Nathaniel Lawrence, LEMMA, Université Panthéon-Assas"
doc = """
Berlin Numeracy Test
From: Cokely, E. T., Galesic, M., Schulz, E., Ghazal, S., & Garcia-Retamero, R. (2012).
Measuring risk literacy: The berlin numeracy test. Judgment and Decision Making, 7(1), 25–47. 
"""

if LANGUAGE_CODE == 'fr':
    from _static.lexicon_fr import Lexicon
else:
    from _static.lexicon_en import Lexicon


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if fr }} Oui {{ else }} Yes {{ endif }}
which_language = {'en': False, 'fr': False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


# Define constants here, in all-caps
class C(BaseConstants):
    NAME_IN_URL = 'bnt'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_QUESTIONS = 8 + 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

# define the questions a player must answer here


class Player(BasePlayer):
    # Numeracy
    num_1 = models.IntegerField(
        label=Lexicon.lex_num_1,
        min=0
    )
    num_2a = models.IntegerField(
        label=Lexicon.lex_num_2a,
        min=0
    )
    num_2b = models.IntegerField(
        label=Lexicon.lex_num_2b,
        min=0
    )
    num_3 = models.IntegerField(
        label=Lexicon.lex_num_3,
        min=0
    )
    # Response time
    responseTime_1 = models.FloatField(initial=0)
    responseTime_2a = models.FloatField(initial=0)
    responseTime_2b = models.FloatField(initial=0)
    responseTime_3 = models.FloatField(initial=0)

    # Numeracy Attitude
    numatt_1 = models.StringField(
        choices=[
            [1, '1 - {}'.format(Lexicon.lex_numatt_not_confident)],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5 - {}'.format(Lexicon.lex_numatt_confident)]
        ],
        label=Lexicon.lex_numatt_1,
        widget=widgets.RadioSelect
    )
    numatt_2 = models.StringField(
        choices=[
            [1, '1 - {}'.format(Lexicon.lex_numatt_not_confident)],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5 - {}'.format(Lexicon.lex_numatt_confident)]
        ],
        label=Lexicon.lex_numatt_2,
        widget=widgets.RadioSelect
    )
    numatt_3 = models.StringField(
        choices=[
            [1, '1 - {}'.format(Lexicon.lex_numatt_not_confident)],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5 - {}'.format(Lexicon.lex_numatt_confident)]
        ],
        label=Lexicon.lex_numatt_3,
        widget=widgets.RadioSelect
    )
    numatt_4 = models.StringField(
        choices=[
            [1, '1 - {}'.format(Lexicon.lex_numatt_not_confident)],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5 - {}'.format(Lexicon.lex_numatt_confident)]
        ],
        label=Lexicon.lex_numatt_4,
        widget=widgets.RadioSelect
    )

# FUNCTIONS


def creating_session(subsession: Subsession):
    session = subsession.session
    for player in subsession.get_players():
        player.participant.remunerated_questions = []


# PAGES
class BNT_Intro(Page):
    counter_questions = 0

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


class BNT_1(Page):
    form_model = 'player'
    form_fields = ['num_1', 'responseTime_1']

    counter_questions = BNT_Intro.counter_questions + 1

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(BNT_1.counter_questions / C.NUM_QUESTIONS * 100,),
            Lexicon=Lexicon,
            **which_language
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.num_1 == 25:
            player.participant.remunerated_questions.append(1)

        else:
            player.participant.remunerated_questions.append(0)
        return player.participant.remunerated_questions


class BNT_2a(Page):
    form_model = 'player'
    form_fields = ['num_2a', 'responseTime_2a']

    # Must subtract 1 from counter because of responseTime form_fields
    counter_questions = BNT_1.counter_questions + len(BNT_1.form_fields) - 1

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(BNT_2a.counter_questions / C.NUM_QUESTIONS * 100,),
            Lexicon=Lexicon,
            **which_language
        )

    @staticmethod
    def is_displayed(player):
        return player.num_1 != 25

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.num_2a == 30:
            player.participant.remunerated_questions.append(1)

        else:
            player.participant.remunerated_questions.append(0)
        return player.participant.remunerated_questions


class BNT_2b(Page):
    form_model = 'player'
    form_fields = ['num_2b', 'responseTime_2b']

    counter_questions = BNT_2a.counter_questions + len(BNT_1.form_fields) - 1

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(BNT_2b.counter_questions / C.NUM_QUESTIONS * 100,),
            Lexicon=Lexicon,
            **which_language
        )

    @staticmethod
    def is_displayed(player):
        return player.num_1 == 25

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.num_2b == 20:
            player.participant.remunerated_questions.append(1)

        else:
            player.participant.remunerated_questions.append(0)
        return player.participant.remunerated_questions


class BNT_3(Page):
    form_model = 'player'
    form_fields = ['num_3', 'responseTime_3']

    counter_questions = BNT_2b.counter_questions + len(BNT_2b.form_fields) - 1

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(BNT_3.counter_questions / C.NUM_QUESTIONS * 100,),
            Lexicon=Lexicon,
            **which_language
        )

    @staticmethod
    def is_displayed(player):
        if player.field_maybe_none('num_2a') is None:
            if player.num_2b != 20:
                return True

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.num_3 == 50:
            player.participant.remunerated_questions.append(1)

        else:
            player.participant.remunerated_questions.append(0)
        return player.participant.remunerated_questions


class NAtt(Page):
    form_model = 'player'
    form_fields = ['numatt_1', 'numatt_2', 'numatt_3', 'numatt_4']

    counter_questions = BNT_3.counter_questions + len(BNT_3.form_fields) - 1

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(NAtt.counter_questions / C.NUM_QUESTIONS * 100,),
            Lexicon=Lexicon,
            **which_language
        )


class Results(Page):
    counter_questions = NAtt.counter_questions + len(NAtt.form_fields)

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(Results.counter_questions / C.NUM_QUESTIONS * 100,),
            Lexicon=Lexicon,
            **which_language
        )


page_sequence = [
    BNT_Intro,
    BNT_1,
    BNT_2a,
    BNT_2b,
    BNT_3,
    NAtt,
    Results
]
