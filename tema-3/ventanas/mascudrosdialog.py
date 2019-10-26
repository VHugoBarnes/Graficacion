# Programa escrito por: yolyrdz.blogspot.com
from Tkinter import *
from tkMessageBox import *

def main():
    showinfo("Title", "Your message here")
    showerror("An Error", "Oops!")
    showwarning("Title", "This may not work...")
    askyesno("Title", "Do you love me?")
    askokcancel("Title", "Are you well?")
    askquestion("Title", "How are you?")
    askretrycancel("Title", "Go again?")
    askyesnocancel("Title", "Are you well?")

main()