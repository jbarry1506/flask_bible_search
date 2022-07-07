from flask import Flask, render_template, Response, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from execution import biblesearch


app = Flask(__name__)

app.config['SECRET_KEY'] = 'thesecretkey'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/biblesearch/', methods=["POST", "GET"])
def search_bible():
    word = request.args.get('word')
    print(word)
    return render_template("index.html", word=word)


if __name__ == '__main__':
    app.run(debug=True)
