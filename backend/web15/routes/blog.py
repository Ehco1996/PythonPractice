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

from models.blog import (
    Blog,
    BlogComment,
)
from utils import log

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字, 以后会有用(add函数里面就用到了)
# 第二个参数是套路
main = Blueprint('blog', __name__)


@main.route("/")
def index():
    all_blog = Blog.all()
    return render_template("blog_index.html", blogs=all_blog)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    Blog.new(form)
    return redirect(url_for('.index'))


@main.route("/new", methods=["GET"])
def new():
    return render_template("blog_new.html")


@main.route("/<int:blog_id>", methods=["GET"])
def view(blog_id):
    comments = BlogComment.find_all(blog_id=blog_id)
    blog = Blog.find(blog_id)
    return render_template("blog_view.html", blog=blog, comments=comments)


@main.route("/comment/new", methods=["POST"])
def comment():
    form = request.form
    BlogComment.new(form)
    return redirect(url_for('.view', blog_id=form.get("blog_id")))