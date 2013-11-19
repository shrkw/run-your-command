#!/bin/env python
# coding:utf-8$      

import subprocess
from subprocess import check_output, CalledProcessError
from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
app = Flask(__name__)

illegal_chars = " '\"/\:;|&`()$<>*?{}[]"
illegal_chars_t = tuple(illegal_chars)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    name = request.args.get("name")
    out = None
    err = None
    for i in illegal_chars_t:
        if i in name:
            err = "Illegal characters: " + illegal_chars + ", Found illegal character in: " + name
            break

    if err == None:
        try:
            out = check_output(["/bin/sh", "scripts/run.sh", name], stderr=subprocess.STDOUT)
        except CalledProcessError as e:
            out = e.returncode
            err = e.output

    result = {
        "Result":{
            "out": out,
            "err": err,
        }
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
