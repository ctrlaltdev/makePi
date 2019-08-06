#!/bin/env python3

import os
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

@app.route('/decimals/<length>')
def getPiDecN(length):
    try:
        decimals = int(length)
        if (decimals > 100000):
            return createRes({ 'error': 'Awww, come on, that\'s too many decimals for a little server' }, 400)
        return createRes({ 'decimals': getPiDecimals(int(length), True) })
    except ValueError:
        return createRes({ 'error': 'The number of decimals should be an int, DUH.' }, 400)

@app.route('/decimals/')
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
        return createRes({ 'error': 'The number of decimals should be an int, DUH.' }, 400)

@app.route('/')
def getPi():
    return createRes({ 'pi': getPiDecimals() })


if __name__ == '__main__':
    app.run()
