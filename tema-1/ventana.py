# First things, first. Import the wxPython package.
from wx import *

# Next, create an application object.
app = Wx.App()

# Then a frame.
frm = Wx.Frame(None, title="Hello world")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
