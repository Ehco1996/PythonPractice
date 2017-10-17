from flask import Flask

from routes.todo import main as todo_routes
from routes.comment import main as comment_routes
from routes.session_exp import main as session_routes
from routes.blog import main as blog_routes
from routes.index import main as index_routes

# web framework
# web application
# __main__
app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = 'test for good'


"""
在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
用法如下
"""
# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
app.register_blueprint(todo_routes, url_prefix='/todo')
app.register_blueprint(comment_routes, url_prefix='/comment')
app.register_blueprint(session_routes, url_prefix='/session')
app.register_blueprint(blog_routes, url_prefix='/blog')
app.register_blueprint(index_routes)


# 运行代码
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
