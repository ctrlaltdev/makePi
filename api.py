#!/bin/env python3

from flask import Flask
from flask import Response
from flask import json
from pidigits import piGenerator

app = Flask(__name__)

def getPiDecimals(length = 100):
    piGen = piGenerator()
    next(piGen)
    piDec = '3.'

    for i in range(length):
        piDec += str(next(piGen))

    return piDec

def createRes(content, status = 200):
    headers = { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json; charset=utf-8' }
    res = Response(response=json.dumps(content), status=status, headers=headers)
    return res

@app.route('/<length>')
def getPiN(length):
    if (int(length) > 10000):
        return createRes({ 'error': 'Awww, come on, that\'s too many decimals for a little server' }, 400)
    return createRes({ 'pi': getPiDecimals(int(length)) })

@app.route('/')
def getPi():
    return createRes({ 'pi': getPiDecimals() })


if __name__ == '__main__':
    app.run()
