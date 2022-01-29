#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from flask import Flask
from flask import render_template, jsonify, make_response

from utils.translators.portuguese import num2ptbr
from utils.translators.chinese import num2chinese, chinese2pinyin


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/convert/<int:number>")
def converter(number):
    ptbr = num2ptbr(number)
    cn = num2chinese(number)
    pinyin = chinese2pinyin(cn)
    results = {
        'num': number,
        'ptbr': ptbr,
        'cn': cn,
        'pinyin': pinyin
    }
    res = make_response(jsonify(results), 200)
    logging.info(res)
    return res

if __name__ == "__main__":
    logging.info("Server started")
    app.run(threaded=True, port=5000)
