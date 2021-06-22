from tkinter import *
import tkinter.font as font
import time;
import time
import random
from random import randint
from cyber_tools import get_hashed_password, hashes_match, get_popular_passwords_from_file


window = Tk()
window.overrideredirect(True)

homeFrame = Frame(window)
timeFrame = Frame(window)
calcFrame = Frame(window)
canvasFrame = Frame(window)
calculatortestFrame = Frame(window)
bombFrame = Frame(window)
pongFrame = Frame(window)
mazeFrame = Frame(window)

cell_size = 12 
ms = 50 
visited_cells = []
walls = []
revisited_cells = []

canvas_side = ms*cell_size
ffs = Canvas(mazeFrame, width = canvas_side, height = canvas_side, bg = 'grey')


map = [['w' for _ in range(ms)] for _ in range(ms)]

canvas = Canvas(canvasFrame, height=750, width = 1275, bg="white", cursor = "dot")
colour = "black"

pongCanvas = Canvas(pongFrame, width = 1500, height = 1000, bg = "cyan", cursor = "dot", bd = 10)
NotColour = "red"
lastx, lasty = 0,0


equation = StringVar()
input_field = Entry(calculatortestFrame, textvariable=equation)



gameover = False
score = 0
squarestoclear = 0
bombfield = []

expression = ""

def fnplay_bombdoger():
    global gameover
    gameover=False
    homeFrame.pack_forget()
    bombFrame.pack(padx=5,pady=5)
    create_bombfield(bombfield)
    layout_window(bombFrame)

def create_bombfield(bombfield):   
    global squarestoclear
    for row in range(0,10):
        rowlist = []
        for column in range (0,10):
            if random.randint(1,100) < 20:
                rowlist.append(1)
            else:
                rowlist.append(0)
                squarestoclear +=  1
        bombfield.append(rowlist)
                
def printfield(bombfield):
    for rowlist in bombfield:
        print(rowlist)
        
def click_function(event):
    global bombfield
    global gameover
    if not gameover:
        onclick(event)
    

def layout_window(bombFrame):
    global bombfield
    for rownumber, rowlist in enumerate (bombfield):
        for columnumber,columentry in enumerate (rowlist):
            if random.randint(1,100) < 35:
                square = Label(bombFrame, text = "    ", bg = "green")
            elif random.randint(1,100) > 65:
                square = Label(bombFrame, text="    ", bg = "seagreen")
            else:
                square = Label(bombFrame, text = "    ", bg = "darkgreen")
            square.grid(row = rownumber, column = columnumber)
            square.bind("<Button-1>",click_function)
            
def onclick(event):
    canvas.pack()
    global row
    global score
    global gameover
    global squarestoclear
    gameover = False
    score = 0
    squarestoclear = 0
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currenttext = square.cget("text")
    if gameover == False:
        if bombfield[row][column] == 1:    
            gameover = True
            square.config(bg = "red")
            Quit = Button(bombFrame, text=("Quit"), width=5, command = fnlogin)
            Quit.place(height=70)
        elif bombfield[row][column] == 0:
            square.config(bg = "white")
            totalbombs = 0
            if row < 9:
                if bombfield[row+1][column] == 1:
                    totalbombs = totalbombs + 1
            if row > 0:
                if bombfield[row-1][column] == 1:
                    totalbombs = totalbombs + 1
            if column > 0:
                if bombfield[row][column-1] == 1:
                    totalbombs = totalbombs + 1
            if column < 9:
                if bombfield[row][column+1] == 1:
                    totalbombs = totalbombs + 1
            if row > 0 and column> 0:
                if bombfield[row-1][column-1] == 1:
                    totalbombs = totalbombs + 1
            if row < 9 and column > 0:
                if bombfield[row+1][column-1] == 1:
                    totalbombs = totalbombs + 1
            if row > 0 and column < 9:
                if bombfield[row-1][column+1] == 1:
                    totalbombs = totalbombs + 1
            if row < 9 and column < 9:
                if bombfield[row+1][column+1] == 1:
                    totalbombs = totalbombs + 1
            square.config(text=" "+ str(totalbombs) + " ")
            squarestoclear = squarestoclear - 1
            score = score+1
            if squarestoclear == 0:
                gameover = True
                Quit = Button(bombFrame, text=("Quit"), width=5, command = fnlogin)
                Quit.place(height=70)


