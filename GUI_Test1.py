import tkinter.messagebox
from tkinter import *

#creating the main window and storing the window object in 'win'
win=Tk()
#setting title of the window
win.title('Ruuvi readings for ASRO')
#setting the size of the window
win.geometry('500x500')

## CANVAS
#can=Canvas(win, width=500, height=300, bg='cyan') 
#can.place(x=30,y=30)
#oval=can.create_oval(100, 100, 200, 180,fill='green') 
#can.pack()

## BUTTON
def welcome2ASRO():#function of the button
    tkinter.messagebox.showinfo("Greetings","Hello! Welcome to ASRO")
    
btn=Button(win,text="Click Me", width=10,height=5,command=welcome2ASRO)
btn.place(x=200,y=30)

## CHECKBOX
#cb_var1 = IntVar() 
#cb1=Checkbutton(win, text='Python', variable=cb_var1,onvalue=1,offvalue=0,height=5,width=20).grid(row=0, sticky=W) 

## LABEL
#lab=Label(win,text='RuuviTag1',width=50,height=30)
#lab.pack()

## LIST 
# lb = Listbox(win) 
# lb.insert(1, 'Dosa') 
# lb.insert(2, 'Idli') 
# lb.insert(3, 'Roti') 
# lb.insert(4, 'Coffee')
# lb.insert(5, 'Tea')
# lb.insert(6, 'Others') 
# lb.pack() 

# sb = Scrollbar(win) 
# sb.pack( side = RIGHT, fill = Y ) 
# list_1 = Listbox(win, yscrollcommand = sb.set ) 
# for i in range(100): 
#     list_1.insert(END, 'Item ' + str(i)) 
# list_1.pack( side = LEFT, fill = BOTH ) 
# sb.config( command = list_1.yview ) 


win.mainloop() #running the loop that works as a triggerb