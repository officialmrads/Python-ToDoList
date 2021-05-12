import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import *
import time
import speech_recognition as sr

class Todo:
    def __init__(self,root):
        self.root = root
        self.root.geometry("300x500")
        self.root.title("Smart ToDo")
        self.root.resizable(False, False)
        self.today = datetime.now()

        self.img = tk.PhotoImage(file="icon\wallpaper.png")
        self.lbl = tk.Label(self.root, image=self.img, width=400, height=200)
        self.lbl.place(x=0, y=0)

        self.s1 = StringVar()
        self.entry = ttk.Entry(self.root, font="System 16", textvariable=self.s1)
        self.entry.place(x=3, y=460, height=36, width=200)

        self.bt1 = ttk.Button(self.root, text="ADD", command=self.add_list)
        self.bt1.place(x=205, y=460, height=36, width=45)

        self.mic_img = tk.PhotoImage(file="microphone.png")
        self.bt3 = ttk.Button(root, image=self.mic_img , command = self.speech)
        self.bt3.place(x=252, y=460, height=36, width=45)

        self.timeText = ttk.Label(self.root,  text = '' ,  font=("Ariel", 22) )
        self.timeText.place( x = 88 , y = 50)
        self.update_timeText()

        self.root.config(bg = "#383838")



    def run(self):
        self.root.mainloop()

    def add_list(self):

        self.todotask = self.s1.get()
        global next
        self.lb2 = ttk.Label(self.root, text=self.todotask, font="System 16" , command =self.entry.delete(0 ,100))
        self.lb2.place(x=3, y=212 + next, height=36, width=200)

        self.bt2 = ttk.Button(root, text="Delete", command=self.del_button)
        self.bt2.place(x=205, y=212 + next, height=36, width=91)
        next = next + 40


    def del_button(self):
        self.lb2.destroy()
        self.bt2.destroy()

    def update_timeText(self):
        # Get the current time, note you can change the format as you wish
        self.current = time.strftime("%H:%M:%S")
        # Update the timeText Label box with the current time
        self.timeText.configure(text=" " + self.current + "\n" + self.today.strftime(('%d/%b/%y')))
        # Call the update_timeText() function after 1 second
        self.root.after(1000, self.update_timeText)

    def speech(self):

        self.r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak:")
            self.audio = self.r.listen(source)

            try:
                self.text = self.r.recognize_google(self.audio)
                print("You said " + self.text)
                self.entry.config(textvariable = self.text)

            except:
                print("Could not understand audio")



root = tk.Tk()
next = 0
obj = Todo(root)
obj.run()