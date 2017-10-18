from flask import Flask, redirect, url_for, jsonify, request


app = Flask(__name__)
user = []


@app.route('/', methods=["GET"])
def index():
    return'''
    <form method=post action='/add'>
    <input type=text name=author>
    <button>提交</button>
    </form>
'''


@app.route('/add', methods=["POST"])
def add():
    form = request.form
    user.append(dict(author=request.form.get('author', '')))
    return redirect(url_for('.index'))


@app.route('/json')
def json():
    return jsonify(user)


app.run()
