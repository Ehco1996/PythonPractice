from models.user import User
from models.weibo import Weibo
from models.weibo import Comment

from routes.session import session
from utils import template
from utils import response_with_headers
from utils import redirect
from utils import error
from utils import log

Tweet = Weibo


def current_user(request):
    session_id = request.cookies.get('user', '')
    user_id = session.get(session_id, -1)
    return user_id

# 微博相关页面
def index(request):
    headers = {
        'Content-Type': 'text/html',
    }
    header = response_with_headers(headers)
    user_id = request.query.get('user_id', -1)
    user_id = int(user_id)
    user = User.find(user_id)
    if user is None:
        return redirect('/login')
    # 找到 user 发布的所有 weibo
    weibos = Weibo.find_all(user_id=user_id)
    body = template('weibo_index.html', weibos=weibos, user=user)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def new(request):
    headers = {
        'Content-Type': 'text/html',
    }
    uid = current_user(request)
    header = response_with_headers(headers)
    user = User.find(uid)
    body = template('weibo_new.html')
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def add(request):
    headers = {
        'Content-Type': 'text/html',
    }
    uid = current_user(request)
    header = response_with_headers(headers)
    user = User.find(uid)
    # 创建微博
    form = request.form()
    w = Tweet(form)
    w.user_id = user.id
    w.save()
    return redirect('/weibo/index?user_id={}'.format(user.id))


def delete(request):
    headers = {
        'Content-Type': 'text/html',
    }
    uid = current_user(request)
    header = response_with_headers(headers)
    user = User.find(uid)
    # 删除微博
    weibo_id = request.query.get('id', None)
    weibo_id = int(weibo_id)
    w = Tweet.find(weibo_id)
    w.delete()
    return redirect('/weibo/index?user_id={}'.format(user.id))


def edit(request):
    headers = {
        'Content-Type': 'text/html',
    }
    header = response_with_headers(headers)
    weibo_id = request.query.get('id', -1)
    weibo_id = int(weibo_id)
    w = Tweet.find(weibo_id)
    if w is None:
        return error(request)
    # 生成一个 edit 页面
    body = template('weibo_edit.html',
                    weibo_id=w.id,
                    weibo_content=w.content)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def update(request):
    username = current_user(request)
    user = User.find_by(username=username)
    form = request.form()
    content = form.get('content', '')
    weibo_id = int(form.get('id', -1))
    w = Tweet.find(weibo_id)
    if user.id != w.user_id:
        return error(request)
    w.content = content
    w.save()
    # 重定向到用户的主页
    return redirect('/weibo/index?user_id={}'.format(user.id))


def comment_add(request):
    headers = {
        'Content-Type': 'text/html',
    }
    uid = current_user(request)
    header = response_with_headers(headers)
    user = User.find(uid)
    # 创建微博
    form = request.form()
    w = Comment(form)
    w.user_id = user.id
    w.save()
    return redirect('/weibo/index?user_id={}'.format(user.id))

# 定义一个函数统一检测是否登录
def login_required(route_function):
    def func(request):
        uid = current_user(request)
        log('登录鉴定, user_id ', uid)
        if uid == -1:
            # 没登录 不让看 重定向到 /login
            return redirect('/login')
        else:
            # 登录了, 正常返回路由函数响应
            return route_function(request)
    return func


route_dict = {
    '/weibo/index': index,
    '/weibo/new': login_required(new),
    '/weibo/edit': login_required(edit),
    '/weibo/add': login_required(add),
    '/weibo/update': login_required(update),
    '/weibo/delete': login_required(delete),
    # 评论功能
    '/comment/add': login_required(comment_add),
}
