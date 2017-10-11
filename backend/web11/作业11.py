# 作业 1
#
# 下面的代码直接复制
#
# 然后按照作业要求完成 CSS 部分
#
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>课 10 布局练习</title>
#     <!-- 这是基础的 css 不要改动 -->
#     <style>
#         .gua-header {
#             height: 50px;
#             background: lightsteelblue;
#         }
#         .gua-content {
#             height: 80px;
#             background: lightcoral;
#         }
#         .gua-index {
#             height: 50px;
#             background: lightblue;
#         }
#         .gua-detail {
#             height: 30px;
#             background: lightyellow;
#         }
#         .gua-footer {
#             height: 50px;
#             background: lightseagreen;
#         }
#     </style>
#     <!-- 你的 css 写在这个 style 标签里 -->
#     <style>
#
#     </style>
# </head>
# <body>
#     <div class="gua-page">
#         <div class="gua-header">
#             header
#         </div>
#
#         <div class="gua-container">
#             <div class="gua-index">
#                 index
#             </div>
#             <div class="gua-content">
#                 content
#             </div>
#             <div class="gua-detail">
#                 detail
#             </div>
#         </div>
#
#         <div class="gua-footer">
#             footer
#         </div>
#     </div>
# </body>
# </html>
# 参考的链接
# http://jsbin.com/taraqapafo/edit?html,css,output
#
# gua-header gua-footer 不做额外改动
# 参考上课的板书使用 float 布局实现以下设计
#
# gua-content 占一半宽度
# gua-index 在左边占据 25%
# gua-detail 在右边占据 25%
#
# 作业 2
# 在作业 1 的基础上让 gua-container 占据 80% 的宽度，并且使用 margin 使其水平居中
#
# 作业 3
# 给 gua-container 添加 clearfix class，并且实现清除浮动
#
#
# 作业4
# 设置
# gua - header
# 元素
# hover
# 时的颜色和背景色
# 颜色为  # fff
# 背景色为  # 698ebf
#
# 作业5
# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="utf-8">
#         <title>1, 最基础的导航栏样式 - 导航栏 css 大全</title>
#     </head>
#     <style>
#         nav {
#             background: black;
#         }
#         /* 组合选择器, 选中 class 为 gua-nav-item 的 a 标签*/
#         /* 当然, 不写 a 也是一样的 */
#         a.gua-nav-item {
#             /* 设置 inlin-block, 这样才能设置 a 的尺寸和 padding */
#             display: inline-block;
#             color: white;
#             padding: 20px;
#             text-align: center;
#             text-decoration: none;
#         }
#
#         /* 鼠标移上去的时候, 设置新颜色 */
#         .gua-nav-item:hover {
#             background-color: white;
#             color: black;
#             /* 鼠标指针变为链接手 */
#             cursor: pointer;
#         }
#     </style>
#     <body>
#         <!--
#         nav 是 HTML5 里面的新标签, 和 div 一样的, 默认 display: block
#         这里当然用 div 也是完全没问题的, 只是你要加 class(不然怎么设置专有样式呢?)
#         但是在 HTML5 中你完全可以用任意自定义标签, 自己设置它的样式就可以了
#         -->
#         <nav>
#           <a class="gua-nav-item" href="#">首页</a>
#           <a class="gua-nav-item" href="#">博客</a>
#           <a class="gua-nav-item" href="#">宝库</a>
#           <a class="gua-nav-item" href="#">关于</a>
#         </nav>
#     </body>
# </html>
# 导航栏作业 1
# 直接复制上面的 HTML，然后完成下列布局要求
# 1, 设置导航栏背景色为黑色
# 2, 设置链接的 display color padding 居中, 删除下划线
# 3, 给链接设置 hover 的颜色和背景色
#
#
# 作业6
# 导航栏作业 2
# 在导航栏作业 1 的基础上，完成下面要求
#
# 给基础导航栏加上一个 高亮当前菜单 功能
# 1, 给「首页」那个链接设置 gua-active 类
# 2, 给 gua-active 写样式
# a.gua-active {
#     background: red;
# }
#
# 作业7
# 导航栏作业 3
# 在导航栏作业 2 的基础上，完成下面要求
#
# 让部分菜单右对齐
# 1, 给「关于」那个链接加一个 gua-right 类
# 2, 设置样式, 右浮动
# .gua-right {
#     float: right;
# }
#
# 作业8
# 导航栏作业 4
#
# 这个作业主要实现下拉菜单，直接复制下面的代码，然后完成下拉的布局
#
# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="utf-8">
#         <title>4, 下拉菜单基础 - 导航栏 css 大全</title>
#     </head>
#     <style>
#         /*
#         下拉菜单基础
#         1, content 默认是 display: none
#         2, 在 dropdown:hover 的时候, 设置 content 显示
#         */
#         .gua-dropdown-content {
#             /*
#             我们可以先布局好菜单的显示再设置 none, 方便开发调试
#             */
#             display: none;
#             /*
#             为何用 absolute
#             因为我们不希望它对页面布局产生影响
#             */
#             position: absolute;
#             background-color: black;
#         }
#
#         .gua-dropdown {
#             /* 因为 content 需要 absolute 定位, 所以作为父节点必须不是 static */
#             position: relative;
#         }
#
#         /*
#         这是一个组合选择器
#         选中的是 gua-dropdown:hover 的子元素 gua-dropdown-content
#         也就是说 dropdown:hover 的时候, content 才会有这个样式
#         */
#         .gua-dropdown:hover .gua-dropdown-content {
#             display: block;
#         }
#
#         /* 用组合选择器美化一下菜单 */
#         .gua-dropdown-content a {
#             display: block;
#             padding: 5px 15px;
#             color: white;
#             text-decoration: none;
#         }
#
#         .gua-dropdown-content a:hover {
#             background: white;
#             color: black;
#         }
#     </style>
#     <body>
#         <!--
#         小作业, 美化一下 gua-dropdown-title
#         -->
#         <div class="gua-dropdown">
#             <a class="gua-dropdown-title" href="#">下拉菜单</a>
#             <div class="gua-dropdown-content">
#                 <a class="gua-nav-item" href="#">博客</a>
#                 <a class="gua-nav-item" href="#">宝库</a>
#                 <a class="gua-nav-item" href="#">关于</a>
#             </div>
#         </div>
#     </body>
# </html>
#
# 作业9
# 图标输入框作业
# 复制下面代码，然后实现图标输入框布局
# 1, input 设置背景图片
# 2, 设置 padding-left 给图片腾出空间
# 注意, 你必须在目录下放一个 icon.png 图片, 尺寸最好是 32*32
#
# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="utf-8">
#         <title>5, 图标输入框 - 导航栏 css 大全</title>
#     </head>
#     <style>
#         input.gua-icon-input {
#             /* 设置外观 */
#             border: 1px solid red;
#             font-size: 20px;
#             /* 这个缩写的含义请在浏览器中用检查器看 */
#             background: url(icon.png) no-repeat scroll 4px;
#             /* 下面这样可以让图片居中 */
#             height: 40px;
#             padding-left: 40px;
#         }
#     </style>
#     <body>
#         <input class="gua-icon-input" type="text" name="name" value="">
#     </body>
# </html>