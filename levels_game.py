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

board_instruction = Image.open("images/levels_game-images/borad_instruction.png")
board_instruction_size = board_instruction.resize((1000,430))
show_board_instruction = ImageTk.PhotoImage(board_instruction_size)
canvas.create_image(635,460, image=show_board_instruction)

canvas.create_text(450,390, text=".  Count coins and follow time", font=("Robus",15,"bold"), fill="black")
canvas.create_text(420,430, text=".  lost when caught with", font=("Robus",15,"bold"), fill="black")
canvas.create_text(360,465, text="   obstacle", font=("Robus",15,"bold"), fill="black")
canvas.create_text(440,500, text=".  winning when got a lots of", font=("Robus",15,"bold"), fill="black")
canvas.create_text(440,540, text="   coin before time or on time", font=("Robus",15,"bold"), fill="black")

canvas.create_text(750,390, text=".   Key to play:", font=("Robus",15,"bold"), fill="black")
canvas.create_text(790,430, text=".   R = go right", font=("Robus",15,"bold"), fill="black")
canvas.create_text(783,460, text=".   L = go left", font=("Robus",15,"bold"), fill="black")
canvas.create_text(799,490, text=".   Space = jump", font=("Robus",15,"bold"), fill="black")

#