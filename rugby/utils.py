from datetime import datetime


def get_current_season():
    today = datetime.now()
    current_year = int(str(today.year)[2:])
    if today.month > 6:
        return f"{current_year}{current_year + 1}"
    return f"{current_year - 1}{current_year}"


def get_current_season_string():
    current_season = get_current_season()
    return f"{current_season[:2]}-{current_season[2:]}"
