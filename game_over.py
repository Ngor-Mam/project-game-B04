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

background_over= Image.open('images/game_over-images/background_over_page.png')
background_over_size = background_over.resize((window_width,window_height))
show_background_over = ImageTk.PhotoImage(background_over_size)
canvas.create_image(0,0,image=show_background_over,anchor='nw')

over_text = Image.open('images/game_over-images/game_over_text.png')
text_size = over_text.resize((650,350))
show_text = ImageTk.PhotoImage(text_size)
canvas.create_image(700,170,image=show_text)

character = Image.open('images/game_over-images/character.png')
character_size = character.resize((300,600))
show_character = ImageTk.PhotoImage(character_size)
canvas.create_image(200,350,image=show_character)

score_bg = Image.open('images/game_over-images/background_score.png')
score_bg_size = score_bg.resize((450,70))
show_score_bg = ImageTk.PhotoImage(score_bg_size)
canvas.create_image(690,350,image=show_score_bg)

star_bg = Image.open('images/game_over-images/background_score.png')
star_bg_size = star_bg.resize((340,70))
show_star_bg = ImageTk.PhotoImage(star_bg_size)
canvas.create_image(690,450,image=show_star_bg)

star1 = Image.open('images/game_over-images/star.png')
star1_size = star1.resize((85,85))
show_star = ImageTk.PhotoImage(star1_size)
canvas.create_image(590,450,image=show_star)