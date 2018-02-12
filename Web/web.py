# from flask import Flask
# from flask import request
# from flask import render_template
# # import stringComparison
#
# app = Flask(__name__)
#
# @app.route('/')
# def my_form():
#     return render_template("my-form.html")
#
# @app.route('/', methods=['POST'])
# def my_form_post():
#     text1 = request.form['text1']
#     text2 = request.form['text2']
#     plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(text1,text2)
#     if plagiarismPercent > 50 :
#         return "<h1>Plagiarism Detected !</h1>"
#     else :
#         return "<h1>No Plagiarism Detected !</h1>"
# if __name__ == '__main__':
#     app.run()
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index!"


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/members")
def members():
    return "Members"


@app.route("/members/<string:name>/")
def getMember(name):
    return name


if __name__ == "__main__":
    app.run()