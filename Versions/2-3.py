# ۱
import tkinter as tk
from tkinter import messagebox  
Quoridor = tk.Tk()
Quoridor.geometry('560x610+300+0')
Quoridor.title("Quoridor Game")
Quoridor.resizable(width=False, height=False)



Square = dict()
for i in range(9) :
    for j in range(9) :
        Square[f'sq{i}{j}'] = tk.Button(Quoridor , bg = "white" , bd = 0)
        Square[f'sq{i}{j}'].place(height = 50 , width = 50 , y = (i+1)*10 + 50*i + 5 , x = (j+1) * 10 + j*50 + 5)
        Square[f'sq{i}{j}'].config(command = lambda arg = Square[f'sq{i}{j}'] , y = i , x = j : move(arg,y,x))



Horizental_wall = dict()
for i in range(10):
    for j in range(9) :
        if i == 0 or i == 9 :
            Horizental_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "gray" , bd = 0)
        else :
            Horizental_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "#aee2ff" , bd= 0)
        
        Horizental_wall[f'wall{i}{j}'].place(height = 10 , width = 50 , x = j * 50 +(j+1)*10 + 5, y = i*50 + i * 10 +5)




Vertical_wall = dict()
for i in range(9) :
    for j in range(10) :
        if j == 0 or j == 9 :
            Vertical_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "gray" , bd = 0)
        else :
            Vertical_wall[f'wall{i}{j}'] = tk.Button(Quoridor , background = "#aee2ff" , bd =0)
        
        
        Vertical_wall[f'wall{i}{j}'].place(height = 50 , width = 10 , x = j * 50 + (j)*10 + 5, y = i*50+(i+1)*10 + 5)



for i in range(10) :
    for j in range(9) :
        if j < 8 :
            Horizental_wall[f'wall{i}{j}'].config(command = lambda arg1 = Horizental_wall[f'wall{i}{j}'] , arg2 = Horizental_wall[f'wall{i}{j+1}'] , x = j , y = i , typew = 'h' : creat_wall(arg1,arg2,x,y,typew))   
for i in range(9) :
    for j in range(10) :
        if i < 8 :
            Vertical_wall[f'wall{i}{j}'].config(command = lambda arg1 = Vertical_wall[f'wall{i}{j}'] , arg2 = Vertical_wall[f'wall{i+1}{j}'] , x = j , y = i , typew = 'v': creat_wall(arg1,arg2,x,y,typew))



class Maze :
    X = 9
    Y = 9
    step = 0
    number_of_p1_wall = 10
    xplayer1 = 4
    yplayer1 = 0
    block = list()
    for i in range(9) :
        block.append([])
        for j in range(9) :
            block[i].append({
                'u' : False ,
                'r' : False ,
                'l' : False ,
                'd' : False ,
                'v' : -1
            })
    number_of_p2_wall = 10
    xplayer2 = 4
    yplayer2 = 8

player1 = tk.Button(Quoridor , bg = "#ff4d4d" )
player2 = tk.Button(Quoridor , bg = "#00ff80"  )
player1.place(height = 40 , width = 40 , x = 260 , y = 20)
player2.place(height = 40 , width = 40, x = 260 , y = 500 )
player1.config(command = lambda arg = player1 , p = 1 : set_lightblueColor_goal(arg , p))
player2.config(command = lambda arg = player2 , p = 2 : set_lightblueColor_goal(arg , p))

lbl_nwallp1 = tk.Label(Quoridor , bg = "white" , text = "Player1 Walls : 10" , font = ("Aria" ,9 , 'bold') , fg = 'red')
lbl_nwallp1.place(height = 30 , width = 120 , x = 120 , y = 570 , )

lbl_nwallp2 = tk.Label(Quoridor , bg = "white" , text = "Player2 Walls : 10" , font = ("Aria" ,9 , 'bold') , fg = "green")
lbl_nwallp2.place(height = 30 , width = 120 , x = 320 , y = 570)

lbl_turns = tk.Label(Quoridor , text = "Red Turn" , bg = "red"  ,font = ("Helvetica" , 8 , "bold") ,borderwidth=2, relief="solid")
lbl_turns.place(height = 30 , width = 80 , x = 240 , y = 570)

