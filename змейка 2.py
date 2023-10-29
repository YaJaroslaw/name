import time
import random
from tkinter import*
window = Tk()
window.title("змейка")
window.geometry('1000x1000')
window.resizable(False,False)
width = 1000
height = 1000
c = Canvas(width=width, height=height)
c.pack()
snake_size = 6
item_size = 20
snake_list = []
apple_list = []
snake_color = "green"
snake_color1 = "black"
snake_x = width // item_size // 2
snake_y = height // item_size // 2
apple_x = random.randint(1, 48)
apple_y = random.randint(1, 48)
snake_navigation_x = 0
snake_navigation_y = 0
apple_count = 0
game_running = True


def snake_paint(c, x, y):
    global snake_list
    uid1 = c.create_rectangle(x * item_size,y * item_size,
                       x * item_size + item_size,y * item_size + item_size,fill=snake_color1)
    uid2 = c.create_rectangle(x * item_size + 2, y * item_size + 2,
                       x * item_size + item_size - 2,y * item_size + item_size - 2,fill=snake_color)
    snake_list.append([x, y, uid1, uid2])


def snake_del():
    if len(snake_list) >= snake_size:
        temp = snake_list.pop(0)
        c.delete(temp[2])
        c.delete(temp[3])


def snake_move(event):
    global snake_x, snake_y, snake_navigation_x, snake_navigation_y
    if event.keysym == "Right":
        snake_navigation_x = 1
        snake_navigation_y = 0
    if event.keysym == "Left":
        snake_navigation_x = -1
        snake_navigation_y = 0
    if event.keysym == "Up":
        snake_navigation_x = 0
        snake_navigation_y = -1
    if event.keysym == "Down":
        snake_navigation_x = 0
        snake_navigation_y = 1


def snake_eat(c, x1, y1):
    global snake_size, apple_count
    global apple_list
    global apple_x
    global apple_y
    if apple_count <1:
        uid3 = c.create_oval(x1 * item_size, y1 * item_size, x1 * item_size + item_size,
                             y1 * item_size + item_size, fill="black")
        uid4 = c.create_oval(x1 * item_size + 2, y1 * item_size + 2, x1 * item_size + item_size - 2,
                             y1 * item_size + item_size - 2, fill="red")
        apple_x = random.randint(1, 48)
        apple_y = random.randint(1, 48)
        apple_list.append([x1, y1, uid3, uid4])
        apple_count += 1
    if apple_list[0][0] == snake_x and apple_list[0][1] == snake_y:
        c.delete(apple_list[0][2])
        c.delete(apple_list[0][3])
        apple_list.pop()
        apple_count -= 1
        snake_size += 1


def zone():
    global snake_x, snake_y, game_running
    if snake_x > 48 or snake_y > 48 or snake_x < 1 or snake_y < 1:
        game_running = False


def snake_die(head_x, head_y):
    global snake_list, game_running, snake_navigation_x, snake_navigation_y
    if not (snake_navigation_x == 0 and snake_navigation_y == 0):
        for i in range(len(snake_list)):
            if snake_list[i][0] == head_x or snake_list[i][1] == head_y:
                game_running = False


def snake_run():
    global snake_x, snake_y
    snake_x += snake_navigation_x
    snake_y += snake_navigation_y
    snake_paint(c, snake_x, snake_y)
    snake_del()


c.create_rectangle(0, 0, 1000, 1000, fill="red")
c.create_rectangle(20, 20, 980, 980, fill="white")
c.bind_all("<KeyPress-Right>", snake_move)
c.bind_all("<KeyPress-Left>", snake_move)
c.bind_all("<KeyPress-Up>", snake_move)
c.bind_all("<KeyPress-Down>", snake_move)
snake_paint(c, snake_x, snake_y)
while game_running:
    zone()
    snake_eat(c, apple_x, apple_y)
    snake_run()
#   snake_die(snake_x + snake_navigation_x, snake_y + snake_navigation_y)
    window.update_idletasks()
    window.update()
    time.sleep(0.15)


def snake_pass(event):
    pass


c.bind_all("<KeyPress-Right>", snake_pass)
c.bind_all("<KeyPress-Left>", snake_pass)
c.bind_all("<KeyPress-Up>", snake_pass)
c.bind_all("<KeyPress-Down>", snake_pass)



