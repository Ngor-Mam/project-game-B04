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