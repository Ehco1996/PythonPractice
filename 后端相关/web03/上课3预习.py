"""
课 3 预习
2017/02/19


static 目录中存储了图片
templates 目录中存储了 html 文件
utils.py 包含了 log 函数
server.py 是扩展的服务器代码, 详细流程功能说明请看后文
routes.py 是服务器能处理的 path(路由) 和 路由处理函数
models.py 是数据存储的代码


MVC 设计模式（一个经典有用的套路）
Model       数据
View        显示
Controller  控制器



以下是课 3 的 server.py 的整理思路
server.py
    建立host和端口
    监听请求
    接受请求
        分解请求信息
            method
            path
            query
            body
        保存请求
            临时保存，用完就丢
    处理请求
        获取路由字典
            path和响应函数的映射字典
        根据请求的path和字典处理请求并获得返回页面
            routes
                主页
                    返回页面
                登录
                    处理post请求
                        对比post数据和用户数据
                        返回登录结果
                    返回页面
                注册
                    处理post请求
                        对比post数据和注册规则
                        保存合法的注册信息
                            保存到User.txt
                        返回注册结果
                    返回页面
                留言板
                    处理post请求
                        将post的数据加入留言列表
                    返回页面
                        包含留言列表
                静态资源（图片）
                    根据query的内容返回对应的资源
        返回响应内容
    发送响应内容
    关闭请求连接


"""
