import wx


class Frame1(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, parent=superior, title='example',
                          pos=(100, 200), size=(350, 200))
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel, value="hello world", size=(350, 200))


app = wx.App()
frame = Frame1(None)
frame.Show(True)
app.MainLoop()
