from tkinter import *
import badideas


def get_new_idea():
    idea = badideas.generate()
    button1.config(text=idea)
    
def get_neww_idea():
    idea2 = badideas.pattern()
    button2.config(text=idea2)
    
window = Tk()
button1 = Button(window, text="Generate bad ideas!",command=get_new_idea)
button1.pack()

button2 = Button(window, text="Generate bad ideas!",command=get_neww_idea)
button2.pack()
