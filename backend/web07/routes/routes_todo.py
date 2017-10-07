from models import Todo
from routes.session import session
from utils import log
from utils import template


def response_with_headers(headers, status_code=200):
    header = 'HTTP/1.1 {} OK\r\n'.format(status_code)
    header += ''.join(['{}: {}\r\n'.format(k, v)
                           for k, v in headers.items()])
    return header


def redirect(location):
    headers = {
        'Content-Type': 'text/html',
    }
    headers['Location'] = location
    # 301 永久重定向 302 普通定向
    # 302 状态码的含义, Location 的作用
    header = response_with_headers(headers, 302)
    r = header + '\r\n' + ''
    return r.encode(encoding='utf-8')


# 直接写函数名字不写 route 了
def index(request):
    """
    主页的处理函数, 返回主页的响应
    """
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    session_id = request.cookies.get('user', '')
    user_id = session.get(session_id)
    todo_list = Todo.find_all(user_id=user_id)
    log('index debug', user_id, todo_list)
    body = template('todo_index.html', todos=todo_list)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def add(request):
    """
    接受浏览器发过来的添加 todo 请求
    添加数据并发一个 302 定向给浏览器
    浏览器就会去请求 / 从而回到主页
    """
    # 得到浏览器发送的表单
    form = request.form()
    session_id = request.cookies.get('user', '')
    user_id = session.get(session_id)
    # 创建一个 todo
    Todo.new(form, user_id)
    # 让浏览器刷新页面到主页去
    return redirect('/todo/index')


def delete(request):
    """
    通过下面这样的链接来删除一个 todo
    /delete?id=1
    """
    todo_id = int(request.query.get('id'))
    session_id = request.cookies.get('user', '')
    user_id = session.get(session_id)
    t = Todo.find(todo_id)
    if t.user_id == user_id:
        Todo.delete(todo_id, user_id=user_id)
    return redirect('/')


def edit(request):
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    todo_id = int(request.query.get('id'))
    t = Todo.find(todo_id)
    body = template('simple_todo_edit.html', todo=t)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def update(request):
    # header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    form = request.form()
    todo_id = int(form.get('id'))
    Todo.update(todo_id, form)
    return redirect('/')


route_dict = {
    '/todo/index': index,
    '/todo/add': add,
    '/todo/delete': delete,
    '/todo/edit': edit,
    '/todo/update': update,
}
