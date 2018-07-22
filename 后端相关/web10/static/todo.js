var timeString = function (ct) {
    ct = new Date(ct * 1000)
    ct = ct.toLocaleTimeString()
    return ct
}



var todoTemplate = function (todo) {
    var ct = timeString(todo.ct)
    var t = `
        <div class="todo-cell" data-id="${todo.id}">
            <button class="todo-edit">编辑</button>        
            <button class="todo-delete">删除</button>
            <span>${todo.title}</span>
            <time>${ct}<time>
        </div>
    `
    return t
}

var insertTodo = function (todo) {
    var title = todo.title
    var id = todo.id
    var todoCell = todoTemplate(todo)
    // 插入 todo-list
    var todoList = e('.todo-list')
    todoList.insertAdjacentHTML('beforeend', todoCell)
}


var loadTodos = function () {
    // 调用 ajax api 来载入数据
    apiTodoAll(function (r) {
        // console.log('load all', r)
        // 解析为 数组
        var todos = JSON.parse(r)
        // 循环添加到页面中
        for (var i = 0; i < todos.length; i++) {
            var todo = todos[i]
            insertTodo(todo)
        }
    })
}

var insertEditForm = function (cell) {
    var form = `
    <div class="todo-deit-form">
        <input class="todo-edit-input">
        <button class="todo-update">更新</button>
    </div>
    `
    cell.insertAdjacentHTML('beforeend', form)
}


var bindEventTodoAdd = function () {
    var b = e('#id-button-add')
    // 注意, 第二个参数可以直接给出定义函数
    b.addEventListener('click', function () {
        var input = e('#id-input-todo')
        var title = input.value
        log('click add', title)
        var form = {
            title: title,
        }
        apiTodoAdd(form, function (r) {
            // 收到返回的数据, 插入到页面中
            var todo = JSON.parse(r)
            insertTodo(todo)
        })
    })
}

var bindEventTodoDelete = function () {
    var b = e('.todo-list')
    // 注意, 第二个参数可以直接给出定义函数
    b.addEventListener('click', function (event) {
        var self = event.target
        if (self.classList.contains('todo-delete')) {
            // 删除这个todo的数据
            var todoCell = self.parentElement
            var todo_id = todoCell.dataset.id
            apiTodoDelete(todo_id, function (r) {
                log('删除成功', todo_id)
                // 删除这个todo的页面元素
                todoCell.remove()
            })
        }
    })
}

var bindEventTodoEdit = function () {
    var b = e('.todo-list')
    // 注意, 第二个参数可以直接给出定义函数
    b.addEventListener('click', function (event) {
        var self = event.target
        if (self.classList.contains('todo-edit')) {
            // 删除这个todo的数据
            var todoCell = self.parentElement
            insertEditForm(todoCell)
        }
    })
}

var bindEventTodoUpdate = function () {
    var b = e('.todo-list')
    // 注意, 第二个参数可以直接给出定义函数
    b.addEventListener('click', function (event) {
        var self = event.target
        if (self.classList.contains('todo-update')) {
            // 更新tod
            var editFrom = self.parentElement

            var input = editFrom.querySelector('.todo-edit-input')
            var title = input.value
            // 用closest 方法可以找到最近的直系父节点
            var todoCell = self.closest('.todo-cell')
            var todo_id = todoCell.dataset.id
            var form = {
                'id': todo_id,
                'title': title,
            }
            apiTodoUpdate(form, function (r) {
                log('更新成功', todo_id)
            })
        }
    })
}

var bindEvents = function () {
    bindEventTodoAdd()
    bindEventTodoDelete()
    bindEventTodoEdit()
    bindEventTodoUpdate()


}

var __main = function () {
    bindEvents()
    loadTodos()
}

__main()






/*
给 删除 按钮绑定删除的事件
1, 绑定事件
2, 删除整个 todo-cell 元素
*/
// var todoList = e('.todo-list')
// // 事件响应函数会被传入一个参数, 就是事件本身
// todoList.addEventListener('click', function(event){
//     // log('click todolist', event)
//     // 我们可以通过 event.target 来得到被点击的元素
//     var self = event.target
//     // log('被点击的元素是', self)
//     // 通过比较被点击元素的 class 来判断元素是否是我们想要的
//     // classList 属性保存了元素的所有 class
//     // 在 HTML 中, 一个元素可以有多个 class, 用空格分开
//     // log(self.classList)
//     // 判断是否拥有某个 class 的方法如下
//     if (self.classList.contains('todo-delete')) {
//         log('点到了 删除按钮')
//         // 删除 self 的父节点
//         // parentElement 可以访问到元素的父节点
//         self.parentElement.remove()
//     } else {
//         // log('点击的不是删除按钮******')
//     }
// })