from os import environ


SESSION_CONFIGS = [
    dict(
        name='search_experiment',
        display_name="Search Experiment",
        app_sequence=['instructions', 'search_app_a', 'search_app_b', 'search_app_c', 'mpl', 'crt', 'payment'],
        num_demo_participants=20,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['treatment', 'decision_turns_a',
                      'random_round_part1_a', 'payoff_part1_a',
                      'decision_turns_b', 'random_round_part1_b',
                      'payoff_part1_b', 'decision_turns_c',
                      'random_round_part1_c', 'payoff_part1_c',
                      'payoff_part1', 'random_round_part2',
                      'chose_lottery', 'lottery_percent',
                      'won_lottery', 'payoff_part2',
                      'questions_correct', 'payoff_part3',
                      'payment_incentive', 'payment_total']
SESSION_FIELDS = []

LANGUAGE_CODE = 'en'

REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '7090507088802'

INSTALLED_APPS = ['otree']