def assign_wall_to_block() :
    for i in range(9) :
        for j in range(9) :
            if Horizental_wall[f'wall{i}{j}']['bg'] != '#aee2ff'  : #light blue 
                Maze.block[i][j]['u'] = True 
            else :
                Maze.block[i][j]['u'] = False
            if Horizental_wall[f'wall{i+1}{j}']['bg'] != '#aee2ff' :
                Maze.block[i][j]['d'] = True
            else :
                Maze.block[i][j]['d'] = False
            if Vertical_wall[f'wall{i}{j}']['bg'] != '#aee2ff' :
                Maze.block[i][j]['l'] = True
            else :
                Maze.block[i][j]['l'] = False
            if Vertical_wall[f'wall{i}{j+1}']['bg'] != '#aee2ff' :
                Maze.block[i][j]['r'] = True
            else :
                Maze.block[i][j]['r'] = False
    #for i in range(9):
        #for j in range(9):
            #u , r , l , d , v = Maze.block[i][j]['u'] , Maze.block[i][j]['r'] , Maze.block[i][j]['l'] , Maze.block[i][j]['d'] , Maze.block[i][j]['v']
            #messagebox.showinfo(f'block info {i}{j}' , f'u : {u} , r : {r} , l : {l} , d : {d} , v : {v}')

def clear_square_color() :
    for i in range(9) :
        for j in range(9) :
            Square[f'sq{i}{j}']['bg'] = "white"
def reset_vblock() :
    for i in range(9) :
        for j in range(9) :
            Maze.block[i][j]['v'] = -1
def is_valid_wall(x , y , typew) :
    
    #return true or false
    assign_wall_to_block()
    if typew == 'h' :
        Maze.block[y][x]['u'] = True
        Maze.block[y][x+1]['u'] = True 
        Maze.block[y-1][x]['d'] = True
        Maze.block[y-1][x+1]['d'] = True 
    elif typew == 'v' :
        Maze.block[y][x]['l'] = True
        Maze.block[y+1][x]['l'] = True
        Maze.block[y][x-1]['r'] = True
        Maze.block[y+1][x-1]['r'] = True

    else :
        messagebox.showinfo("error - is_valid_wall()" , "typew is not h or v")
    
    ############################################## p1
    reset_vblock()
    validp1 = False
    Maze.block[Maze.yplayer1][Maze.xplayer1]['v'] = 0
    step = 0
    while True :
        f = False
        for i in range(9) :
            for j in range(9) :
                
                if Maze.block[i][j]['v'] == step :
                        #messagebox.showinfo("v" , f'{i} {j} : {step}')
                        if Maze.block[i][j]['u'] == False:
                            if Maze.block[i-1][j]['v'] == -1 :
                                #messagebox.showinfo("v" , f'u {i-1} {j} : {step + 1}')
                                Maze.block[i-1][j]['v'] = step + 1
                                f = True
                        if Maze.block[i][j]['r'] == False  :
                            if Maze.block[i][j+1]['v'] == -1 :
                                #messagebox.showinfo("v" , f'r {i} {j+1} : {step + 1}')
                                Maze.block[i][j+1]['v'] = step + 1
                                f = True
                        if Maze.block[i][j]['l'] == False :
                            if Maze.block[i][j-1]['v'] == -1 :
                                #messagebox.showinfo("v" , f'l {i} {j-1} : {step + 1}')
                                Maze.block[i][j-1]['v'] = step + 1
                                f = True
                        if Maze.block[i][j]['d'] == False :
                            if Maze.block[i+1][j]['v'] == -1 :
                                #messagebox.showinfo("v" , f' d {i+1} {j} : {step + 1}')
                                Maze.block[i+1][j]['v'] = step + 1
                                f = True
        step += 1
        if f == False :
            break
    for i in range(9) :
        #messagebox.showinfo(f'v block8{i}' , Maze.block[8][j]['v'])
        if Maze.block[8][i]['v'] != -1 :
            
            validp1 = True
            break
    #assign_wall_to_block()
    ########################################### p2 
    reset_vblock()
    validp2 = False
    Maze.block[Maze.yplayer2][Maze.xplayer2]['v'] = 0
    step = 0
    while True :
        f = False
        for i in range(9) :
            for j in range(9) :
                if Maze.block[i][j]['v'] == step :
                        if Maze.block[i][j]['u'] == False :
                            if Maze.block[i-1][j]['v'] == -1 :
                                Maze.block[i-1][j]['v'] = step + 1
                                f = True
                        if Maze.block[i][j]['r'] == False :
                            if Maze.block[i][j+1]['v'] == -1 :
                                Maze.block[i][j+1]['v'] = step + 1
                                f = True
                        if Maze.block[i][j]['l'] == False :
                            if Maze.block[i][j-1]['v'] == -1 :
                                Maze.block[i][j-1]['v'] = step + 1
                                f = True
                        if Maze.block[i][j]['d'] == False :
                            if Maze.block[i+1][j]['v'] == -1 :
                                Maze.block[i+1][j]['v'] = step + 1
                                f = True
        step += 1
        if f == False :
            break
    for i in range(9) :
        if Maze.block[0][i]['v'] != -1 :
            validp2 = True
            break
    #assign_wall_to_block()

    ######################### return
    if validp1 == False :
        messagebox.showinfo("wrong wall" , "Player1 will be surrounded")
    if validp2 == False :
        messagebox.showinfo("wrong wall" , "Player2 will be surrounded")
    if validp1 and validp2 :
        return True
    else :
        return False
    assign_wall_to_block()
    ######################### end is_valid_wall() 

