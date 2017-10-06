from utils import log
from utils import template
from utils import redirect
from utils import http_response

from models import User

import random

session = {}


def random_str():
    seed = 'abcdefjsad89234hdsfkljasdkjghigaksldf89weru'
    s = ''
    for i in range(16):
        random_index = random.randint(0, len(seed) - 2)
        s += seed[random_index]
    return s


def current_user(request):
    session_id = request.cookies.get('user', '')
    user_id = int(session.get(session_id, '-1'))
    u = User.find_by(id=user_id)
    return u


def route_login(request):
    """
    登录页面的路由函数
    """
    headers = {}
    log('login, cookies', request.cookies)

    if request.method == 'POST':
        form = request.form()
        u = User(form)
        if u.validate_login():
            user = User.find_by(username=u.username)
            # 设置 session
            session_id = random_str()
            session[session_id] = user.id
            headers['Set-Cookie'] = 'user={}'.format(session_id)
            log('headers response', headers)
            # 登录后定向到 /
            return redirect('/', headers)
    # 显示登录页面
    body = template('login.html')
    return http_response(body, headers=headers)


def route_register(request):
    """
    注册页面的路由函数
    """
    if request.method == 'POST':
        form = request.form()
        u = User(form)
        if u.validate_register():
            u.save()
            # 注册成功后 定向到登录页面
            return redirect('/login')
        else:
            # 注册失败 定向到注册页面
            return redirect('/register')
    # 显示注册页面
    body = template('register.html')
    return http_response(body)


def route_admin_users(request):
    u = current_user(request)
    log('admin users', u)
    if u is not None and u.is_admin():
        us = User.all()
        body = template('admin_users.html', users=us)
        return http_response(body)
    else:
        return redirect('/login')
# 6, 在 /admin/users 页面中新增一个表单
# 表单包括 id password 两个 input
# 管理员可以在这个表单中输入 id 和 新密码 来修改相应用户的密码
# 这个表单发送 POST 请求到 /admin/user/update
# 所以你要增加一个新的路由函数实现更新用户密码的功能

def route_admin_user_update(request):
    form = request.form()
    user_id = int(form.get('id', -1))
    new_password = form.get('password', '')
    u = User.find_by(id=user_id)
    if u is not None:
        u.password = new_password
        u.save()
    return redirect('/admin/users')


def route_static(request):
    """
    静态资源的处理函数, 读取图片并生成响应返回
    """
    filename = request.query.get('file', 'doge.gif')
    path = 'static/' + filename
    with open(path, 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\nContent-Type: image/gif\r\n\r\n'
        img = header + f.read()
        return img


# 路由字典
route_dict = {
    '/login': route_login,
    '/register': route_register,
    '/admin/users': route_admin_users,
    '/admin/user/update': route_admin_user_update,
}
