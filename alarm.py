from threading import Thread
from tkinter.ttk import *
from tkinter import *

from time import sleep
from datetime import datetime
from pygame import mixer

from PIL import ImageTk, Image

# colors
bg_color = '#fff'  # white
col = '#72D2C2'   # cyan
col2 = '#2C2D31'  # black

# window
root = Tk()
root.title("Alarm Clock")
root.geometry("350x150")
root.configure(bg=bg_color)

# frames top
frame_line = Frame(root, width=400, height=5, bg=col)
frame_line.grid(row=0, column=0)

# frame body
frame_body = Frame(root, width=400, height=290, bg=col2)
frame_body.grid(row=1, column=0)

# configuring frame body
img = Image.open('icon3.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

image = Label(frame_body, height=100, image=img, bg=col2)
image.place(x=10, y=10)

name = Label(frame_body, text="Alarm", height=1, font=('Ivy 18 bold'),  bg=col2, foreground="white")
name.place(x=125, y=10)

hour = Label(frame_body, text="hour", height=1, font=('Ivy 10 bold'),  bg=col2, foreground=col)
hour.place(x=127, y=40)
combo_hour = Combobox(frame_body, width=2, font=('arial 15'))
combo_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
combo_hour.current(0)
combo_hour.place(x=130, y=58)

minute = Label(frame_body, text="min", height=1, font=('Ivy 10 bold'),  bg=col2, foreground=col)
minute.place(x=177, y=40)
combo_minute = Combobox(frame_body, width=2, font=('arial 15'))
combo_minute['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "34", "35", "36", "37", "38 ", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60")
combo_minute.current(0)
combo_minute.place(x=180, y=58)

second = Label(frame_body, text="sec", height=1, font=('Ivy 10 bold'),  bg=col2, foreground=col)
second.place(x=227, y=40)
combo_second = Combobox(frame_body, width=2, font=('arial 15'))
combo_second['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "34", "35", "36", "37", "38 ", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60")
combo_second.current(0)
combo_second.place(x=230, y=58)

period = Label(frame_body, text="period", height=1, font=('Ivy 10 bold'),  bg=col2, foreground=col)
period.place(x=277, y=40)
combo_period = Combobox(frame_body, width=3, font=('arial 15'))
combo_period['values'] = ("AM", "PM")
combo_period.current(0)
combo_period.place(x=280, y=58)

def activate():
    a = Thread(target=alarm)
    a.start()

def deactivate():
    print("Deactivate alarm: ", selected.get())
    mixer.music.stop()

selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text="Activate", bg=col2, foreground="white", command=activate, variable=selected)
rad1.place(x=125, y=95)

def sound_alarm():
    mixer.music.load('Avicii - The Nights (Lyrics)(MP3_128K).mp3')
    mixer.music.play()
    selected.set(0)

    rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value=2, text="Deactivate", bg=col2, foreground="white", command=deactivate, variable=selected)
    rad2.place(x=195, y=95)


def alarm():
    while True:
        control = 1
        alarm_hour = combo_hour.get()
        alarm_minute = combo_minute.get()
        alarm_second = combo_second.get()
        alarm_period = combo_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control ==1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:
                            print("Time to take a break")
                            sound_alarm()
        sleep(1)

mixer.init()
root .mainloop()
