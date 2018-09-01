from flask import Flask, render_template

app = Flask(__name__)


data = []
with open('tables.csv', 'r') as fin:
    for i in fin:
        tmp = i[:-2].split(",")
        data.append(tmp[:-1])

@app.route("/")
def index():
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run()
