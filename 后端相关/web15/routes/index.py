from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
)

from models.user import User

from utils import log


main = Blueprint('index', __name__)


def current_user():
    # 从 session 中找到 user_id 字段, 找不到就 -1
    # 然后 User.find_by 来用 id 找用户
    # 找不到就返回 None
    uid = session.get('user_id', -1)
    u = User.find_by(id=uid)
    return u

"""
用户在这里可以
    访问首页(会被设置 cookie)
    注册
    登录

用户登录后, 会写入 session, 并且定向到 /profile
"""
@main.route("/")
def index():
    u = current_user()
    template = render_template("index.html", user=u)
    # 如果要写入 cookie, 必须使用 make_response 函数
    # 然后再用 set_cookie 来设置 cookie
    r = make_response(template)
    r.set_cookie('cookie_name', 'GUA')
    return r


@main.route("/register", methods=['POST'])
def register():
    form = request.form
    u = User.register(form)
    return redirect(url_for('.index'))


@main.route("/login", methods=['POST'])
def login():
    form = request.form
    u = User.validate_login(form)
    if u is None:
        return redirect(url_for('.index'))
    else:
        # session 中写入 user_id
        session['user_id'] = u.id
        return redirect(url_for('.profile'))


@main.route('/profile')
def profile():
    u = current_user()
    if u is None:
        return redirect(url_for('.index'))
    else:
        return render_template('profile.html', user=u)
