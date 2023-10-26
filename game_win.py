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