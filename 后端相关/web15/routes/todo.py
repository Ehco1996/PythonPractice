from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)
# 一次性引入多个 flask 里面的名字
# 注意最后一个后面也应该加上逗号
# 这样的好处是方便和一致性

from models.todo import Todo
from utils import log

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字, 以后会有用(add函数里面就用到了)
# 第二个参数是套路
main = Blueprint('todo', __name__)

'''
GET /todo/ HTTP/1.1
Host: localhost:2000
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4
'''

'''
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1734
Server: Werkzeug/0.12.1 Python/3.6.0
Date: Fri, 17 Mar 2017 13:05:19 GMT'''
# /todo/
@main.route('/')
def index():
    # 查找所有的 todo 并返回
    todo_list = Todo.all()
    request.method
    log("args", request.args)
    # []
    # todos = todolist
    # flask 已经配置好了 jinja2 模板引擎
    # 并且可以直接使用 render_template 来生成响应数据(http_response)
    return render_template('todo_index.html', todos=todo_list)

# http://localhost:2000/todo/add?a=b&c
# request.args
# dict
#
'''
{
    'a' : 'b',
    'c' : ''

}'''

'''
HTTP/1.0 302 FOUND
Content-Type: text/html; charset=utf-8
Content-Length: 219
Location: http://localhost:2000/todo/
'''
# /todo/add only post
@main.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return redirect(url_for('todo.index'))
    # request local
    # post form request.form()
    # get request.args
    form = request.form
    t = Todo.new(form)
    t.save()
    # 蓝图中的 url_for 需要加上蓝图的名字，这里是 todo

    # todo.index blueprint
    # todo.index
    # /todo/
    return redirect(url_for('todo.index'))


# /todo/delete/1
# /todo/delete/2
'''
GET /todo/delete/2/ HTTP/1.1
Host: localhost:2000
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: http://localhost:2000/todo/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4
'''
# 动态路由
@main.route('/delete/<int:todo_id>/')
def delete(todo_id):
    """
    <int:todo_id> 的方式可以匹配一个 int 类型
    int 指定了它的类型，省略的话参数中的 todo_id 就是 str 类型

    这个概念叫做 动态路由
    意思是这个路由函数可以匹配一系列不同的路由

    动态路由是现在流行的路由设计方案
    """
    # 通过 id 删除 todo
    t = Todo.delete(todo_id)
    log("deleted todo id", todo_id)
    # 引用蓝图内部的路由函数的时候，可以省略名字只用 .
    # 因为我们就在 todo 这个蓝图里面, 所以可以省略 todo
    # return redirect(url_for('todo.index'))
    return redirect(url_for('.index'))
