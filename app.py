#!/usr/bin/env sage -python

from flask import Flask
import bidimensional_system

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
