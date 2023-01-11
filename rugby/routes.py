from flask import render_template
import datetime

from rugby import app, settings, database, collect_table
from rugby import db
from rugby.utils import get_current_season_string


@app.before_first_request
def setup():
    db.create_all()
    collect_table.main()


@app.route("/")
def index():
    teams = database.all_teams()
    table_data = [team.__dict__ for team in teams]
    table_headers = [
        "Place",
        "",
        "Team",
        "Played",
        "Won",
        "Lost",
        "Drawn",
        "For",
        "Against",
        "Difference",
        "Bonus",
        "Points"
    ]
    # last_updated = 
    return render_template(
        "index.html",
        table_data=table_data,
        table_headers=table_headers,
        logos=settings.TEAM_LOGOS,
        year=get_current_season_string(),
        updated=datetime.datetime.now(),
    )


"""
@app.route('/api/<year>/table/all')
def table_api(year):
    json_url = os.path.join(SITE_ROOT, "data", year, "rugby_table.json")
    try:
        api_data = json.load(open(json_url))
        return jsonify(api_data)
    except:
        return "Error, no data."


@app.route("/api/team/<team>")
def team_api(team):
    team = team.capitalize()
    for item in api_data:
        if item['Team'] == team:
            return jsonify(item)
    return 'No such team in the premiership!'
"""
