# ۱
import tkinter as tk
from tkinter import messagebox  
Quoridor = tk.Tk()
Quoridor.geometry('760x760+300+100')
Quoridor.title("Quoridor Game")
Quoridor.resizable(width=False, height=False)


Square = dict()
for i in range(9) :
    for j in range(9) :
        Square[f'sq{i}{j}'] = tk.Button(Quoridor , bg = "white")
        Square[f'sq{i}{j}'].place(height = 60 , width = 60 , y = (i+1)*20 + 60*i + 10 , x = (j+1) * 20 + j*60 + 10)
        Square[f'sq{i}{j}'].config(command = lambda arg = Square[f'sq{i}{j}'] , y = i , x = j : move(arg,y,x))



Horizental_wall = dict()
for i in range(10):
    for j in range(9) :
        if i == 0 or i == 9 :
            Horizental_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "gray")
        else :
            Horizental_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "blue")
        
        Horizental_wall[f'wall{i}{j}'].place(height = 20 , width = 60 , x = j * 60 +(j+1)*20 + 10, y = i*60 + i * 20 +10)




Vertical_wall = dict()
for i in range(9) :
    for j in range(10) :
        if j == 0 or j == 9 :
            Vertical_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "gray")
        else :
            Vertical_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "blue")
        
        
        Vertical_wall[f'wall{i}{j}'].place(height = 60 , width = 20 , x = j * 60 + (j)*20 + 10, y = i*60+(i+1)*20 + 10)



for i in range(10) :
    for j in range(9) :
        if j < 8 :
            Horizental_wall[f'wall{i}{j}'].config(command = lambda arg1 = Horizental_wall[f'wall{i}{j}'] , arg2 = Horizental_wall[f'wall{i}{j+1}'] , x = i , y = j  : change_color(arg1,arg2,x,y))   
for i in range(9) :
    for j in range(10) :
        if i < 8 :
            Vertical_wall[f'wall{i}{j}'].config(command = lambda arg1 = Vertical_wall[f'wall{i}{j}'] , arg2 = Vertical_wall[f'wall{i+1}{j}'] , x = i , y = j : change_color(arg1,arg2,x,y))



class Maze :
    X = 9
    Y = 9
    step = 0
    xplayer1 = 0
    yplayer1 = 0

    xplayer2 = 0
    yplayer2 = 8


def clear_square_color() :
    for i in range(9) :
        for j in range(9) :
            Square[f'sq{i}{j}']['bg'] = "white"


def change_color(arg1 , arg2 , x , y) :
    #messagebox.showinfo(" x , y" , f'{x}  {y}')
    if Maze.step % 2 == 0 :
        if arg1['bg'] == "blue" and arg2['bg'] == "blue" :
            clear_square_color()
            arg1['bg'] = "red"
            arg2['bg'] = "red"
            Maze.step += 1
    else :
        if arg1['bg'] == "blue" and arg2['bg'] == "blue" :
            clear_square_color()
            arg1['bg'] = "green"
            arg2['bg'] = "green"
            Maze.step += 1


