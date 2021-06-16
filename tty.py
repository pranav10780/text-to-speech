import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

class Widget():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("TTS")
        self.root.resizable(0,0)
        self.root.configure(background="pink")
        self.label = tk.Label(text="What you want me to speak?",bg="pink",fg="brown",font="Arial 35 bold")
        self.label.pack()
        self.entry = tk.Entry(font="Arial 25",width=30)
        self.entry.pack()
        self.button = tk.Button(text="SPEAK",bg="red",fg="brown",font="Arial 35 bold",command=self.clicked)
        self.button.pack()
        self.root.mainloop()

    def clicked(self):
        text = self.entry.get()
        self.speak(text)

    def speak(self,text):
        engine.say(text)
        engine.runAndWait()


if __name__ == "__main__":
    temp = Widget()