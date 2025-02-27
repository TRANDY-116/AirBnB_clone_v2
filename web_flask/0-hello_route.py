#!/usr/bin/python3
""" Starting Flask Application """


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ displays Hello HBNB!" """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run('0.0.0.0', port='5000')
