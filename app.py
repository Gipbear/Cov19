from flask import Flask
from flask import jsonify
from flask import render_template
from jieba.analyse import extract_tags
import numpy as np

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
    res = utils.get_c2_data()
    data = []
    res_num = []
    per_num = [0]
    per = []
    for tup in res:
        data.append({'name': tup[0], 'value': int(tup[1])})
        res_num.append(int(tup[1]))
    da = np.array(res_num)
    per_num.append(np.percentile(da, 25))
    per_num.append(np.median(da))
    per_num.append(np.percentile(da, 75))
    per_num.append(np.percentile(da, 95))
    for i in range(len(per_num) - 1):
        per.append({'start': per_num[i], 'end': per_num[i + 1]})
    per.append({'start': per_num[-1]})
    return jsonify({'data': data, 'per': per})


@app.route('/l1')
def get_l1_data():
    data = utils.get_l1_data()
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for a, b, c, d, e in data[7:]:
        day.append(a.strftime('%m-%d'))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({'day': day, 'confirm': confirm, 'suspect': suspect, 'heal': heal, 'dead': dead})


@app.route('/l2')
def get_l2_data():
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime('%m-%d'))
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({'day': day, 'confirm_add': confirm_add, 'suspect_add': suspect_add})


@app.route('/r1')
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k, v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({'city': city, 'confirm': confirm})


@app.route('/r2')
def get_r2_data():
    res = utils.get_r2_data()
    d = []
    for i, v in res:
        ks = extract_tags(i)
        for j in ks:
            if not j.isdigit():
                d.append({'name': j, 'value': v})
    return jsonify({'kws': d})


if __name__ == '__main__':
    app.run()