def creat_wall(arg1 , arg2 , x , y , typew) :
    #messagebox.showinfo(" x , y" , f'{x}  {y}')
    if Maze.yplayer2 == 0 :
        messagebox.showinfo("End Game" , "Player2 Won")
    elif Maze.yplayer1 == 8 :
        messagebox.showinfo("End Game" , "Player1 Won") 
    else :
        if Maze.step % 2 == 0 :
            if arg1['bg'] == "#aee2ff" and arg2['bg'] == "#aee2ff" and Maze.number_of_p1_wall != 0 :
                clear_square_color()
                if is_valid_wall(x,y,typew) : 
                    arg1['bg'] = "#e8002a" #red
                    arg2['bg'] = "#e8002a"
                    assign_wall_to_block()
                    Maze.step += 1
                    Maze.number_of_p1_wall -= 1
                    lbl_nwallp1['text'] = f'Player1 Walls : {Maze.number_of_p1_wall}'
                    lbl_turns['bg'] = "#00d021"
                    lbl_turns['text'] = "Green Turn"
        else :
            if arg1['bg'] == "#aee2ff" and arg2['bg'] == "#aee2ff" and Maze.number_of_p2_wall != 0:
                clear_square_color()
                if is_valid_wall(x,y,typew) :
                    arg1['bg'] = "#00d021" #green
                    arg2['bg'] = "#00d021"
                    assign_wall_to_block()
                    Maze.step += 1
                    Maze.number_of_p2_wall -= 1
                    lbl_nwallp2['text'] = f'Player2 Walls : {Maze.number_of_p2_wall}'
                    lbl_turns['bg'] = "#e8002a"
                    lbl_turns['text'] = "Red Turn"

