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

character1 = Image.open("images/main-images/big_character.png")
character_size = character1.resize((360,570))
show_character1 = ImageTk.PhotoImage(character_size)
image1_id = canvas.create_image(200,430, image = show_character1)

character2 = Image.open("images/main-images/small_character.png")
character2_size = character2.resize((230,390))
show_character2 = ImageTk.PhotoImage(character2_size)
character2_id = canvas.create_image(370,490, image = show_character2)

first_coin = Image.open("images/main-images/first_coin.png")
first_coin_size = first_coin.resize((200,300))
show_first_coin = ImageTk.PhotoImage(first_coin_size)
canvas.create_image(1180,250, image = show_first_coin)

second_coin = Image.open("images/main-images/second_coin.png")
second_coin_size = second_coin.resize((190,390))
show_second_coin = ImageTk.PhotoImage(second_coin_size)
second_coin_id = canvas.create_image(1070,400, image = show_second_coin)

third_coin = Image.open("images/main-images/second_coin.png")
third_coin_size = third_coin.resize((190,390))
show_third_coin = ImageTk.PhotoImage(third_coin_size)
third_coin_id = canvas.create_image(1190,500, image = show_third_coin)

canvas.create_text(700,100, text="Timely Coin ", font=("Robus",60,"bold"), fill="white")
canvas.create_text(690,200, text="Chase", font=("Robus",60,"bold"), fill="white")

def button_click_levels():
    print("Button clicked!")
    window.destroy()
    os.system("python levels_game.py") 
button = tk.Button(frame, text="Play Game", command=button_click_levels, bg="white", fg="black", font=("bold", 30),width=10,height=1)
button.place(x = 540, y = 400)
window.resizable(0,0)

move_up = True
def animation_player():
    global move_up
    if move_up:
        canvas.move(image1_id, 0, -5)
        canvas.move(character2_id, 0, -5)
        if canvas.coords(image1_id)[1] <= 400:
            move_up = False
    else:
        canvas.move(image1_id, 0, 5)
        canvas.move(character2_id, 0, 5)
        if canvas.coords(image1_id)[1] >= 500:
            move_up = True
    winsound.PlaySound("sounds/levels_game-sound/sound_level_game.wav",winsound.SND_ASYNC)
    window.after(50, animation_player)
animation_player()

def play_sound():
    winsound.PlaySound("sounds/main_sounds/show_sound.wav", winsound.SND_FILENAME + winsound.SND_LOOP)
sound_thread = threading.Thread(target=play_sound)
sound_thread.start()
window.mainloop()