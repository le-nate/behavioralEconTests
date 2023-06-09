from os import environ

SESSION_CONFIGS = [
    dict(
        name='BRET',
        display_name='Bomb risk elicitation task',
        app_sequence=['BRET'],
        num_demo_participants=1,
    ),
    dict(
        name='lossAversion',
        display_name='Loss aversion',
        app_sequence=['lossAversion'],
        num_demo_participants=1,
    ),
    dict(
        name='Numeracy',
        display_name='Berlin Numeracy Test',
        app_sequence=['Numeracy'],
        num_demo_participants=1,
    ),
    dict(
        name='riskPreferences',
        display_name='Holt & Laury',
        app_sequence=['riskPreferences'],
        num_demo_participants=1,
    ),
    dict(
        name='timePreferences',
        display_name='Time Preferences',
        app_sequence=['timePreferences'],
        num_demo_participants=1,
    ),
    dict(
        name='wisconsin',
        display_name='Wisconsin card sorting task',
        app_sequence=['wisconsin'],
        num_demo_participants=1,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'fr'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '7146632425768'
