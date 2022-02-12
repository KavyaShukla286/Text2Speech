from tkinter import *
import pyttsx3

root = Tk()
root.title("Text to Speech")
root.geometry("800x500")
root.resizable(0,0)
root.configure(bg='black')
root.iconbitmap("m.ico")

def talk():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)
    engine.setProperty('voice', voices[1].id)
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0,END)

my_entry = Entry(root, font=("Helvetica", 28))
my_entry.pack(pady=20)

my_button = Button(root,text="Speak",font=('arial',15,'italic bold'), command=talk,activebackground='Tan')
my_button.pack(pady=20)

root.mainloop()