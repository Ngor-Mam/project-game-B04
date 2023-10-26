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

backgroung_level3 = Image.open('images/level_3-images/background_level3.png')
backgroung_level3_size = backgroung_level3.resize((window_width, window_height))
show_backgrund_level3 = ImageTk.PhotoImage(backgroung_level3_size)
canvas.create_image(0, 0, image=show_backgrund_level3,anchor="nw" )

button_back = Image.open('images/level_3-images/button_back.png')
button_back_size = button_back.resize((70,70))
btn = ImageTk.PhotoImage(button_back_size)
canvas.create_image(50,50,image=btn)
def button_click():
    print("Button clicked!")
    window.destroy()
    os.system("python levels_game.py") 
button = tk.Button(frame, image=btn, command=button_click,bg="black")

board_score = Image.open("images/level_3-images/background_score.png")
board_score_size = board_score.resize((510,60))
show_board_score = ImageTk.PhotoImage(board_score_size)
canvas.create_image(1050,50,image=show_board_score)

time_remaining = 80
timer_label = tk.Label(frame, text=f"Time: {time_remaining}s", font=("arial", 20))
timer_label.place(x=900, y=30)

score_count = 0
score_label = tk.Label(frame, text=f"Scores: {score_count}/20", font=("arial", 20))
score_label.place(x=1060, y=30)

player_1 = Image.open("images/level-1-images/character.png")
player_1_size = player_1.resize((100, 130))
player1 = ImageTk.PhotoImage(player_1_size)
player = canvas.create_image(50, 530, image=player1)

stone_first = Image.open('images/level_3-images/stone.png')
stone_first_size = stone_first.resize((200,140))
show_stone_first = ImageTk.PhotoImage(stone_first_size)
canvas.create_image(180, 285, image=show_stone_first, tags="PLATFORM")

stone_second = Image.open('images/level_3-images/stone.png')
stone_second_size = stone_second.resize((200, 180))
show_stone_second = ImageTk.PhotoImage(stone_second_size)
canvas.create_image(500,500, image=show_stone_second, tags="PLATFORM")

stone_third = Image.open('images/level_3-images/stone.png')
stone_third_size = stone_third.resize((200, 140))
show_stone_third = ImageTk.PhotoImage(stone_third_size)
canvas.create_image(740,350, image=show_stone_third, tags="PLATFORM")

stone_four = Image.open('images/level_3-images/stone.png')
stone_four_size = stone_four.resize((300, 140))
show_stone_four = ImageTk.PhotoImage(stone_four_size)
canvas.create_image(1010,260, image=show_stone_four, tags="PLATFORM")

stone_five = Image.open('images/level_3-images/stone.png')
stone_five_size = stone_five.resize((200, 180))
show_stone_five = ImageTk.PhotoImage(stone_five_size)
canvas.create_image(1250,500, image=show_stone_five, tags="PLATFORM")

# Coin
coin = Image.open("images/level-1-images/coin.png")
coin_size = coin.resize((40, 40))
coin1 = ImageTk.PhotoImage(coin_size)

# Create three coins
coin_positions = [(100, 200),(150, 200),(200, 200),
 (200, 560),(250, 560), (300, 560),(350, 560),
 (460, 400),(510, 400),(560, 400),
(700, 265),(750, 265),(800, 265),
(900, 175),(950, 175),(1000, 175),(1050, 175),
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
keyPressed = []

canvas.create_rectangle(0, 600, SCREEN_WIDTH, 650, fill="black", tags="PLATFORM")
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
    if score_count == 20:
            os.system("python game_win.py")
            window.destroy()
            print("Level completed!")    
    # else:
    #     if score_count == 20:
    #         os.system("python game_win.py")
    #         window.destroy()
    #         print("Level completed!")
    #     if score_count < 20 and time_remaining==0:
    #         os.system("python game_over.py")
    #         window.destroy()
    #         print("Game Over")    
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