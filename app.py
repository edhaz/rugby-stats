#! /usr/bin/python3

from flask import Flask, render_template, jsonify, url_for, redirect
from flask_moment import Moment
import json
import os
import datetime
import logos_urls
from update_time_getter import update_time_getter

app = Flask(__name__)
moment = Moment(app)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
now = datetime.datetime.now()
CURRENT_YEAR = now.year


@app.route("/")
def index():
    return redirect(url_for('rugby_year', year=CURRENT_YEAR))


@app.route("/<year>")
def rugby_year(year):
    """Shows table of rugby union premiership from given year"""
    if year < str(2018) or year > str(CURRENT_YEAR):
        return "Not found."
    table_data = []
    with open(SITE_ROOT + '/data_archive/' + str(year) + '/tables.csv', 'r') as fin:
        for i in fin:
            tmp = i[:-1].split(",")
            table_data.append(tmp[:])
    # Leave room for images in the table data
    for item in table_data[1:]:
        item.insert(1, 'i')
    updated = update_time_getter(year)
    logos = logos_urls.team_logos
    return render_template("index.html", data=table_data, logos=logos, updated=updated)

"""
@app.route('/api/<year>/table/all')
def table_api(year):
    json_url = os.path.join(SITE_ROOT, "data_archive", year, "rugby_table.json")
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


if __name__ == "__main__":
    app.run()