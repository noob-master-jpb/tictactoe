from tkinter import *

def pp():
    g.set('a')
gui = Tk()
gui.title("Tic Tac Toe")
g = StringVar()
bt1 = Button(gui,textvariable = g,padx= 50,pady = 50,command=pp).grid(row = 0,column = 0)

bt2 = Button(gui,text = '2',padx= 50,pady = 50).grid(row = 0,column = 1)
bt3 = Button(gui,text = '3',padx= 50,pady = 50).grid(row = 0,column = 2)
bt4 = Button(gui,text = '4',padx= 50,pady = 50).grid(row = 1,column = 0)
bt5 = Button(gui,text = '5',padx= 50,pady = 50).grid(row = 1,column = 1)
bt6 = Button(gui,text = '6',padx= 50,pady = 50).grid(row = 1,column = 2)
bt7 = Button(gui,text = '7',padx= 50,pady = 50).grid(row = 2,column = 0)
bt8 = Button(gui,text = '8',padx= 50,pady = 50).grid(row = 2,column = 1)
bt9 = Button(gui,text = '9',padx= 50,pady = 50).grid(row = 2,column = 2)

# diflable = Label(gui,text="Difficulty").grid(row = 4,column = 1,pady = 20)
# dbt1 = Button(gui,text = 'Easy',padx= 20,pady = 20).grid(row = 5,column = 0)
# dbt2 = Button(gui,text = 'Hard',padx= 20,pady = 20).grid(row = 5,column = 1)
# dbt3 = Button(gui,text = 'Very Hard',padx= 20,pady = 20).grid(row = 5,column = 2)
gui.geometry("350x500")

gui.mainloop()