def set_lightblueColor_goal(arg,p) :
    #messagebox.showinfo("1" ,f'{Maze.yplayer1} {Maze.xplayer1}')
    #messagebox.showinfo("2" , f'{Maze.yplayer2} {Maze.xplayer2}')
    if Maze.yplayer1 == 8 :
        messagebox.showinfo("End Game" , "Player1 Won")
    elif Maze.yplayer2 == 0 :
        messagebox.showinfo("End Game" , "Player2 Won")
    else :
        pass
        if Maze.step % 2 == 0 :
            if p == 1 :
                #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}  {Maze.yplayer1}')
                clear_square_color()
                if Horizental_wall[f'wall{Maze.yplayer1}{Maze.xplayer1}']['bg'] == "#aee2ff" : #up
                    #messagebox.showinfo("up")
                    #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                    if Maze.yplayer1 - 1 == Maze.yplayer2 and Maze.xplayer1 == Maze.xplayer2 :
                        if Horizental_wall[f'wall{Maze.yplayer1-1}{Maze.xplayer1}']['bg'] == "#aee2ff" :
                            Square[f'sq{Maze.yplayer1-2}{Maze.xplayer1}']['bg'] = "#ffff79"
                    else :
                        Square[f'sq{Maze.yplayer1-1}{Maze.xplayer1}']['bg'] = "#ffff79"

                if Horizental_wall[f'wall{Maze.yplayer1+1}{Maze.xplayer1}']['bg'] == "#aee2ff" : #down
                    #messagebox.showinfo("down")
                    #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                    if Maze.yplayer1+1 == Maze.yplayer2 and Maze.xplayer1 == Maze.xplayer2 :
                        if Horizental_wall[f'wall{Maze.yplayer1+2}{Maze.xplayer1}']['bg'] == "#aee2ff" :
                            Square[f'sq{Maze.yplayer1+2}{Maze.xplayer1}']['bg'] = "#ffff79"
                    else :
                        Square[f'sq{Maze.yplayer1+1}{Maze.xplayer1}']['bg'] = "#ffff79"

                if Vertical_wall[f'wall{Maze.yplayer1}{Maze.xplayer1}']['bg'] == "#aee2ff" : #left
                    #messagebox.showinfo("left")
                    #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                    if Maze.xplayer1 - 1 == Maze.xplayer2 and Maze.yplayer1 == Maze.yplayer2 :
                        if Vertical_wall[f'wall{Maze.yplayer1}{Maze.xplayer1 -1}']['bg'] == "#aee2ff" :
                            Square[f'sq{Maze.yplayer1}{Maze.xplayer1-2}']['bg'] = "#ffff79" 
                    else :
                        Square[f'sq{Maze.yplayer1}{Maze.xplayer1-1}']['bg'] = "#ffff79"

                if Vertical_wall[f'wall{Maze.yplayer1}{Maze.xplayer1+1}']['bg'] == "#aee2ff" : #right
                    #messagebox.showinfo("right")
                    #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                    if Maze.xplayer1 + 1 == Maze.xplayer2 and Maze.yplayer1 == Maze.yplayer2 :
                        if Vertical_wall[f'wall{Maze.yplayer1}{Maze.xplayer1+2}']['bg'] == "#aee2ff" :
                            Square[f'sq{Maze.yplayer1}{Maze.xplayer1+2}']['bg'] = "#ffff79"
                    else :
                        Square[f'sq{Maze.yplayer1}{Maze.xplayer1+1}']['bg'] = "#ffff79"
        
        ###################### player 2
        else :

            if p == 2 :
                clear_square_color()
                if Horizental_wall[f'wall{Maze.yplayer2}{Maze.xplayer2}']['bg'] == "#aee2ff" :  #up
                    #messagebox.showinfo("up")
                    #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                    if Maze.yplayer2 - 1 == Maze.yplayer1 and Maze.xplayer1 == Maze.xplayer2 :
                        if Horizental_wall[f'wall{Maze.yplayer2 - 1}{Maze.xplayer2}']['bg'] == "#aee2ff" : 
                            Square[f'sq{Maze.yplayer2-2}{Maze.xplayer2}']['bg'] = "#ffff79"
                    else :
                        Square[f'sq{Maze.yplayer2-1}{Maze.xplayer2}']['bg'] = "#ffff79"

                if Horizental_wall[f'wall{Maze.yplayer2+1}{Maze.xplayer2}']['bg'] == "#aee2ff" : #down
                    #messagebox.showinfo("down")
                    #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                    if Maze.yplayer2 + 1 == Maze.yplayer1 and Maze.xplayer1 == Maze.xplayer2 :
                        if Horizental_wall[f'wall{Maze.yplayer2+2}{Maze.xplayer2}']['bg'] == "#aee2ff" :
                            Square[f'sq{Maze.yplayer2+2}{Maze.xplayer2}']['bg'] = "#ffff79"
                    else :
                        Square[f'sq{Maze.yplayer2+1}{Maze.xplayer2}']['bg'] = "#ffff79"

                if Vertical_wall[f'wall{Maze.yplayer2}{Maze.xplayer2}']['bg'] == "#aee2ff" : #left
                    #messagebox.showinfo("left")
                    #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                    if Maze.xplayer2 - 1 == Maze.xplayer1 and Maze.yplayer1 == Maze.yplayer2 :
                        if Vertical_wall[f'wall{Maze.yplayer2}{Maze.xplayer2 -1}']['bg'] == "#aee2ff" :
                            Square[f'sq{Maze.yplayer2}{Maze.xplayer2-2}']['bg'] = "#ffff79" 
                    else :
                        Square[f'sq{Maze.yplayer2}{Maze.xplayer2-1}']['bg'] = "#ffff79"

                if Vertical_wall[f'wall{Maze.yplayer2}{Maze.xplayer2+1}']['bg'] == "#aee2ff" : #right
                    #messagebox.showinfo("right")
                    #messagebox.showinfo("p1 xy" , f'{Maze.xplayer1}   {Maze.yplayer1}')
                    if Maze.xplayer2 + 1 == Maze.xplayer1 and Maze.yplayer1 == Maze.yplayer2 :
                        if Vertical_wall[f'wall{Maze.yplayer2}{Maze.xplayer2+2}']['bg'] == "#aee2ff" :
                            Square[f'sq{Maze.yplayer2}{Maze.xplayer2+2}']['bg'] = "#ffff79"
                    else :
                        Square[f'sq{Maze.yplayer2}{Maze.xplayer2+1}']['bg'] = "#ffff79"
        
        
        #pass
        
