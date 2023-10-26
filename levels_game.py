import tkinter as tk
from PIL import Image,ImageTk
import winsound
import threading
import os
windows = tk.Tk()
windows_width = 1600
windows_height = 100
windows_width = windows.winfo_screenwidth()
windows_height = windows.winfo_screenheight()
windows.geometry(f'{windows_width}x{windows_height}')

frame = tk.Frame(windows,width=windows_width,height=windows_height)
frame.pack()

canvas = tk.Canvas(frame,width=windows_width,height=windows_height)
canvas.pack()

bg_image = Image.open("images/levels_game-images/background_level.jpg")
bg_image_size = bg_image.resize((windows_width,windows_height))
background = ImageTk.PhotoImage(bg_image_size)
background_level = canvas.create_image(0, 0, image=background,anchor='nw')

def link_main():
    print("Button clicked!")
    windows.destroy()
    os.system("python main.py")
button = tk.Button(frame, text="Back", command=link_main, bg="green", fg="white", font=("bold", 30))
button.place(x = 30, y = 30)
windows.resizable(0,0)

text_level = Image.open("images/levels_game-images/level_text.png")
text_level_size = text_level.resize((520,230))
show_text_level = ImageTk.PhotoImage(text_level_size)
canvas.create_image(620,67, image = show_text_level)