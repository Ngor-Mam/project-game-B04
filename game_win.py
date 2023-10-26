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

star_background_open = Image.open('images/game_win-images/background_score.png')
star_background_size = star_background_open.resize((340,70))
show_star_background = ImageTk.PhotoImage(star_background_size)
canvas.create_image(690,450,image=show_star_background)

star1_open = Image.open('images/game_win-images/star.png')
star1_size = star1_open.resize((85,85))
show_star1 = ImageTk.PhotoImage(star1_size)
canvas.create_image(590,450,image=show_star1)

star2_open = Image.open('images/game_win-images/star.png')
star2_size = star2_open.resize((85,85))
show_star2 = ImageTk.PhotoImage(star2_size)
canvas.create_image(680,450,image=show_star2)
#------star3------
star3_open = Image.open('images/game_win-images/star.png')
star3_size = star3_open.resize((85,85))
show_star3 = ImageTk.PhotoImage(star3_size)
canvas.create_image(780,450,image=show_star3)

button_back_background_open = Image.open('images/game_win-images/star.png')
button_back_background_size = star_background_open.resize((340,70))
show_button_back_background = ImageTk.PhotoImage(button_back_background_size)

button_play_background_open = Image.open('images/game_win-images/background_score.png')
button_play_background_size = star_background_open.resize((340,70))
show_button_play_background = ImageTk.PhotoImage(button_play_background_size)

def button_back():
    os.system("python levels_game.py")  # Replace "levels_game.py" with the correct file path if needed
    window.destroy()


button = tk.Button(frame, text="Back", command=button_back, bg="Saddle Brown", fg="white", font=("Arial", 32))
button.place(x=460, y=550)

def button_retry():
    os.system("python levels_game.py")  # Replace "levels_game.py" with the correct file path if needed
    window.destroy()


button = tk.Button(frame, text="Retry", command=button_retry, bg="Saddle Brown", fg="white", font=("Arial", 32))
button.place(x=720, y=550)

board_background_open = Image.open('images/game_win-images/background_score.png')
board_background_size = board_background_open.resize((340,300))
show_board_background = ImageTk.PhotoImage(board_background_size)
canvas.create_image(1140,430,image=show_board_background)