# from tkinter import*
# import random
# GAME_WIDTH=700
# GAME_HEIGHT=700
# SPEED=50
# SPACE_SIZE=50
# BODY_PARTS=3
# SNAKE_COLOR="#00FF00"
# FOOD_COLOR="#FF0000"
# BACKGROUND_COLOR="#000000"

# class snake:
#     def __init__(self):
#         self.body_size = BODY_PARTS
#         self.coordinates = []
#         self.squares = []

#         for i in range(0,BODY_PARTS):
#             self.coordinates.append([0, 0])

#         for x, y in self.coordinates:
#             square = canvas.create_rectangle(x, y, x + SPACE_SIZE,fill_color = SNAKE_COLOR,tag="snake")
#             self.squares.append(square)

# class food:
#     def __init__(self):
#         x=random.randint((0,GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
#         Y=random.randint((0,GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
#         self.coordinates=[x, y]

#         canvas.create_oval(x, y , x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# def next_turn(snake, food):
#     x, y= snake.coordinates[0]
#     if direction=="up":
#         y -= SPACE_SIZE
#     elif direction=="down":
#         y += SPACE_SIZE    
#     elif direction=="left":
#         x -= SPACE_SIZE
#     elif direction=="right":
#         x += SPACE_SIZE
#     snake.coordinates.insert(0, (x, y))
#     square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
#     snake.squares.insert(0, square)
#     if x == food.coordinates[0] and y == food.coordinates[i]:
#         global score
#         score+=1
#         label.config(text="score:{}".format(score))
#         canvas.delete("food")
#         food = Food()
#     else:
#         del snake.coordinates[-1]
#         canvas.delete(snake.squares[-1])
    
#         del snake.squares[-1]
#     if check_collisions(snake):
#         game_over()

#     else:


#         window.after(SPEED, next_turn, snake, food)
# def change_direction(new_direction):
#     global direction
#     if new_direction == 'left':
#         if direction != 'right':
#             direction = new_direction
#     elif new_direction == 'right':
#         if direction != 'left':
#             direction = new_direction
#     elif new_direction == 'up':
#         if direction != 'down':
#             direction = new_direction
#     elif new_direction == 'down':
#         if direction != 'up':
#             direction = new_direction




# def check_collisions():
#     x, y = snake.coordinates[0]

#     if x < 0 or x >= GAME_WIDTH:
#         return True
#     elif y < 0 or y >= GAME_HEIGHT:
#         return True
    
#     for body_part in snake.coordinates[1:]:
#         if x == body_part[0] and y == body_part[1]:
#             print("GAME OVER")
#             return True
#     return False

# def game_over():
#     canvas.delete(ALL)
#     canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")


    
# window = Tk()
# window.title("snake game")
# window.resizable(False, False)
# score=0
# direction="down"
# label=Label(window, text="score:{}".format(score), font=('consolas',40))
# label.pack()
# canvas=Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT,width=GAME_WIDTH)
# canvas.pack()
# window.update()
# window_width=window.winfo_width()
# window_height=window.winfo_height()
# screen_width=window.winfo_screenwidth()
# screen_height=window.winfo_screenheight()


# x=int((screen_width/2)-(window_width/2))
# y=int((screen_height/2)-(window_height/2))
# window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# window.bind('<left>', lambda event: change_direction('left'))
# window.bind('<right>', lambda event: change_direction('right'))
# window.bind('<up>', lambda event: change_direction('up'))
# window.bind('<down>', lambda event: change_direction('down'))
# snake = snake()
# food = food()
# next_turn(snake, food)
# window.mainloop()

# import pyautogui as pg
# while True:
#     a=pg.confirm("except me as i am" ,buttons=["yes","No"])
#     if a=="yes":
#         break     




# classroom
# workshop


from tkinter import*
root=Tk()
root.geometry('600x300+50+150')
root.resizable(1,1)
root.title("my first application")
root.iconbitmap("C:\\Users\\agnih\\Downloads\\python.py.ico")
root.config(bg="pink")
def click():
    # print("my first application")
    x=a.get()
    b.set("hi"+x)
    # print(x)
# LABEL
lbl=Label(root,text="Palak",font=("Ariel",20,'bold'),fg='green',bg="yellow")
# lbl.pack(side='top')
# pack contains position
# lbl.place(x=10,y=50)
# place contains x and y axis
lbl.grid(row=0,column=1)
# grid contains row and column
lbl1=Label(root,text="Agnihotri",font=("Ariel",20,'bold'),fg='green',bg="yellow")
# lbl1.pack(side='bottom')
# lbl1.place(x=10,y=110)
lbl1.grid(row=1,column=2)
#ENTRY BOX
a=StringVar()
ent=Entry(root,font=('Ariel',20),fg='yellow',bg='red',textvariable=a)
ent.place(x=10,y=160,width=100,height=67)
# ent.grid(row=10,column=3)
b=StringVar()
ent1=Entry(root,font=('Ariel',20),fg='yellow',bg='red',textvariable=b)
ent1.place(x=300,y=160,width=100,height=67)

#BUTTONS
but=Button(root,font=("calibri",20),bg="black",fg="white",text="click",command=click)
but.place(x=150,y=200,width=100,height=50)

root.mainloop()


 
