from tkinter import *

import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3

reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text , text="00:00")
    my_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    global my_label
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if it's the 8 th rep:
    if reps%2== 0:
        my_label.config(text="long break",fg=RED)
        count_down(long_break_sec)
    elif reps%8== 0:

        my_label.config(text="short break",fg=PINK)
        #if it's 2nd/3rd/4th/6th rep:
        count_down(short_break_sec)
    else:
        # if it's the 1st /3rd/5th/7th rep:

        my_label.config(text="work time",fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:

        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

tick="✔"
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

my_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
my_label.grid(column=2,row=1)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
check_marks.grid(column=2, row=4)

button = Button(text="Start",highlightthickness=0,command=start_timer)
button.grid(column=1,row=3)

button = Button(text="Reset",highlightthickness=0,command=reset_timer)
button.grid(column=3, row=3)

window.mainloop()
