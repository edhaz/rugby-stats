#! /usr/bin/python3

from flask import Flask, render_template, jsonify, url_for, redirect
import json
import os
import datetime
import logos_urls
from update_time_getter import update_time_getter

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
CURRENT_YEAR = 2019


@app.route("/")
def index():
    return redirect(url_for('rugby_year', year=CURRENT_YEAR))


@app.route("/<year>")
def rugby_year(year):
    if year < str(2018) or year > str(CURRENT_YEAR):
        return "Not found."
    table_data = get_table_data(year)
    updated = update_time_getter(year)
    logos = logos_urls.team_logos
    return render_template("index.html", 
                        table_data=table_data, 
                        logos=logos, 
                        updated=updated,
                        year=int(year),
                        CURRENT_YEAR=int(CURRENT_YEAR),
                        next_year_short=int(year) - 2000 + 1
                        )


def get_table_data(year):
    table_data = []
    with open(SITE_ROOT + '/data/' + str(year) + '/tables.csv', 'r') as fin:
        for i in fin:
            tmp = i[:-1].split(",")
            table_data.append(tmp[:])
    return table_data


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


if __name__ == "__main__":
    app.run()
