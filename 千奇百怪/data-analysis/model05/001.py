'''
用wxpython
定制一个gui程序
'''

import wx


app = wx.App()
frame = wx.Frame(None, title='hello')
frame.Show()
app.MainLoop()
