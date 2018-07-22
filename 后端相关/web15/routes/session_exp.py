from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    session,
)


main = Blueprint('session', __name__)


# @main.route('/')
# def index():
#     username = session.get("user_name", None)
#     if username is None:
#         return render_template("login.html")
#     else:
#         return render_template('session_index.html', username=username)


@main.route('/')
def index():
    username = session.get("user_name", None)
    if username == None:
        return render_template('login.html')
    else:
        return render_template("session_index.html")


@main.route("/login", methods=['POST'])
def login():
    user_name = request.form.get("user_name", "")
    session["user_name"] = user_name
    return redirect(url_for(".index"))


@main.route("/logout", methods=['get'])
def log_out():
    session.pop("user_name")
    return redirect(url_for(".index"))
