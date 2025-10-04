import time
from tkinter import *
import random

seconds = SEC = 20

GREEN="#78C841"
RED="#FB4141"
MENTIONER="#A7AAE1"
BLUE = "#34656D"
WHITE = "#FAF8F1"
FONT_NAME= "Courier"
TEXT_FONT="Verdana"
correct_words = 0
typed_words = 0
#text generator
def text_generator():
    words=[]
    with open("common_english_words.csv") as file:
        words = file.read().splitlines()
    text_list = random.choices(words, k=30)
    return text_list

def text_writer(first_bg):
    text.tag_config('first', background=first_bg)
    text.insert(END, text_gen[0] + " ", 'first')
    text.insert(END, text_gen[1:])

def deleter():
    text.delete("1.0", "end")
    text_gen.pop(0)
    typed.delete("1.0", "end")
    text_writer(MENTIONER)

def show_feedback(color):
    text.delete("1.0", "end")
    text_writer(color)
    root.after(500, deleter)

def space_pressed(event):
    global correct_words, typed_words
    if event.keysym == "space":
        input = typed.get("1.0", "end-1c")
        if input.strip() == text_gen[0].strip():
            correct_words +=1
            show_feedback(GREEN)
        else:
            show_feedback(RED)
        typed_words +=1

def start_text():
    text.delete("1.0", "end")
    typed.delete("1.0", "end")
    text_writer(MENTIONER)
    typed.config(state=NORMAL)
    start.config(state=DISABLED)
    start_timer()

def results():
    global correct_words, typed_words
    text.delete("1.0", "end")
    text.insert(END, f"typed words: {typed_words}\n")
    text.insert(END, f"correct words: {correct_words}\n")
    text.insert(END, f"speed: {(correct_words / seconds) * 60} WPM")

def start_timer():
    global SEC
    if SEC == 0 :
        sec_label.config(text = "time finished")
        typed.config(state=DISABLED)
        start.config(state=NORMAL)
        results()
        SEC = seconds
    else:
        sec_label.config(text=str(SEC))
        SEC -=1
        root.after(1000, start_timer)


#UI Setup
root = Tk()
root.title("Typing Test")
root.geometry("800x600")
root.config(bg=BLUE)

logo_label = Label(root,fg=WHITE,bg= BLUE ,text="TYPING MASTER",font=(FONT_NAME, 40))
logo_label.config(padx=30, pady = 30)
logo_label.grid(row=0, column=0)


text_gen = text_generator()
text = Text(root,height=8, width=30,wrap=WORD, font=(TEXT_FONT, 18),padx=10,pady=10)
text.grid(row=1,column=0)

time_label = Label(root,text="TIME: ",font=(TEXT_FONT, 18),bg= BLUE ,fg=WHITE)
time_label.grid(row=1, column=1)

typed= Text(root, height=2, width=30,font=(TEXT_FONT, 18),padx=10,pady=10, cursor="arrow",state=DISABLED)
typed.bind("<KeyPress>",space_pressed)
typed.focus_set()
typed.grid(row=2, column=0)

sec_label = Label(root,font=(TEXT_FONT, 18),bg= BLUE ,fg=WHITE)
sec_label.grid(row=1, column=2)

start = Button(root, height=2, width=10, text="START", command=start_text)
start.grid(row=2,column=1)

root.mainloop()
