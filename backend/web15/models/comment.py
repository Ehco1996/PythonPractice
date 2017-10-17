import time
from models import Model

# 针对我们的数据 comment
# 我们要做 4 件事情
"""
C create 创建数据
R read 读取数据
U update 更新数据
D delete 删除数据

Comment.new() 来创建一个 todo
"""


class Comment(Model):
    @classmethod
    def new(cls, form):
        '''类方法，新建评论对象'''
        t = cls(form)
        t.save()
        return t

    def __init__(self, form):
        self.id = None
        self.author = form.get('author', '')
        self.content = form.get('content', '')
        self.create_time = int(time.time())
