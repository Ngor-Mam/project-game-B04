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