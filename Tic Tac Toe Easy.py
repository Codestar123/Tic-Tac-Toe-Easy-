from tkinter import *
import time
import random
class Game:
    def __init__(self,c):
        self.c = c
        self.turn = 'you'
        self.clicked = []
        self.text = StringVar()
        self.winnertext = Entry(self.c.tk,textvariable = self.text)
        self.winnertext.grid(columnspan =50 , ipadx = 70)
        self.text.set('_____________________________________________________')
        self.but1 = Button(self.c.tk,text ='',  command = lambda: self.but(0),width = 14,height = 7,fg = 'blue',bg = 'yellow')
        self.but1.grid(row = 1,column = 0)
        self.but2 = Button(self.c.tk, text='', command=lambda: self.but(1), width=14, height=7,fg = 'blue',bg = 'yellow')
        self.but2.grid(row=1, column=1)
        self.but3 = Button(self.c.tk, text='', command=lambda: self.but(2), width=14, height=7,fg = 'blue',bg = 'yellow')
        self.but3.grid(row=1, column=2)
        self.but4 = Button(self.c.tk, text='', command=lambda: self.but(3), width=14, height=7,fg = 'blue',bg = 'yellow')
        self.but4.grid(row=2, column=0)
        self.but5 = Button(self.c.tk, text='', command=lambda: self.but(4), width=14, height=7,fg = 'blue',bg = 'yellow')
        self.but5.grid(row=2, column=1)
        self.but6 = Button(self.c.tk, text='', command=lambda: self.but(5), width=14, height=7,fg = 'blue',bg = 'yellow')
        self.but6.grid(row=2, column=2)
        self.but7 = Button(self.c.tk, text='', command=lambda: self.but(6), width=14, height=7,fg = 'blue',bg = 'yellow')
        self.but7.grid(row=3, column=0)
        self.but8 = Button(self.c.tk, text='', command=lambda: self.but(7), width=14, height=7,fg = 'blue',bg = 'yellow')
        self.but8.grid(row=3, column=1)
        self.but9 = Button(self.c.tk, text='', command=lambda: self.but(8), width=14, height=7,fg = 'blue',bg = 'yellow')
        self.but9.grid(row=3, column=2)
        for x in range(0,9):
            self.clicked.append('')
        self.but_for_num = {
            0 : self.but1 ,
            1 : self.but2 ,
            2 : self.but3 ,
            3 : self.but4 ,
            4 : self.but5 ,
            5 : self.but6 ,
            6 : self.but7 ,
            7 : self.but8 ,
            8 : self.but9 ,
        }
        self.num_opt_for_com = [0,1,2,3,4,5,6,7,8]
        self.turn = 'you'
    def but(self,but_no):
        if self.win_com() == False and self.win_you() == False and self.full() == False:
            if self.clicked[but_no] == '' :
                butnotfuncuser = self.but_for_num[but_no]
                butnotfuncuser['text'] = 'O'
                self.c.tk.update()
                del self.clicked[but_no]
                self.clicked.insert(but_no,'O')
                self.turn = 'comp'
                time.sleep(0.09)

        if self.win_com() == False and self.win_you() == False and self.full() == False and self.turn == 'comp':
            numforcom = random.choice(self.num_opt_for_com)
            while self.clicked[numforcom] != '':
                numforcom = random.choice(self.num_opt_for_com)
            butnotfunccom = self.but_for_num[numforcom]
            
            butnotfunccom['text'] = 'X'
            del self.clicked[numforcom]
            self.clicked.insert(numforcom, 'X')
            self.turn = 'you'

        if self.win_com() == True:
            self.text.set('You Lose😒😠👎👺👿')

        if self.win_you() == True:
            self.text.set('You Won😄😎👍👏👌')
        
        if self.full() == True and self.win_you() == False and self.win_com() == False:
            self.text.set('Game Over😐😫✋🙋🍺☔')
    def win_you(self):
        if self.clicked[0] == 'O' and self.clicked[4] == 'O' and self.clicked[8] == 'O'\
            or self.clicked[2] == 'O' and self.clicked[4] == 'O' and self.clicked[6] == 'O'\
            or self.clicked[0] == 'O' and self.clicked[1] == 'O' and self.clicked[2] == 'O' \
            or self.clicked[3] == 'O' and self.clicked[4] == 'O' and self.clicked[5] == 'O' \
            or self.clicked[6] == 'O' and self.clicked[7] == 'O' and self.clicked[8] == 'O' \
            or self.clicked[0] == 'O' and self.clicked[3] == 'O' and self.clicked[6] == 'O' \
            or self.clicked[1] == 'O' and self.clicked[4] == 'O' and self.clicked[7] == 'O' \
            or self.clicked[2] == 'O' and self.clicked[5] == 'O' and self.clicked[8] == 'O':
            return True
        return False
    def win_com(self):
        if self.clicked[0] == 'X' and self.clicked[4] == 'X' and self.clicked[8] == 'X'\
            or self.clicked[2] == 'X' and self.clicked[4] == 'X' and self.clicked[6] == 'X'\
            or self.clicked[0] == 'X' and self.clicked[1] == 'X' and self.clicked[2] == 'X' \
            or self.clicked[3] == 'X' and self.clicked[4] == 'X' and self.clicked[5] == 'X' \
            or self.clicked[6] == 'X' and self.clicked[7] == 'X' and self.clicked[8] == 'X' \
            or self.clicked[0] == 'X' and self.clicked[3] == 'X' and self.clicked[6] == 'X' \
            or self.clicked[1] == 'X' and self.clicked[4] == 'X' and self.clicked[7] == 'X' \
            or self.clicked[2] == 'X' and self.clicked[5] == 'X' and self.clicked[8] == 'X':
            return True
        return False
    def full(self):
        if '' not in self.clicked:
            return True

        return False

class Controller:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('TicTacToe')
        self.tk.resizable(0,0)
        self.tk.wm_attributes('-topmost',1)
        self.tk.configure(background = 'light green')

c = Controller()
g = Game(c)
c.tk.mainloop()
