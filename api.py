#!/bin/env python3

from flask import Flask
from pidigits import piGenerator

app = Flask(__name__)

def getPiDecimals(length = 100):
    piGen = piGenerator()
    next(piGen)
    piDec = '3.'

    for i in range(length):
        piDec += str(next(piGen))

    return piDec

@app.route('/<length>')
def getPiN(length):
    return getPiDecimals(int(length))

@app.route('/')
def getPi():
    return getPiDecimals()


if __name__ == '__main__':
    app.run()
