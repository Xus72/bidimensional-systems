#!/usr/bin/env sage -python

from flask import Flask, render_template, request
from bidimensional_system import fixed_points
from sage.all import *

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def set_params():
    if request.method == "POST":
        a = request.form.get("a")
        b = request.form.get("b")
    return render_template("index.html")

if __name__ == '__main__':
    xn, yn = var('xn,yn')
    x = var('x')
    a, b = var('a,b')
    f = b * x + 2 * (1 - b) ** (x ** 2 / 1 + x ** 2)
    fn = vector([a * yn + f(x=xn), - xn + f(x=xn + 1)])
    app.run(debug=True)
