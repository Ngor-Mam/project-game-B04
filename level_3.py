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

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 864
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 5
TIMED_LOOP = 10

canvas.create_rectangle(0, 600, SCREEN_WIDTH, 650, fill="black", tags="PLATFORM")
canvas.create_rectangle(1400,1, SCREEN_WIDTH, 650, fill="black", tags="PLATFORM")
canvas.create_rectangle(0,1, SCREEN_WIDTH, 2, fill="black", tags="PLATFORM")

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
window.mainloop()