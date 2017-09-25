from models import Model


# 定义一个 class 用于保存 message
class Message(Model):
    def __init__(self, form):
        self.author = form.get('author', '')
        self.message = form.get('message', '')
