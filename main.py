from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK="✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec <= 9:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        window.after(1000, count_down, count -1)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=228, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer) # add command
reset_button = Button(text="Reset") # add command
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_marks = Label(text=CHECK_MARK, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
check_marks.grid(column=1, row=3)
window.mainloop()