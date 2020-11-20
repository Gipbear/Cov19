from flask import Flask
from flask import jsonify
from flask import render_template

import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/time')
def get_time():
    return utils.get_time()


@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({'confirm': data[0], 'suspect': data[1], 'heal': data[2], 'dead': data[3]})


@app.route('/c2')
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        # print(tup)
        res.append({'name': tup[0], 'value': int(tup[1])})
    return jsonify({'data': res})


if __name__ == '__main__':
    app.run()
