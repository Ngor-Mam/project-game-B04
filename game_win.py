import tkinter as tk
import os
from PIL import Image, ImageTk

window = tk.Tk()
window_width=1600
window_height=100
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_height}')
window.attributes('-fullscreen', True)

frame = tk.Frame(window,width=window_width,height=window_height)
frame.master.title("Game over")
frame.pack()

canvas = tk.Canvas(frame,width=window_width,height=window_height)
canvas.pack()

background_game_over= Image.open('images/game_win-images/background_win_page.png')
background_game_over_size = background_game_over.resize((window_width,window_height))
show_background_game_over = ImageTk.PhotoImage(background_game_over_size)
canvas.create_image(0,0,image=show_background_game_over,anchor='nw')

win_text = Image.open('images/game_win-images/text_win.png')
text_size = win_text.resize((780,350))
show_text = ImageTk.PhotoImage(text_size)
canvas.create_image(650,170,image=show_text)

character_open = Image.open('images/game_win-images/character.png')
character_size = character_open.resize((300,600))
show_character = ImageTk.PhotoImage(character_size)
canvas.create_image(200,350,image=show_character)

score_background_open = Image.open('images/game_win-images/background_score.png')
score_background_size = score_background_open.resize((450,70))
show_score_background = ImageTk.PhotoImage(score_background_size)
canvas.create_image(690,350,image=show_score_background)