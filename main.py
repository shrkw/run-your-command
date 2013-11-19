#!/bin/env python
# coding:utf-8$      

from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
app = Flask(__name__)
 
@app.route('/')
def hello():
    return render_template('index.html')
 
def j():
    return 'Hello Flask.'


@app.route('/j/<name>')
def hello_world(name):
  greet = "Hello %s from flask!" % name
  result = {
    "Result":{
      "Greeting": greet
      }
  }
  return jsonify(result)

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
