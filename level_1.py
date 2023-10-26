import tkinter as tk
from PIL import Image, ImageTk
import winsound
import os

window = tk.Tk()
window_width = 1480
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

backgroung_level1 = Image.open('images/level-1-images/background_level1.png')
backgroung_level1_size = backgroung_level1.resize((window_width, window_height))
show_backgrund_level1 = ImageTk.PhotoImage(backgroung_level1_size)
canvas.create_image(0, 0, image=show_backgrund_level1,anchor="nw" )

button_back = Image.open('images/level_3-images/button_back.png')
button_back_size = button_back.resize((70,70))
btn = ImageTk.PhotoImage(button_back_size)
canvas.create_image(50,50,image=btn)

def button_back():
    print("Button clicked!")
    os.system("python levels_game.py")
    window.destroy()
      # Replace "animetion.py" with the correct file path if needed

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

stone1 = Image.open("images/level-1-images/stone.png")
stone1_size = stone1.resize((300, 50))
show_stone1 = ImageTk.PhotoImage(stone1_size)
show_stone1_position = canvas.create_image(350, 525, image=show_stone1,tags="PLATFORM")


stone2 = Image.open("images/level-1-images/stone.png")
stone2_size = stone2.resize((300, 50))
show_stone2 = ImageTk.PhotoImage(stone2_size)
show_stone2_position = canvas.create_image(590, 370, image=show_stone2,tags="PLATFORM")



stone3 = Image.open("images/level-1-images/stone.png")
stone3_size = stone3.resize((230, 50))
show_stone3 = ImageTk.PhotoImage(stone3_size)
show_stone3_position = canvas.create_image(650, 150, image=show_stone3,tags="PLATFORM")


stone4 = Image.open("images/level-1-images/stone.png")
stone4_size = stone4.resize((300, 50))
show_stone4  = ImageTk.PhotoImage(stone4_size)
show_stone4_position = canvas.create_image(930, 480, image=show_stone4,tags="PLATFORM")

stone5= Image.open("images/level-1-images/stone.png")
stone5_size = stone5.resize((300, 50))
show_stone5= ImageTk.PhotoImage(stone5_size)
stone5_size_position = canvas.create_image(1150, 230, image=show_stone5,tags="PLATFORM")

coin_positions = [(300, 480),(350, 480),(400, 480),
 (500, 320),(550, 320),(600, 320),
(600, 105),(650, 105),(700, 105),
(1050, 185),(1100, 185),(1150, 185),(1200, 185),
(850, 430),(900, 430), (950, 430),(1000, 430),
(1200, 560),(1250, 560), (1300, 560)
 ]
coins = []
for position in coin_positions:
    coin = canvas.create_image(position[0], position[1], image=coin1)
    coins.append(coin)