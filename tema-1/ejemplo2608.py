# Import every method from Tkinter library.
from Tkinter import *

# Create a variable as a Tk member.
window = Tk()

# Set a window title.
window.title('Mi primer aplicacion')

# Create a label.
lbl = Label(window, text='Nombre:')
lbl2 = Label(window, text='Apellido:')

# Set the position on the window grid.
lbl.grid(row = 0, column = 0)
lbl2.grid(row = 1, column=0)

# Setup of the window size.
window.geometry('350x200')

# Create an Entry member.
txt = Entry(window)
txt2 = Entry(window)

# Set the txt position on the window grid.
txt.grid(row = 0, column = 1)
txt2.grid(row = 1, column = 1)

# Is used when we are ready for the application to run. 
# mainloop() is an infinite loop used to run the application,
# wait for an event to occur and process the event till the windows is not closed.
window.mainloop()
