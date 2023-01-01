# ۱
import tkinter as tk
from tkinter import messagebox  
Quoridor = tk.Tk()
Quoridor.geometry('760x850+300+100')
Quoridor.title("Quoridor Game")
Quoridor.resizable(width=False, height=False)


Square = dict()
for i in range(9) :
    for j in range(9) :
        Square[f'sq{i}{j}'] = tk.Button(Quoridor , bg = "white" , bd = 0)
        Square[f'sq{i}{j}'].place(height = 60 , width = 60 , y = (i+1)*20 + 60*i + 10 , x = (j+1) * 20 + j*60 + 10)
        Square[f'sq{i}{j}'].config(command = lambda arg = Square[f'sq{i}{j}'] , y = i , x = j : move(arg,y,x))



Horizental_wall = dict()
for i in range(10):
    for j in range(9) :
        if i == 0 or i == 9 :
            Horizental_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "gray" , bd = 0)
        else :
            Horizental_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "#aee2ff" , bd= 0)
        
        Horizental_wall[f'wall{i}{j}'].place(height = 20 , width = 60 , x = j * 60 +(j+1)*20 + 10, y = i*60 + i * 20 +10)




Vertical_wall = dict()
for i in range(9) :
    for j in range(10) :
        if j == 0 or j == 9 :
            Vertical_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "gray" , bd = 0)
        else :
            Vertical_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "#aee2ff" , bd =0)
        
        
        Vertical_wall[f'wall{i}{j}'].place(height = 60 , width = 20 , x = j * 60 + (j)*20 + 10, y = i*60+(i+1)*20 + 10)



for i in range(10) :
    for j in range(9) :
        if j < 8 :
            Horizental_wall[f'wall{i}{j}'].config(command = lambda arg1 = Horizental_wall[f'wall{i}{j}'] , arg2 = Horizental_wall[f'wall{i}{j+1}'] , x = i , y = j  : creat_wall(arg1,arg2,x,y))   
for i in range(9) :
    for j in range(10) :
        if i < 8 :
            Vertical_wall[f'wall{i}{j}'].config(command = lambda arg1 = Vertical_wall[f'wall{i}{j}'] , arg2 = Vertical_wall[f'wall{i+1}{j}'] , x = i , y = j : creat_wall(arg1,arg2,x,y))



class Maze :
    X = 9
    Y = 9
    step = 0
    number_of_p1_wall = 10
    xplayer1 = 4
    yplayer1 = 0

    number_of_p2_wall = 10
    xplayer2 = 4
    yplayer2 = 8

player1 = tk.Button(Quoridor , bg = "#ff4d4d" )
player2 = tk.Button(Quoridor , bg = "#00ff80"  )
player1.place(height = 50 , width = 50 , x = 355 , y = 35)
player2.place(height = 50 , width = 50, x = 355 , y = 675 )
player1.config(command = lambda arg = player1 , p = 1 : set_lightblueColor_goal(arg , p))
player2.config(command = lambda arg = player2 , p = 2 : set_lightblueColor_goal(arg , p))

lbl_nwallp1 = tk.Label(Quoridor , bg = "white" , text = "Player1 Walls : 10" , font = ("Aria" ,12 , 'bold') , fg = 'red')
lbl_nwallp1.place(height = 50 , width = 150 , x = 195 , y = 780 , )

lbl_nwallp2 = tk.Label(Quoridor , bg = "white" , text = "Player2 Walls : 10" , font = ("Aria" ,12 , 'bold') , fg = "green")
lbl_nwallp2.place(height = 50 , width = 150 , x = 415 , y = 780)

lbl_turns = tk.Label(Quoridor , text = "Red Turn" , bg = "red"  ,font = ("Helvetica" , 8 , "bold") ,borderwidth=2, relief="solid")
lbl_turns.place(height = 50 , width = 70 , x = 345 , y = 780)


def clear_square_color() :
    for i in range(9) :
        for j in range(9) :
            Square[f'sq{i}{j}']['bg'] = "white"


