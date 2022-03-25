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
reps = 0
is_clicked = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global is_clicked
    global reps

    is_clicked = False
    reps = 0
    check_marks.config(text="")
    title.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00" )


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def click_start():
    global is_clicked
    if not is_clicked:
        is_clicked = True
        start_timer()


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        title.config(text="Long Break!", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Short Break!", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Work!", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    min = math.floor(count / 60)
    sec = count % 60
    if sec <= 9:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += CHECK_MARK
        check_marks.config(text=marks)
        start_timer()
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


start_button = Button(text="Start", command=click_start)
reset_button = Button(text="Reset", command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
check_marks.grid(column=1, row=3)
window.mainloop()