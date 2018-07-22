
# 常用的关系型数据库有 mysql postgresql sqlite 等（具体区别上课再说）
#
# 传统数据库以表的形式存储数据
# 一张表可以有很多个字段

# 以用户表为例, 存储 4 个数据的表结构如下
# 用户 id
# 用户名
# 密码
# 邮箱
#
# 范例数据如下
# 1     gua     123     gua@qq.com
# 2     gua1    23      gua1@q.com

# 数据库通过 SQL 来操作数据
# SQL （结构化查询语言）
# 操作数据库的接口 也就是操作数据库的方法
# 增加数据
# 删除数据
# 修改数据
# 查询数据
# CRUD
# create retrieve update delete
#
# 数据库的更多的概念，上课会解释（文字太苍白）
# 请下载 sqlitebrowser 软件（这是一个管理 sqlite 数据库的免费软件，自行搜索或者等群内链接）

# SQL 语句如下（仅为范例，上课会讲具体的语法）
"""
INSERT INTO
    `users`(`id`,`username`,`password`,`email`)
VALUES \
    (2,'','',NULL);

UPDATE `users` SET `username`=? WHERE `_rowid_`='2';
UPDATE `users` SET `password`=? WHERE `_rowid_`='2';
UPDATE `users` SET `email`=? WHERE `_rowid_`='2';
"""

"""
几种关系型数据库的用法和 sql 语法都极度相似
开发中一般会用 sqlite 数据库
部署到服务器上的时候才会使用 mysql 等数据库


下面是 python 操作 sqlite 数据库的范例代码
注意，代码上课会讲，你不用看懂，也不用运行
"""

import sqlite3


def create(conn):
    # 注意 CREATE TABLE 这种语句不分大小写
    sql_create = '''
    CREATE TABLE `users` (
        `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `username`	TEXT NOT NULL UNIQUE,
        `password`	TEXT NOT NULL,
        `email`	TEXT
    )
    '''
    # 用 execute 执行一条 sql 语句
    conn.execute(sql_create)
    print('创建成功')


def insert(conn, username, password, email):
    sql_insert = '''
    INSERT INTO
        users(username,password,email)
    VALUES
        (?, ?, ?);
    '''
    # 下面的写法用 string.format 拼 sql, 是一个严重的安全漏洞
    # 会被 SQL 注入
    # sql = '''
    # INSERT INTO
    #     users(username,password,email)
    # VALUES
    #     ("{}", "{}", "{}")
    # '''.format('123', '345', 'a.com')
    # conn.execute(sql)
    # 参数拼接要用 ?，execute 中的参数传递必须是一个 tuple 类型
    conn.execute(sql_insert, (username, password, email))
    print('插入数据成功')
]

def select(conn):
    # 一个注入的用户名
    usr = 'sql4" or "1"="1'
    pwd = 'gua'
    sql = '''
    SELECT
        id, username, email
    FROM
        users
    WHERE
        username="{}" and password="{}"
    '''.format(usr, pwd)
    # 这是读取数据的套路
    cursor = conn.execute(sql)
    print('所有数据', list(cursor))
    # for row in cursor:
    #     print(row)


def delete(conn, user_id):
    sql_delete = '''
    DELETE FROM
        users
    WHERE
        id=?
    '''
    # 注意, execute 的第二个参数是一个 tuple
    # tuple 只有一个元素的时候必须是这样的写法
    conn.execute(sql_delete, (user_id,))


def update(conn, user_id, email):
    """
    UPDATE
        `users`
    SET
        `email`='gua', `username`='瓜'
    WHERE
        `id`=6
    """
    sql_update = '''
    UPDATE
        `users`
    SET
        `email`=?
    WHERE
        `id`=?
    '''
    conn.execute(sql_update, (email, user_id))


def main():
    # 指定数据库名字并打开
    db_path = 'web8.sqlite'
    conn = sqlite3.connect(db_path)
    print("打开了数据库")
    # 打开数据库后 就可以用 create 函数创建表
    # create(conn)
    # 然后可以用 insert 函数插入数据
    # insert(conn, 'sql4', '1234', 'a@b.c')
    # 可以用 delete 函数删除数据
    # delete(conn, 1)
    # 可以用 update 函数更新数据
    # update(conn, 7, 'gua@cocode.cc')
    # select 函数查询数据
    select(conn)
    #
    # 必须用 commit 函数提交你的修改
    # 否则你的修改不会被写入数据库
    conn.commit()
    # 用完数据库要关闭
    conn.close()


if __name__ == '__main__':
    main()


'''
CREATE TABLE `users` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `username` TEXT NOT NULL UNIQUE,
    `password` TEXT NOT NULL,
    `email` TEXT
)
'''