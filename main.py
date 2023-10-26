import tkinter as tk
from PIL import Image,ImageTk
import os
import winsound
import threading

window = tk.Tk()

window_width = 1600
window_height = 100
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_height}')


frame = tk. Frame(window,width=window_width,height=window_height)
frame.pack()


canvas = tk. Canvas(frame,width=window_width,height=window_height)
canvas.pack()


bg_image = Image.open("images/main-images/background_main.jpg")
bg_image_size = bg_image.resize((window_width, window_height))
background = ImageTk.PhotoImage(bg_image_size)
canvas.create_image(0, 0, image=background,anchor='nw')


def button_exit():
    print("Button clicked!")
    window.destroy()
button = tk.Button(frame, text="Exit", command=button_exit, bg="white", fg="red", font=("bold", 30),width=10,height=1)
button.place(x = 540, y = 500)
window.resizable(0,0)



window.mainloop()