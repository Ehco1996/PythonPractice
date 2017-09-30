"""
课 5 上课内容预习


本次上课的主要内容如下


增加作业中的 redirect 函数
    routes.py 中

一个简单 todo 程序项目, 包含的文件如下
    routes_todo.py 包含了项目的所有路由函数
        显示所有todo (包含在文件中)
        增加todo (包含在文件中)
        更新todo (上课讲)
        删除todo (上课讲, 需要更改 Model)
    todo.py
        包含了 Todo Model, 用于处理数据
    templates/todo_index.html
        显示所有 todo 的页面
    templates/todo_edit.html
        显示编辑 todo 的界面 (现在是空白文件 上课会增加内容)

点击添加按钮增加一个新的 todo 的时候, 程序的流程如下(包含原始 HTTP 报文)
    1, 浏览器提交一个表单给服务器(发送 POST 请求)
POST /todo/add HTTP/1.1
Content-Type: application/x-www-form-urlencoded

title=heuv
    2, 服务器解析出表单的数据, 并且增加一条新数据, 并返回 302 响应
HTTP/1.1 302 REDIRECT
Location: /todo

    3, 浏览器根据 302 中的地址, 自动发送了一条新的 GET 请求
GET /todo HTTP/1.1
Host: ....

    4, 服务器给浏览器一个页面响应
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: ...

<html>
    ....
</html>
    5, 浏览器把新的页面显示出来



把 TODO 改写为带用户功能的高级版(这部分上课讲)
    涉及到不同数据的关联
    关联数据在服务器/浏览器之间的传递
"""



# 下面是一些 HTTP 请求和响应的例子, 本课用不着
"""
POST /login?id=2 HTTP/1.1
Host: localhost:3000
Connection: keep-alive
Content-Length: 25
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Cookie: Pycharm-7367d7d5=bf094603-b9e9-4994-9ebd-564f1f5ad2c0

username=gua&password=123
"""

"""
2017/02/22 19:42:48 login 的响应
HTTP/1.1 210 VERY OK
Content-Type: text/html
Set-Cookie: user=gua1

<html>
"""

"""
2017/02/22 19:45:16 ip and request, ('127.0.0.1', 50317)
GET /login HTTP/1.1
Host: localhost:3000
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Cookie: user=gua1
"""
