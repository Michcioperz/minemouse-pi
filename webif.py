#!/usr/bin/env python2
from flask import Flask, render_template, g, redirect, url_for
import minemouse, json

app = Flask(__name__)

minemouse.regen()
g.bot = minemouse.Bot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/regen")
def regen():
    minemouse.regen()

@app.route("/bot/reset")
def bot_reset():
    getattr(g, 'bot', None).die()
    return jsonify(zero=0)

@app.route("/bot/move/<int:x>/<int:y>/<int:d>")
def bot_move(x, y, d):
    getattr(g, 'bot', None).move(x, y, d)
    return jsonify(zero=0)

@app.route("/bot/forward/<int:l>")
def bot_forward(l):
    getattr(g, 'bot', None).forward(l)
    return jsonify(zero=0)

@app.route("/bot/go/<int:d>/<int:l>")
def bot_go(d, l):
    getattr(g, 'bot', None).go(d, l)
    return jsonify(zero=0)

@app.route("/bot/turn/<int:d>")
def bot_turn(d):
    getattr(g, 'bot', None).turn(d)
    return jsonify(zero=0)

@app.route("/bot/scan/<results>")
def bot_scan(n, e, s, w):
    getattr(g, 'bot', None).scan(json.loads(results))
    return jsonify(zero=0)
