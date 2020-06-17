import tkinter 
from tkinter import *
from tkinter.messagebox import showinfo
game = Tk()
game.geometry('303x330')
game.configure(background='black')
game.resizable(0,0)
bclick = True
clicked = 0

def btnClick(buttons):
    global bclick,  clicked
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        clicked += 1
        checkingwin()
        
    if buttons["text"] == " " and bclick == False:
        buttons["text"] = "0"
        bclick = True
        clicked+=1
        checkingwin()
        
def checkingwin():
    if (
       button1['text'] == button2['text'] == button3['text'] == 'X' or
       button4['text'] == button5['text'] == button6['text'] == 'X' or
       button7['text'] == button8['text'] == button9['text'] == 'X' or
       button1['text'] == button4['text'] == button7['text'] == 'X' or
       button2['text'] == button5['text'] == button8['text'] == 'X' or
       button1['text'] == button5['text'] == button9['text'] == 'X' or
       button7['text'] == button5['text'] == button3['text'] == 'X'
       ):
        print("X is winner")
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "X is Winner")
        
        
    elif (
       button1['text'] == button2['text'] == button3['text'] == '0' or
       button4['text'] == button5['text'] == button6['text'] == '0' or
       button7['text'] == button8['text'] == button9['text'] == '0' or
       button1['text'] == button4['text'] == button7['text'] == '0' or
       button2['text'] == button5['text'] == button8['text'] == '0' or
       button1['text'] == button5['text'] == button9['text'] == '0' or
       button7['text'] == button5['text'] == button3['text'] == '0'
       ):
        print("0 is winner")
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "0 is Winner")
        
    elif (clicked == 9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Its a tie")
        disableButton()
        
buttons = StringVar()
player_1 = Label(game, text="Player 1 (X)", font=("Chiller",18), fg='red', bg='black').grid(row=0,column=0)
player_2 = Label(game, text="Player 2 (0)", font=("Chiller",18), fg='red', bg='black').grid(row=0,column=2)
 
button1=Button(game, text=" ", font=("Chiller",18), fg='black',bg='#ffffff',
 width=10, height=3, borderwidth=0, command=lambda: btnClick(button1))
button2=Button(game, text=" ", font=("Chiller",18), fg='black',bg='#ffffff', width=10, height=3, borderwidth=0, command=lambda: btnClick(button2))
button3=Button(game, text=" ", font=("Chiller",18), fg='black',bg='#ffffff', width=10, height=3, borderwidth=0, command=lambda: btnClick(button3))

button4=Button(game, text=" ", font=("Chiller",18), fg='black',bg='#ffffff', width=10, height=3, borderwidth=0, command=lambda: btnClick(button4))
button5=Button(game, text=" ", font=("Chiller",18), fg='black',bg='#ffffff', width=10, height=3, borderwidth=0, command=lambda: btnClick(button5))
button6=Button(game, text=" ", font=("Chiller",18), fg='black',bg='#ffffff', width=10, height=3, borderwidth=0, command=lambda: btnClick(button6))

button7=Button(game, text=" ", font=("Chiller",18), fg='black',bg='#ffffff', width=10, height=3, borderwidth=0, command=lambda: btnClick(button7))
button8=Button(game, text=" ", font=("Chiller",18), fg='black',bg='#ffffff', width=10, height=3, borderwidth=0, command=lambda: btnClick(button8))
button9=Button(game, text=" ", font=("Chiller",18), fg='black',bg='#ffffff', width=10, height=3, borderwidth=0, command=lambda: btnClick(button9))


button1.grid(row=1,column=0,ipadx=1,pady=1)
button2.grid(row=1,column=1,ipadx=1,pady=1)
button3.grid(row=1,column=2,ipadx=1,pady=1)

button4.grid(row=2,column=0,ipadx=1,pady=1)
button5.grid(row=2,column=1,ipadx=1,pady=1)
button6.grid(row=2,column=2,ipadx=1,pady=1)

button7.grid(row=3,column=0,ipadx=1,pady=1)
button8.grid(row=3,column=1,ipadx=1,pady=1)
button9.grid(row=3,column=2,ipadx=1,pady=1)

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
    
game.mainloop()