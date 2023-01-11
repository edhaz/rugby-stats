from os import path, environ

SITE_ROOT = path.join(path.realpath(path.dirname(__file__)), "2019")
ROOT_DIR = path.realpath(path.dirname(__file__))
DATA_DIR = path.join(ROOT_DIR, "data")
DATABASE_PATH = path.join(DATA_DIR, "rugby.db")

CURRENT_SEASON = 2122

DATA_URL = "https://www.bbc.co.uk/sport/rugby-union/english-premiership/table"
LOGO_URL_PREFIX = "https://cdn.soticservers.net/tools/images/teams/logos/RUGBY969513/d/"

SECRET_KEY = environ.get("APP_SECRET_KEY")

TEAM_LOGOS = {
    "bath": "BATH5627.svg",
    "bristol": "BRIS5950.svg",
    "exeter chiefs": "EXET7458.svg",
    "gloucester": "GLOU5573.svg",
    "harlequins": "HARL5785.svg",
    "leicester tigers": "LEIC7782.svg",
    "newcastle falcons": "NEWC1579.svg",
    "northampton saints": "NORT3133.svg",
    "sale": "SALE8393.svg",
    "saracens": "SARA4298.svg",
    "wasps": "LOND5443.svg",
    "worcester warriors": "WORC9240.svg",
    "london irish": "LOND1618.svg",
}
