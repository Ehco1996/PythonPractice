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

from models.comment import Comment
from utils import log

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字, 以后会有用(add函数里面就用到了)
# 第二个参数是套路
main = Blueprint('comment', __name__)


'''
1 拆分有哪些页面 一个页面就行
    author-content-button
    ----comment----
    ----comment----
    ------------

2 组织数据，把数据操作的实现
    comment 数据格式
    1 id
    2 author string
    3 content string
    4 time int

    数据上的方法
    1 新建评论
    2 所有的评论
数据结构 + 数据方法 = 数据类

3 逻辑
    1 add的时候增加一个评论，然后跳转会主页，在主页显示所有的评论

4 页面

'''


@main.route('/')
def index():
    comments = Comment.all()
    return render_template('comment_new.html', comments=comments)


# /todo/add only post
@main.route('/add', methods=['POST'])
def add():
    t = Comment.new(request.form)
    return redirect(url_for('.index'))


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