def move(arg , y , x) :
    #messagebox.showinfo("block xy " , f'{x}  {y}')
    gy = 0
    gx = 0
    xx = 0
    yy = 0
    if arg['bg'] == "#ffff79" :

        if Maze.step % 2 == 0 :
            if x - Maze.xplayer1 == 0 : 
                gx = Maze.xplayer1

            elif x - Maze.xplayer1 < 0 :
                xx = x - Maze.xplayer1
                gx = Maze.xplayer1 + xx
                Maze.xplayer1 += xx
            elif x - Maze.xplayer1 > 0 :
                xx = x - Maze.xplayer1
                gx = Maze.xplayer1 + xx
                Maze.xplayer1 += xx
            

            if y - Maze.yplayer1 == 0 :
                gy = Maze.yplayer1
            
            elif y - Maze.yplayer1 < 0 :
                yy = y - Maze.yplayer1
                gy = Maze.yplayer1 + yy
                Maze.yplayer1 += yy
            elif y - Maze.yplayer1 > 0 :
                yy = y - Maze.yplayer1
                gy = Maze.yplayer1 + yy
                Maze.yplayer1 += yy
            
            player1.place(x = (gx+1)*10 + gx*50 + 10 , y = (gy+1)*10 + gy*50 + 10)
            clear_square_color()
            Maze.step += 1
            lbl_turns['bg'] = "#00d021"
            lbl_turns['text'] = "Green Turn"
            if Maze.yplayer1 == 8 :
                
                lbl_turns['bg'] = "#b4a8ff"
                lbl_turns['text'] = "Player1 Won"
                for i in range(9) :
                    Square[f'sq{8}{i}']['bg'] = "#ffa8a8"
                messagebox.showinfo("End Game" , "Player1 Won")
        
        ######################################################### p2
        else :
            if x - Maze.xplayer2 == 0 : 
                gx = Maze.xplayer2

            elif x - Maze.xplayer2 < 0 :
                xx = x - Maze.xplayer2
                gx = Maze.xplayer2 + xx
                Maze.xplayer2 += xx
            elif x - Maze.xplayer2 > 0 :
                xx = x - Maze.xplayer2
                gx = Maze.xplayer2 + xx
                Maze.xplayer2 += xx
            

            if y - Maze.yplayer2 == 0 :
                gy = Maze.yplayer2
            
            elif y - Maze.yplayer2 < 0 :
                yy = y - Maze.yplayer2
                gy = Maze.yplayer2 + yy
                Maze.yplayer2 += yy
            elif y - Maze.yplayer2 > 0 :
                yy = y - Maze.yplayer2
                gy = Maze.yplayer2 + yy
                Maze.yplayer2 += yy
            
            player2.place(x = (gx+1)*10 + gx*50 + 10 , y = (gy+1)*10 + gy*50 + 10)
            clear_square_color()
            Maze.step += 1
            lbl_turns['bg'] = "#e8002a"
            lbl_turns['text'] = "Red Turn"
            if Maze.yplayer2 == 0 :
                lbl_turns['bg'] = "#b4a8ff"
                lbl_turns['text'] = "Player2 Won"
                for i in range(9) :
                    Square[f'sq{0}{i}']['bg'] = "#b4ffa8"
                messagebox.showinfo("End Game" , "Player2 Won")







#wall = tk.Button(Quoridor , background  = "red" )
#wall.config(command = lambda arg = wall : change_color(arg))
#wall.place(height = 20 , width = 50 , x = 50 , y = 200)




#3 # loop

Quoridor.mainloop()



