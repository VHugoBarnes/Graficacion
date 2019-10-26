"""
    Programa escrito por: wxpython
"""
# First things, first. Import the wxPython package.
from wx import *

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello world")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