def input_number(number, equation):
   global expression
   expression = expression + str(number)
   equation.set(expression)
def clear_input_field(equation):
   global expression
   expression = ""
   equation.set("Enter the question?")
def evaluate(equation):
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        expression = ""

def set_colour_red(event):
    global colour
    colour = "red"
    
def set_colour_blue(event):
    global colour
    colour = "blue"
    
def set_colour_yellow(event):
    global colour
    colour = "yellow"
    

def set_colour_green(event):
    global colour
    colour = "green"
    
def set_colour_black(event):
    global colour
    colour = "black"


def store_position(event):
    global lastx, lasty
    lastx = event.x
    lasty = event.y
    
def on_click(event):
    store_position(event)
    
def on_drag(event):
    canvas.create_line(lastx,lasty,event.x,event.y, fill = colour, width = 4)
    on_click(event)


def fncalculatortest():
    homeFrame.pack_forget()
    calculatortestFrame.pack(padx=5,pady=5)
    input_field.place(height=100)
    input_field.grid(columnspan=4, ipadx=70, ipady=5)
    equation.set("Enter the expression")
    btn1 = Button(calculatortestFrame, text='1', fg='white', bg='black', bd=0, command=lambda: input_number(1, equation), height=2, width=7)
    btn1.grid(row=2, column=0)
    btn2 = Button(calculatortestFrame, text='2', fg='white', bg='black', bd=0, command=lambda: input_number(2, equation), height=2, width=7)
    btn2.grid(row=2, column=1)
    btn3 = Button(calculatortestFrame, text='3', fg='white', bg='black', bd=0, command=lambda: input_number(3, equation), height=2, width=7)
    btn3.grid(row=2, column=2)
    btn4 = Button(calculatortestFrame, text='4', fg='white', bg='black', bd=0, command=lambda: input_number(4, equation), height=2, width=7)
    btn4.grid(row=3, column=0)
    btn5 = Button(calculatortestFrame, text='5', fg='white', bg='black', bd=0, command=lambda: input_number(5, equation), height=2, width=7)
    btn5.grid(row=3, column=1)
    btn6 = Button(calculatortestFrame, text='6', fg='white', bg='black', bd=0, command=lambda: input_number(6, equation), height=2, width=7)
    btn6.grid(row=3, column=2)
    btn7 = Button(calculatortestFrame, text='7', fg='white', bg='black', bd=0, command=lambda: input_number(7, equation), height=2, width=7)
    btn7.grid(row=4, column=0)
    btn8 = Button(calculatortestFrame, text='8', fg='white', bg='black', bd=0, command=lambda: input_number(8, equation), height=2, width=7)
    btn8.grid(row=4, column=1)
    btn9 = Button(calculatortestFrame, text='9', fg='white', bg='black', bd=0, command=lambda: input_number(9, equation), height=2, width=7)
    btn9.grid(row=4, column=2)
    btn0 = Button(calculatortestFrame, text='0', fg='white', bg='black', bd=0, command=lambda: input_number(0, equation), height=2, width=7)
    btn0.grid(row=5, column=0)
    btnplus = Button(calculatortestFrame, text='+', fg='white', bg='black', bd=0, command=lambda: input_number('+', equation), height=2, width=7)
    btnplus.grid(row=2, column=3)
    btnminus = Button(calculatortestFrame, text='-', fg='white', bg='black', bd=0, command=lambda: input_number('-', equation), height=2, width=7)
    btnminus.grid(row=3, column=3)
    btnmultiply = Button(calculatortestFrame, text='*', fg='white', bg='black', bd=0, command=lambda:  input_number('*', equation), height=2, width=7)
    btnmultiply.grid(row=4, column=3)
    btndivide = Button(calculatortestFrame, text='/', fg='white', bg='black', bd=0, command=lambda: input_number('/', equation), height=2, width=7)
    btndivide.grid(row=5, column=3)
    btnequal = Button(calculatortestFrame, text='=', fg='white', bg='black', bd=0, command=lambda: evaluate(equation), height=2, width=7)
    btnequal.grid(row=5, column=2)
    btnclear = Button(calculatortestFrame, text='Clear', fg='white', bg='black', bd=0, command=lambda: clear_input_field(equation), height=2, width=7)
    btnclear.grid(row=5, column=1)
    btnhome = Button(calculatortestFrame, text="home", command=fnlogin)
    btnhome.grid(row=5, column=4)


