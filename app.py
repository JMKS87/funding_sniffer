from flask import Flask

from fetch_fundings import fetch_fundings

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/fundings')
def fundings():
    fundings = fetch_fundings()
    rv = ""
    for funding in fundings:
        rv += str(funding) + "<br>"
    return rv


if __name__ == '__main__':
    app.run()
