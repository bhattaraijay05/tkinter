import tkinter
from tkinter import *  
cal = Tk()
cal.geometry('380x550')
cal.title("Calculator")
cal.configure(background='white')
cal.resizable(0,0)

operation = ''
equation = StringVar()
equation.set('0')
#assign the input text
enter_value = Entry(cal, width=16, font=('Monospace',30),borderwidth=0, justify='right', textvariable=equation).grid(row=0,column=0,columnspan=4, padx=10,pady=35)

def click_button(number):
    global operation
    operation = operation + number
    equation.set(operation)
    
def clear_button():
    global operation
    operation = ''
    equation.set('0')
    
def equal_button():
    try:
        global operation
        total = str(eval(operation))
        equation.set(total)
        operation = ''
        
    except:
        equation.set('error')
        operation = ""
    
    
#Assign all the buttons
clr_button = Button(cal, text="AC", font=('Monospace',30), bg='white', fg='#ff5900',command=clear_button, borderwidth=0).grid(row=1,column=0,padx=10,pady=5,sticky=W )
percent_button = Button(cal, text="^", font=('Monospace',30), bg='white', fg='#ff5900',command=lambda: click_button("**"), borderwidth=0).grid(row=1,column=2,padx=10,pady=5,sticky=W )
divide_button = Button(cal, text="÷", font=('Monospace',30), bg='white', fg='#ff5900',command=lambda: click_button("/"), borderwidth=0).grid(row=1,column=3,padx=10,pady=1,sticky=W )


#-----------------------------------------------------------------------------------------------------------------------------------------------------

button_7 = Button(cal, text="7", border=0,  font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("7")).grid(row=2,column=0,padx=10,pady=5,sticky=W,)
button_8 = Button(cal, text="8",  font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("8") ,  borderwidth=0).grid(row=2,column=1,padx=10,pady=5,sticky=W )
button_9 = Button(cal, text="9",  font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("9") ,  borderwidth=0).grid(row=2,column=2,padx=10,pady=5,sticky=W )
mul_button = Button(cal, text='×',  font=('Monospace',30),bg='white',fg='#ff5900',command=lambda: click_button("*") ,  borderwidth=0).grid(row=2,column=3,padx=10,pady=5,sticky=W )


#-----------------------------------------------------------------------------------------------------------------------------------------------------

button_4 = Button(cal, text="4",  font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("4"),  borderwidth=0).grid(row=3,column=0,padx=10,pady=5,sticky=W )
button_5 = Button(cal, text="5",  font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("5"),  borderwidth=0).grid(row=3,column=1,padx=10,pady=5,sticky=W )
button_6 = Button(cal, text="6",  font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("6"),  borderwidth=0).grid(row=3,column=2,padx=10,pady=5,sticky=W )
diff_button = Button(cal, text="-",  font=('Monospace',30),bg='white',fg='#ff5900',command=lambda: click_button("-"),  borderwidth=0).grid(row=3,column=3,padx=15,pady=5,sticky=W )


#-----------------------------------------------------------------------------------------------------------------------------------------------------

button_1 = Button(cal, text="1", font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("1"),   borderwidth=0).grid(row=4,column=0,padx=10,pady=5,sticky=W )
button_2 = Button(cal, text="2", font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("2"),   borderwidth=0).grid(row=4,column=1,padx=10,pady=5,sticky=W )
button_3 = Button(cal, text="3", font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("3"),   borderwidth=0).grid(row=4,column=2,padx=10,pady=5,sticky=W )
add_button = Button(cal, text="+", font=('Monospace',30), bg='white', fg='#ff5900',command=lambda: click_button("+"), borderwidth=0).grid(row=4,column=3,padx=10,pady=5,sticky=W )


#-----------------------------------------------------------------------------------------------------------------------------------------------------

clr_button = Button(cal, text="", font=('Monospace',30), bg='white', fg='black',    borderwidth=0).grid(row=5,column=0,padx=10,pady=5,sticky=W )
button_0 = Button(cal, text="0", font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("0"),   borderwidth=0).grid(row=5,column=1,padx=10,pady=5,sticky=W )
dot_button = Button(cal, text=".", font=('Monospace',30), bg='white', fg='black',command=lambda: click_button("."),   borderwidth=0).grid(row=5,column=2,padx=10,pady=5,sticky=W )
equal_button = Button(cal, text="=", font=('Monospace',30), bg='#ff5900', fg='white',command=equal_button, borderwidth=0).grid(row=5,column=3,padx=10,pady=5,sticky=W )






def quit():
    cal.destroy()
off_button = Button(cal, text="OFF", font=('Monospace',20), bg='white',fg='red',command=quit, borderwidth=0).grid(row=1,column=1,padx=10,pady=5,sticky=W )



cal.mainloop()