def creat_wall(arg1 , arg2 , x , y) :
    #messagebox.showinfo(" x , y" , f'{x}  {y}')
    if Maze.step % 2 == 0 :
        if arg1['bg'] == "#aee2ff" and arg2['bg'] == "#aee2ff" and Maze.number_of_p1_wall != 0 :
            clear_square_color()
            arg1['bg'] = "#e8002a" #red
            arg2['bg'] = "#e8002a"
            Maze.step += 1
            Maze.number_of_p1_wall -= 1
            lbl_nwallp1['text'] = f'Player1 Walls : {Maze.number_of_p1_wall}'
            lbl_turns['bg'] = "#00d021"
            lbl_turns['text'] = "Green Turn"
    else :
        if arg1['bg'] == "#aee2ff" and arg2['bg'] == "#aee2ff" and Maze.number_of_p2_wall != 0:
            clear_square_color()
            arg1['bg'] = "#00d021" #green
            arg2['bg'] = "#00d021"
            Maze.step += 1
            Maze.number_of_p2_wall -= 1
            lbl_nwallp2['text'] = f'Player2 Walls : {Maze.number_of_p2_wall}'
            lbl_turns['bg'] = "#e8002a"
            lbl_turns['text'] = "Red Turn"

def set_lightblueColor_goal(arg,p) :
    
    if Maze.step % 2 == 0 :
        if p == 1 :
            #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}  {Maze.yplayer1}')
            clear_square_color()
            if Horizental_wall[f'wall{Maze.yplayer1}{Maze.xplayer1}']['bg'] == "#aee2ff" : #up
                #messagebox.showinfo("up")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer1-1}{Maze.xplayer1}']['bg'] = "#ffff79"

            if Horizental_wall[f'wall{Maze.yplayer1+1}{Maze.xplayer1}']['bg'] == "#aee2ff" : #down
                #messagebox.showinfo("down")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer1+1}{Maze.xplayer1}']['bg'] = "#ffff79"

            if Vertical_wall[f'wall{Maze.yplayer1}{Maze.xplayer1}']['bg'] == "#aee2ff" : #left
                #messagebox.showinfo("left")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer1}{Maze.xplayer1-1}']['bg'] = "#ffff79"

            if Vertical_wall[f'wall{Maze.yplayer1}{Maze.xplayer1+1}']['bg'] == "#aee2ff" : #right
                #messagebox.showinfo("right")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer1}{Maze.xplayer1+1}']['bg'] = "#ffff79"
    
    ###################### player 2
    else :

        if p == 2 :
            clear_square_color()
            if Horizental_wall[f'wall{Maze.yplayer2}{Maze.xplayer2}']['bg'] == "#aee2ff" : #up
                #messagebox.showinfo("up")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer2-1}{Maze.xplayer2}']['bg'] = "#ffff79"

            if Horizental_wall[f'wall{Maze.yplayer2+1}{Maze.xplayer2}']['bg'] == "#aee2ff" : #down
                #messagebox.showinfo("down")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer2+1}{Maze.xplayer2}']['bg'] = "#ffff79"

            if Vertical_wall[f'wall{Maze.yplayer2}{Maze.xplayer2}']['bg'] == "#aee2ff" : #left
                #messagebox.showinfo("left")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer2}{Maze.xplayer2-1}']['bg'] = "#ffff79"

            if Vertical_wall[f'wall{Maze.yplayer2}{Maze.xplayer2+1}']['bg'] == "#aee2ff" : #right
                #messagebox.showinfo("right")
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                Square[f'sq{Maze.yplayer2}{Maze.xplayer2+1}']['bg'] = "#ffff79"
    
     
    #pass
 
def move(arg , y , x) :
    #messagebox.showinfo("block xy " , f'{x}  {y}')
    gy = 0
    gx = 0
    if arg['bg'] == "#ffff79" :

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
            lbl_turns['bg'] = "#00d021"
            lbl_turns['text'] = "Green Turn"
        
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
            lbl_turns['bg'] = "#e8002a"
            lbl_turns['text'] = "Red Turn"








#wall = tk.Button(Quoridor , background  = "red" )
#wall.config(command = lambda arg = wall : change_color(arg))
#wall.place(height = 20 , width = 50 , x = 50 , y = 200)




#3 # loop

Quoridor.mainloop()



