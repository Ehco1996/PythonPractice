/*
1, 给 add button 绑定事件
2, 在事件处理函数中, 获取 input 的值
3, 用获取的值 组装一个 todo-cell HTML 字符串
4, 插入 todo-list 中
*/

var log = function () {
    console.log.apply(console, arguments)
}

var e = function (sel) {
    return document.querySelector(sel)
}

/*
 ajax 函数
*/
var ajax = function (method, path, data, reseponseCallback) {
    var r = new XMLHttpRequest()
    // 设置请求方法和请求地址
    r.open(method, path, true)
    // 设置发送的数据的格式为 application/json
    // 这个不是必须的
    r.setRequestHeader('Content-Type', 'application/json')
    // 注册响应函数
    r.onreadystatechange = function () {
        if (r.readyState === 4) {
            // r.response 存的就是服务器发过来的放在 HTTP BODY 中的数据
            reseponseCallback(r.response)
        }
    }
    // 把数据转换为 json 格式字符串
    data = JSON.stringify(data)
    // 发送请求
    r.send(data)
}

// TODO API
// 获取所有 todo
var apiTodoAll = function (callback) {
    var path = '/api/todo/all'
    ajax('GET', path, '', callback)
}

// 增加一个 todo
var apiTodoAdd = function (form, callback) {
    var path = '/api/todo/add'
    ajax('POST', path, form, callback)
}

// 删除一个 todo 
var apiTodoDelete = function (id, callback) {
    var path = '/api/todo/delete?id=' + id
    ajax('GET', path, '', callback)
}

// 更新一个 todo 
var apiTodoUpdate = function (form, callback) {
    var path = '/api/todo/update'
    ajax('POST', path, form, callback)
}