def password_valid(user,passw):
    popular_passwords_list = []
    count = 0
    get_popular_passwords_from_file("passwords.txt", popular_passwords_list)
    username1 = user
    with open("passwords.txt") as file:
        for line in file:
            line = line.rstrip("\n")
            username, pw = line.split(" ")
            for popular_password in popular_passwords_list:
                result = get_hashed_password(passw, "md5")
                userhash = get_hashed_password(username1, "md5")
                if hashes_match(username, userhash):
                    if hashes_match(result, pw):
                        return True
                    else:
                        return False
                else:
                    return False
#    if user == "joe" and passw == "pass" or user == "dad" and passw == "word" or user == "ham" and passw == "smith" or user == "sparky" and passw == "ksp" or user == "small" and passw == "isaac":
#        return True
#    else:
#        return False
def fnlogin():
    if password_valid(usr.get(),pas.get()):
        window.overrideredirect(True)
        window.attributes("-fullscreen", False)
        window.geometry('370x220')
        loginFrame.pack_forget()
        canvas.delete("all")
        pongCanvas.delete("all")
        pongFrame.pack_forget()
        mazeFrame.pack_forget()
        ffs.pack_forget()
        bombFrame.pack_forget()
        canvasFrame.pack_forget()
        timeFrame.pack_forget()
        calculatortestFrame.pack_forget()
        homeFrame.pack(padx=5,pady=5)
        res = "Welcome " + usr.get()
        lblWelcome = Label(homeFrame, text=res)
        lblWelcome.grid(column=0, row=0)
        btntime = Button(homeFrame, text="time", command=fntime)
        btncalc = Button(homeFrame, text="calculator", command=fncalculatortest)
        btnlotto = Button(homeFrame, text="drawing", command=fncanvas)
        btnhiguy = Button(homeFrame, text="bomb dodgers", command=fnplay_bombdoger)
        btnpong = Button(homeFrame, text="pong", command=fnpong)
        btnmaze = Button(homeFrame, text="maze", command=fnmaze)
        btnQUIT = Button(homeFrame, text="QUIT", command=fnQUIT)
        btntime.grid(column=1, row=1)
        btncalc.grid(column=2, row=1)
        btnlotto.grid(column=1, row=2)
        btnhiguy.grid(column=2, row=2)
        btnpong.grid(column=1, row=3)
        btnmaze.grid(column=2, row=3)
        btnQUIT.grid(column=1, row=4)
    else:
        incorrectlbl = Label(loginFrame, bg="red", foreground="white", text="incorrect password or username")
        incorrectlbl.grid(column=0, row=4)

def create():
    global btnhome1
    "Create a rectangle with draw function (below) with random color"
    for row in range(ms):
        for col in range(ms):
            if map[row][col] == 'P':
                color = 'White'
            elif map[row][col] == 'w':
                color = 'black'
            draw(row, col, color)

 
 
def draw(row, col, color):
    x1 = col * cell_size
    y1 = row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size
    ffs.create_rectangle(x1, y1, x2, y2, fill=color)

 
 