def set_color(arg,p) :
    
    if Maze.step % 2 == 0 :
        if p == 1 :
            #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}  {Maze.yplayer1}')
            clear_square_color()
            if Horizental_wall[f'wall{Maze.yplayer1}{Maze.xplayer1}']['bg'] == "blue" : #up
                #messagebox.showinfo("up")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer1-1}{Maze.xplayer1}']['bg'] = "lightblue"

            if Horizental_wall[f'wall{Maze.yplayer1+1}{Maze.xplayer1}']['bg'] == "blue" : #down
                #messagebox.showinfo("down")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer1+1}{Maze.xplayer1}']['bg'] = "lightblue"

            if Vertical_wall[f'wall{Maze.yplayer1}{Maze.xplayer1}']['bg'] == "blue" : #left
                #messagebox.showinfo("left")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer1}{Maze.xplayer1-1}']['bg'] = "lightblue"

            if Vertical_wall[f'wall{Maze.yplayer1}{Maze.xplayer1+1}']['bg'] == "blue" : #right
                #messagebox.showinfo("right")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer1}{Maze.xplayer1+1}']['bg'] = "lightblue"
    
    ###################### player 2
    else :

        if p == 2 :
            clear_square_color()
            if Horizental_wall[f'wall{Maze.yplayer2}{Maze.xplayer2}']['bg'] == "blue" : #up
                #messagebox.showinfo("up")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer2-1}{Maze.xplayer2}']['bg'] = "lightblue"

            if Horizental_wall[f'wall{Maze.yplayer2+1}{Maze.xplayer2}']['bg'] == "blue" : #down
                #messagebox.showinfo("down")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer2+1}{Maze.xplayer2}']['bg'] = "lightblue"

            if Vertical_wall[f'wall{Maze.yplayer2}{Maze.xplayer2}']['bg'] == "blue" : #left
                #messagebox.showinfo("left")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer2}{Maze.xplayer2-1}']['bg'] = "lightblue"

            if Vertical_wall[f'wall{Maze.yplayer2}{Maze.xplayer2+1}']['bg'] == "blue" : #right
                #messagebox.showinfo("right")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer2}{Maze.xplayer2+1}']['bg'] = "lightblue"
    
     
    #pass
 
def move(arg , y , x) :
    #messagebox.showinfo("block xy " , f'{x}  {y}')
    gy = 0
    gx = 0
    if arg['bg'] == "lightblue" :

        if Maze.step % 2 == 0 :
            if x - Maze.xplayer1 == 0 : 
                gx = Maze.xplayer1

            elif x - Maze.xplayer1 < 0 :
                gx = Maze.xplayer1 - 1
                Maze.xplayer1 -= 1
            elif x - Maze.xplayer1 > 0 :
                gx = Maze.xplayer1 + 1 
                Maze.xplayer1 += 1
            

            if y - Maze.yplayer1 == 0 :
                gy = Maze.yplayer1
            
            elif y - Maze.yplayer1 < 0 :
                gy = Maze.yplayer1 - 1
                Maze.yplayer1 -= 1
            elif y - Maze.yplayer1 > 0 :
                gy = Maze.yplayer1 + 1
                Maze.yplayer1 += 1
            player1.place(x = (gx+1)*20 + gx*60 + 15 , y = (gy+1)*20 + gy*60 + 15)
            clear_square_color()
            Maze.step += 1
        
        ######################################################### p2
        else :
            if x - Maze.xplayer2 == 0 : 
                gx = Maze.xplayer2

            elif x - Maze.xplayer2 < 0 :
                gx = Maze.xplayer2 - 1
                Maze.xplayer2 -= 1
            elif x - Maze.xplayer2 > 0 :
                gx = Maze.xplayer2 + 1 
                Maze.xplayer2 += 1
            

            if y - Maze.yplayer2 == 0 :
                gy = Maze.yplayer2
            
            elif y - Maze.yplayer2 < 0 :
                gy = Maze.yplayer2 - 1
                Maze.yplayer2 -= 1
            elif y - Maze.yplayer2 > 0 :
                gy = Maze.yplayer2 + 1
                Maze.yplayer2 += 1
            player2.place(x = (gx+1)*20 + gx*60 + 15 , y = (gy+1)*20 + gy*60 + 15)
            clear_square_color()
            Maze.step += 1








#wall = tk.Button(Quoridor , background  = "red" )
#wall.config(command = lambda arg = wall : change_color(arg))
#wall.place(height = 20 , width = 50 , x = 50 , y = 200)




#3 # loop
player1 = tk.Button(Quoridor , bg = "black" )
player2 = tk.Button(Quoridor , bg = "yellow" )
player1.place(height = 50 , width = 50 , x = 35 , y = 35)
player2.place(height = 50 , width = 50, x = 35 , y = 675 )
player1.config(command = lambda arg = player1 , p = 1 : set_color(arg , p))
player2.config(command = lambda arg = player2 , p = 2 : set_color(arg , p))
Quoridor.mainloop()



