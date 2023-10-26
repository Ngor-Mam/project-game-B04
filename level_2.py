import tkinter as tk
from PIL import Image, ImageTk
import winsound
import os

window = tk.Tk()
window_width = 1500
window_height = 100
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_height}')
window.attributes('-fullscreen', True)
window.title("Level 3")

frame = tk.Frame(window, width=window_width, height=window_height,)
frame.pack()
canvas = tk.Canvas(frame, width=window_width, height=window_height,)
canvas.pack()

backgroung_level2 = Image.open('images/level_2-images/background_level2.jpg')
backgroung_level2_size = backgroung_level2.resize((window_width, window_height))
show_backgrund_level2 = ImageTk.PhotoImage(backgroung_level2_size)
canvas.create_image(0, 0, image=show_backgrund_level2,anchor="nw" )

button_back = Image.open('images/level_3-images/button_back.png')
button_back_size = button_back.resize((70,70))
btn = ImageTk.PhotoImage(button_back_size)
canvas.create_image(50,50,image=btn)

def button_back():
    print("Button clicked!")
    os.system("python levels_game.py")
    window.destroy()
button = tk.Button(frame, image=btn, command=button_back,bg="black")
button.place(x=10, y=10)

board_score = Image.open("images/level_3-images/background_score.png")
board_score_size = board_score.resize((510,60))
show_board_score = ImageTk.PhotoImage(board_score_size)
canvas.create_image(1050,50,image=show_board_score)

player_1 = Image.open("images/level-1-images/character.png")
player_1_size = player_1.resize((100, 130))
player1 = ImageTk.PhotoImage(player_1_size)
player = canvas.create_image(50, 530, image=player1)



stone1 = Image.open('images/level_2-images/stone.png')
stone1_size = stone1.resize((200, 70))
show_stone1 = ImageTk.PhotoImage(stone1_size)
canvas.create_image(370,500, image=show_stone1,tags="PLATFORM")


stone2 = Image.open('images/level_2-images/stone.png')
stone2_size = stone2.resize((200, 70))
show_stone2 = ImageTk.PhotoImage(stone2_size)
canvas.create_image(810,390, image=show_stone2,tags="PLATFORM")


stone3 = Image.open('images/level_2-images/stone.png')
stone3_size = stone3.resize((200, 70))
show_stone3 = ImageTk.PhotoImage(stone3_size)
canvas.create_image(1100,250, image=show_stone3,tags="PLATFORM")


stone4 = Image.open('images/level_2-images/stone.png')
stone4_size = stone4.resize((200, 70))
show_stone4 = ImageTk.PhotoImage(stone4_size)
canvas.create_image(1250,500, image=show_stone4,tags="PLATFORM")


stone5 = Image.open('images/level_2-images/stone.png')
stone5_size = stone5.resize((200,70))
show_stone5 = ImageTk.PhotoImage(stone5_size)
canvas.create_image(530, 170, image=show_stone5,tags="PLATFORM")


stone6 = Image.open('images/level_2-images/stone.png')
stone6_size = stone6.resize((200,70))
show_stone6 = ImageTk.PhotoImage(stone6_size)
canvas.create_image(190, 270, image=show_stone6,tags="PLATFORM")
coin = Image.open("images/level-1-images/coin.png")
coin_size = coin.resize((40, 40))
coin1 = ImageTk.PhotoImage(coin_size)

coin_positions = [(130, 215),(180, 215),(230, 215),
 (300, 440),(350, 440), (400, 440),(440, 440),
 (460, 120),(510, 120),(560, 120),
(900, 280),(950, 280),(1000, 280),
(1050, 195),(1100, 195),(1150, 195),(1200, 195),
(1200, 400),(1250, 400), (1300, 400)
 ]
coins = []
for position in coin_positions:
    coin = canvas.create_image(position[0], position[1], image=coin1)
    coins.append(coin)

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 864
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 5
TIMED_LOOP = 10


time_remaining = 60
timer_label = tk.Label(frame, text=f"Time: {time_remaining}s", font=("arial", 20))
timer_label.place(x=900, y=30)

score_count = 0
score_label = tk.Label(frame, text=f"Scores: {score_count}/20", font=("arial", 20))
score_label.place(x=1060, y=30)

keyPressed = []
canvas.create_rectangle(1400,1, SCREEN_WIDTH, 650, fill="black", tags="PLATFORM")
canvas.create_rectangle(0,1, SCREEN_WIDTH, 2, fill="black", tags="PLATFORM")

def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.bbox(player)
    platforms = canvas.find_withtag("PLATFORM")
    if coord[0] + dx < 0 or coord[2] + dx > SCREEN_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[2], coord[3] + dy)
    else:
        overlap = canvas.find_overlapping(coord[0] + dx, coord[1] + dy, coord[2] + dx, coord[3])
    for platform in platforms:
        if platform in overlap:
            return False
    return True


def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force - 1)


def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()


def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player, x, 0)
            for i, coin in enumerate(coins):
                if is_overlapping(player, coin):
                    global score_count
                    score_count += 1
                    score_label.config(text=f"Scores: {score_count}/20")
                    canvas.delete(coin)  # Hide the coin
    window.after(TIMED_LOOP, move)


def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)


def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)


def is_overlapping(item1, item2):
    overlap = canvas.find_overlapping(*canvas.bbox(item1))
    return item2 in overlap


def countdown():
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        timer_label.config(text=f"Time: {time_remaining}s")
        window.after(1000, countdown)
        if score_count  == 20 :
            os.system("python game_win.py")
            window.destroy()
            print("Game win")
    else:
        if score_count < 20 :
            os.system("python game_over.py")
            window.destroy()
            print("Game Over")
countdown()
gravity()
def move_player(event):
    player_coords = canvas.coords(player)
    if event.keysym == "Left" and player_coords[0] > 30:
        canvas.move(player, -10, 0)
    elif event.keysym == "Right" and player_coords[0] < SCREEN_WIDTH - 30:
        canvas.move(player, 10, 0)



window.bind("<KeyPress>", move_player)
window.resizable(0, 0)
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)
window.mainloop()


