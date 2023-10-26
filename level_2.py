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