def check_neighbours(ccr, ccc):
    neighbours = [[
        ccr,
        ccc - 1,
        ccr - 1,
        ccc - 2,
        ccr,
        ccc - 2,
        ccr + 1,
        ccc - 2,
        ccr - 1,
        ccc - 1,
        ccr + 1,
        ccc - 1
    ],
 
# left
                [ccr, ccc + 1, ccr - 1, ccc + 2, ccr, ccc + 2, ccr + 1, ccc + 2, ccr - 1, ccc + 1, ccr + 1, ccc + 1], #right
                [ccr - 1, ccc, ccr - 2, ccc - 1, ccr - 2, ccc, ccr - 2, ccc + 1, ccr - 1, ccc - 1, ccr - 1, ccc + 1], #top
                [ccr + 1, ccc, ccr + 2, ccc - 1, ccr + 2, ccc, ccr + 2, ccc + 1, ccr + 1, ccc-1, ccr + 1, ccc + 1]] #bottom
    visitable_neighbours = []           
    for i in neighbours:                                                                        #find neighbours to visit
        if i[0] > 0 and i[0] < (ms-1) and i[1] > 0 and i[1] < (ms-1):
            if map[i[2]][i[3]] == 'P' or map[i[4]][i[5]] == 'P' or map[i[6]][i[7]] == 'P' or map[i[8]][i[9]] == 'P' or map[i[10]][i[11]] == 'P':
                walls.append(i[0:2])                                                                                               
            else:
                visitable_neighbours.append(i[0:2])
    return visitable_neighbours

scr = randint(1, ms)
# starting random column
scc = randint(1, ms)
start_color = 'Green'
# memorize row and column of the starting rectangle
# current color row and current color column
ccr, ccc = scr, scc
x1 = ccr * 12
y1 = ccc * 12
#print(scr, scc)
#print(ccr, ccc)

map[ccr][ccc] = 'P'
loop = 1
while loop:
    visitable_neighbours = check_neighbours(ccr, ccc)
    if len(visitable_neighbours) != 0:
        d = randint(1, len(visitable_neighbours))-1
        ncr, ncc = visitable_neighbours[d]
        map[ncr][ncc] = 'P'
        visited_cells.append([ncr, ncc])
        ccr, ccc = ncr, ncc
    if len(visitable_neighbours) == 0:
        try:
            ccr, ccc = visited_cells.pop()
            revisited_cells.append([ccr, ccc])

     
        except:
            loop = 0

def fnmaze():
    window.geometry('750x650')
    fnmaze1()

def fnmaze1():
    homeFrame.pack_forget()
    mazeFrame.pack()
    ffs.pack()
    btnhome1 = Button(mazeFrame, text = "home", command = fnlogin, anchor = W)
    btnhome1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    btnhome1_window = ffs.create_window(1, 1, anchor=NW, window=btnhome1)
    create()
    y1 = scr * cell_size 
    x1 = scc * cell_size
    draw(scr, scc, start_color)
    e = randint(1, len(revisited_cells))-1
    ecr = revisited_cells[e][0]
    ecc = revisited_cells[e][1]
    end_color = 'red'
    draw(ecr, ecc, end_color)
    # print(revisited_cells)

 
 
 
def draw_rect():
    ffs.create_rectangle((x1, y1, x1 + 12, y1 + 12), fill="green")
    btnhome3 = Button(mazeFrame, text = "home", command = fnlogin, anchor = W)
    btnhome3.configure(width = 100, activebackground = "#33B5E5", relief = FLAT)
    btnhome3_window = ffs.create_window(1, 1, anchor=NW, window=btnhome3)
 
def del_rect():
    ffs.create_rectangle((x1, y1, x1 + 12, y1 + 12), fill="white")
    btnhome4 = Button(mazeFrame, text = "home", command = fnlogin, anchor = W)
    btnhome4.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    btnhome4_window = ffs.create_window(1, 1, anchor=NW, window=btnhome4)
 
def move(event):
    global x1, y1
    # print(event.char)
    del_rect()
    col = w = x1//cell_size
    row = h = y1//cell_size
#    print("before", map[row][col])
    if event.char == "a":
        if map[row][col - 1] == "P":
            x1 -= cell_size
    elif event.char == "d":
        if map[row][col + 1] == "P":
            x1 += cell_size
    elif event.char == "w":
        if map[row - 1][col] == "P":
            y1 -= cell_size
    elif event.char == "s":
        if map[row + 1][col] == "P":
            y1 += cell_size
 
    draw_rect()
    col = w = x1//cell_size
    row = h = y1//cell_size
    btnhome2 = Button(mazeFrame, text = "home", command = fnlogin, anchor = W)
    btnhome2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    btnhome2_window = ffs.create_window(1, 1, anchor=NW, window=btnhome2)
#    print(w, h)
#    print("after", map[row][col])
 
