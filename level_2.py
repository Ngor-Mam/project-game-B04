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