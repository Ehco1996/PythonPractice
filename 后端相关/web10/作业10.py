# 作业1
# 以上课板书为基础，实现以下功能
#
#
# 添加 weibo
# 目前添加 weibo 功能并不能直接使用，程序这部分有一个小 bug，直接修复就可以了
#
# 作业2
# 删除 weibo
# 在 WeiboTemplate 函数中里补上 delete 部分，这样就可以通过事件委托实现，点击的时候发送 delete 请求。
# 为了方便，删除 weibo 的 api 继续写在 api_todo.py 中，并且参照 todo 部分实现删除 weibo 功能
#
# 作业3
# 更新 weibo
# 更新主要分为三步
# 3.1 点击 edit 按钮，隐藏当前显示的 weibo 内容，插入一个表单，里面有 weibo 内容和 update 按钮
# 3.2 点击 update 按钮，发送 update 请求
# 3.3 在 apt_todo 中添加 update_weibo 路由，并且参照 todo 部分实现更新 weibo 功能
#
# 作业4
# 添加 comment
# 绑定 comment-add 的事件，点击之后发送请求
# 添加 add_comment 路由，并且参照 todo 实现增加的功能，这里需要注意 comment 是通过 weibo_id 与 weibo 关联在一起的
#
# 作业5
# 删除 comment
# WeiboTemplate 函数中需要补上 comment-delete 按钮，然后绑定响应的事件，点击之后发送请求
# 添加 delete_comment 路由，实现删除 comment 的功能。
