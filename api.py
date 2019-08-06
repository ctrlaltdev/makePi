#!/bin/env python3

import os
import time
from flask import Flask, Response, json
from playhouse.db_url import connect
from peewee import MySQLDatabase, IntegerField, SmallIntegerField, Model

app = Flask(__name__)

db = connect(os.environ.get('DATABASE_URL'))

class Pi(Model):
    id = IntegerField()
    n = SmallIntegerField()
    class Meta:
        database = db

def getDecimalsRange(start = 0, length = 1000):
    db.connect()

    getDecimals = Pi.select().where(Pi.id >= start).limit(length)

    piDec = ''

    for d in getDecimals:
        piDec += str(d.n)
    
    db.close()

    return piDec

def getPiDecimals(length = 100, onlyDecimals = False):
    db.connect()
    getDecimals = Pi.select().limit(length)

    piDec = '' if onlyDecimals else '3.'

    for d in getDecimals:
        piDec += str(d.n)

    db.close()

    return piDec

def createRes(content, status = 200):
    headers = { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json; charset=utf-8' }
    res = Response(response=json.dumps(content), status=status, headers=headers)
    return res

def eventStream(delay = 0.5):
    counter = 0
    decimals = getDecimalsRange()
    while counter <= 100000:
        if (counter == len(decimals) - 10):
            decimals += getDecimalsRange(len(decimals))
        yield "data: {}\n\n".format(decimals[counter])
        time.sleep(delay)
        counter += 1

@app.route('/stream/<delay>')
def streamTimedPi(delay):
    try:
        timing = int(delay)
        if (timing < 200):
            return createRes({ 'error': 'Have pity on a small server, increase your delay' }, 400)
        headers = { 'Access-Control-Allow-Origin': '*' }
        return Response(response=eventStream(timing / 1000), mimetype='text/event-stream', headers=headers)
    except ValueError:
        return createRes({ 'error': 'The delay should be an int in milliseconds' }, 400)

@app.route('/stream')
def streamPi():
    headers = { 'Access-Control-Allow-Origin': '*' }
    return Response(response=eventStream(), mimetype='text/event-stream', headers=headers)

@app.route('/decimals/<length>')
def getPiDecN(length):
    try:
        decimals = int(length)
        if (decimals > 100000):
            return createRes({ 'error': 'Awww, come on, that\'s too many decimals for a little server' }, 400)
        return createRes({ 'decimals': getPiDecimals(int(length), True) })
    except ValueError:
        return createRes({ 'error': 'The number of decimals should be an int, DUH.' }, 400)

@app.route('/decimals')
def getPiDec():
    return createRes({ 'decimals': getPiDecimals(100, True) })

@app.route('/<length>')
def getPiN(length):
    try:
        decimals = int(length)
        if (decimals > 100000):
            return createRes({ 'error': 'Awww, come on, that\'s too many decimals for a little server' }, 400)
        return createRes({ 'pi': getPiDecimals(int(length)) })
    except ValueError:
        return createRes({ 'error': 'The number of decimals should be an int, DUH' }, 400)

@app.route('/')
def getPi():
    return createRes({ 'pi': getPiDecimals() })


if __name__ == '__main__':
    app.run()
