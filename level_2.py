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
