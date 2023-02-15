#Rock Paper Scissors
from tkinter import *
import random


root = Tk()
root.geometry('400x400')
root.title('Rock,Paper,Scissors')
root.config(bg ='#990545')



Label(root, text = 'ROCK, PAPER, SCISSORS - SHOOT!' , font=('Palatino',24,'bold'), bg = '#10e3e3',fg='#061280').pack(pady=10)



user_take = StringVar()
Label(root, text = 'Choose your weapon rock, paper, scissors:' , font=('Palatino',24,'bold'), bg = '#10e3e3',fg='#061280').pack(pady=10)
Entry(root, font = ('Palatino',20), textvariable = user_take , bg='#051287',fg='#f74d4d').pack(pady=10)




comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    




Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie! You both selected the same.')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You loose! Computer selected paper.')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You win! Computer selected scissors.')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You loose! Computer selected scissors.')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You win! Computer selected rock.')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You loose! Computer selected rock.')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You win! Computer selected paper.')
    else:
        Result.set('Invalid: Choose any one --> rock, paper, scissors')
    
        
    

def Reset():
    Result.set("") 
    user_take.set("")


def Exit():
    root.destroy()


###### button
Button(root, font =('Palatino',20,'bold'), text = 'PLAY',padx =5,bg='#00c777',command = play).pack(pady=10)

Entry(root, font =('Palatino',20), textvariable = Result,bg='#051287',fg='#f74d4d',width = 40,).pack(pady=10)

Button(root, font =('Palatino',20,'bold'), text = 'RESET'  ,padx =5,bg ='#00c777' ,command = Reset).pack(pady=10)

Button(root, font =('Palatino',20,'bold'), text = 'EXIT'  ,padx =5,bg ='#00c777' ,command = Exit).pack(pady=20)

root.mainloop()
