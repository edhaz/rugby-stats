#! /usr/bin/python3

from flask import Flask, render_template, jsonify
import json
import os
import logos_urls

app = Flask(__name__)

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
    logos = logos_urls.team_logos
    return render_template("index.html", data=table_data, logos=logos)


@app.route("/api/table/all")
def table_api():
    return jsonify(api_data)


@app.route("/api/team/<team>")
def team_api(team):
    team = team.capitalize()
    for item in api_data:
        if item['Team'] == team:
            return jsonify(item)
        else:
            return 'No such team in the premiership!'


if __name__ == "__main__":
    app.run()
