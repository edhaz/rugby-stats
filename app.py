from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

json_url = os.path.join(SITE_ROOT, "data_archive", "rugby_table.json")
api_data = json.load(open(json_url))
table_data = []
with open(SITE_ROOT + '/data_archive/tables.csv', 'r') as fin:
    for i in fin:
        print(i)
        tmp = i[:-1].split(",")
        print("tmp", tmp)
        table_data.append(tmp[:])


@app.route("/")
def rugby():
    """Shows table of rugby union premiership"""
    return render_template("index.html", data=table_data)


@app.route("/api/v1/table/all")
def table_api():
    return jsonify(api_data)


if __name__ == "__main__":
    app.run()