window.bind("<Key>", move)



def fnpong():
    homeFrame.pack_forget()
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    pongCanvas.pack()
    pongFrame.pack()
    btnhome = Button(pongFrame, text = "home", command = fnlogin, anchor = W)
    btnhome.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    btnhome_window = pongCanvas.create_window(10, 125, anchor=NW, window=btnhome)
    pongCanvas.coords(line, 150, 500, 150, -250)
    line()

def store_position(event):
    global lastx, lasty
    lastx = event.x
    lasty = event.y
    
def on_clicks(event):
    store_position(event)

def on_drags(event):
    global lastx
    global lasty
    pongCanvas.create_line(lastx,lasty,event.x,event.y, fill = NotColour, width = 4)

def line():
    pongCanvas.create_rectangle(150, 300, 150, -250, fill = "red")
    pongCanvas.create_rectangle(1509, 300, 2000, 600, fill = "blue")
    


def click_move(event):
    global movement
    global lastx, lasty
    if click_move == True:
        button.bind('<Button-1>')
        button.drag('<Button-1>')
        canvas.coords(line, 150, 500, 150, -250)



def fntime():
    timeFrame.pack(padx=5,pady=5)
    homeFrame.pack_forget()
    localtime = time.asctime(time.localtime(time.time()))
    timelbl = Label(timeFrame, text=("the current local time is ", localtime))
    timelbl.grid(column=0, row=3)
    btnhome = Button(timeFrame, text="home", command=fnlogin)
    btnhome.grid(column=0, row=0)


def fncalculator():
    if __name__ == '__main__':
      main()


def fncanvas():
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    homeFrame.pack_forget()
    canvasFrame.pack(padx=5,pady=5)
    canvas.pack()
    lastx,lasty =0,0
    canvas.bind("<Button-1>", on_click)
    canvas.bind("<B1-Motion>", on_drag)
    red_id = canvas.create_oval(10,10,30,30, fill = "red")
    blue_id = canvas.create_oval(10, 35, 30, 55, fill = "blue")
    yellow_id = canvas.create_oval(10,60,30 ,80,fill = "yellow")
    green_id = canvas.create_oval(10, 60,30,80,fill = "green")
    black_id = canvas.create_oval(10,85,30,105,fill = "black")
    canvas.tag_bind(red_id, "<Button-1>", set_colour_red)
    canvas.tag_bind(blue_id, "<Button-1>", set_colour_blue)
    canvas.tag_bind(yellow_id, "<Button-1>", set_colour_yellow)
    canvas.tag_bind(green_id, "<Button-1>", set_colour_green)
    canvas.tag_bind(black_id, "<Button-1>", set_colour_black)
    btnhome = Button(canvasFrame, text = "home", command = fnlogin, anchor = W)
    btnhome.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    btnhome_window = canvas.create_window(10, 155, anchor=NW, window=btnhome)
    btnclear = Button(canvasFrame, text = "clear", command =lambda:clear(), anchor = W)
    btnclear.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    btnclear_window = canvas.create_window(10, 125, anchor=NW, window=btnclear)

def clear():
    canvas.delete("all")
    fncanvas()

   


def fnQUIT():
    window.destroy()

window.title("temp operating system")

window.geometry('370x220')

loginFrame = Frame(window)
loginFrame.pack(padx=5,pady=5)

lbl = Label(loginFrame, text="Welcome to temp operating system", bg="orange")
lbl3 = Label(loginFrame, text="press Escape three times to log out")
lbl1 = Label(loginFrame, text="username")
lbl2 = Label(loginFrame, text="password")
lbl.config(font=('Fixedsys',10))


lbl.grid(column=0, row=0)
lbl3.grid(column=0, row=3)
lbl1.grid(column=0, row=1)
lbl2.grid(column=0, row=2)

usr = Entry(loginFrame,width=10)
pas = Entry(loginFrame,show="*",width=10)

usr.grid(column=1, row=1)
pas.grid(column=1, row=2)

btnLogIn = Button(loginFrame, text="log in", command=fnlogin)

btnLogIn.grid(column=1, row=3)

def forcequit(event):
    window.destroy()

window.bind("<Triple-Escape>",forcequit)
