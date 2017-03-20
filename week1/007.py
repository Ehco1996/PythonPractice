#coding:utf-8
'''
五角星的绘制。绘制一个红色的五角星图形，如图所示
关于 turtle.py

# turtle.py: a Tkinter based turtle graphics module for Python
# Version 1.0.1 - 24. 9. 2009
#
# Copyright (C) 2006 - 2010  Gregor Lingl
# email: glingl@aon.at
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.


'''

from turtle import *

fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs (pos()) < 1:
        delay()##阻止窗口的关闭
end_fill
