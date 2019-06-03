import json
import os
import logos_urls
from flask import render_template, jsonify, request, flash
from app.update_time_getter import update_time_getter
from app import app, data_controller

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# Create usable data for table
json_url = os.path.join(SITE_ROOT, "data_archive", "rugby_table.json")
api_data = json.load(open(json_url))
table_data = []
with open(SITE_ROOT + '/data_archive/tables.csv', 'r') as fin:
    for i in fin:
        tmp = i[:-1].split(",")
        table_data.append(tmp[:])

# Leave room for images in the table data
for item in table_data[1:]:
    item.insert(1, 'i')


@app.route("/")
def rugby():
    """Shows table of rugby union premiership"""
    updated = update_time_getter()
    logos = logos_urls.team_logos
    return render_template("index.html", data=table_data, logos=logos, updated=updated)


@app.route("/api/table/all")
def table_api():
    return jsonify(api_data)


@app.route("/api/team/<team>")
def team_api(team):
    team = team.capitalize()
    for item in api_data:
        if item['Team'] == team:
            return jsonify(item)
    return 'No such team in the premiership!'


@app.route("/admin/add/<team>")
def add(team):
    return data_controller.add_team(team)


@app.route("/admin/add/stats", methods=['GET', 'POST'])
def add_stats():
    if request.method == 'POST':
        place = request.form['place']
        round_number = request.form['round_number']
        team_id = request.form['team_id']
        data_controller.add_stats(round_number, place, team_id)
        flash('Data added!' + place + round_number + team_id)
        return render_template("add_stats.html")
    else:
        return render_template("add_stats.html")



if __name__ == "__main__":
    app.run()
