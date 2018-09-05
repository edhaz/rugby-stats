# adapted from: https://www.idiotinside.com/2015/09/18/csv-json-pretty-print-python/

import json
import csv
import datetime


# read CSV file
def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file, format)


# convert csv data into json and write it
def write_json(data, json_file, format):
    with open(json_file, "w+") as file:
        if format == "pretty":
            file.write(json.dumps(data, sort_keys=False, indent=4, separators=(', ', ': '), ensure_ascii=False))
        else:
            file.write(json.dumps(data))


def run():
    file = 'tables.csv'
    json_file = 'rugby_table.json'
    dated_json = 'data_archive/rugby_table_{}.json'.format(datetime.date.today())
    read_csv(file, json_file, 'pretty')
    read_csv(file, dated_json, 'pretty')

