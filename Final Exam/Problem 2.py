from tkinter import *

class TrafficLights:

    def __init__(self):

        window = Tk()
        window.title("Traffic Light")

        frame = Canvas(window, height=250, width=300)
        frame.pack()

        self.color = StringVar()

        radio_red = Radiobutton(frame, text="Red", bg="red", variable=self.color, value="R", command=self.on_RadioChange)
        radio_red.grid(row=10, column=1)

        radio_yellow = Radiobutton(frame, text="Yellow", bg="yellow", variable=self.color, value="Y", command=self.on_RadioChange)
        radio_yellow.grid(row = 10, column = 2)

        radio_green = Radiobutton(frame, text="Green", bg="green", variable=self.color, value="G", command=self.on_RadioChange)
        radio_green.grid(row = 10, column = 3)

        self.canvas = Canvas(window, width=250, height=300, bg="white")
        self.canvas.pack()

        self.rectangle = self.canvas.create_rectangle(100,50,200,275)
        self.oval_red = self.canvas.create_oval(100, 50, 200, 125, fill="white")
        self.oval_yellow = self.canvas.create_oval(100, 125, 200, 200, fill="white")
        self.oval_green = self.canvas.create_oval(100, 200, 200, 275, fill="white")



        self.color.set('R')
        self.canvas.itemconfig(self.oval_red, fill="red")

        window.mainloop()

    def on_RadioChange(self):
        color = self.color.get()

        if color == 'R':
            self.canvas.itemconfig(self.oval_red, fill="red")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'Y':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="yellow")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'G':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")


TrafficLights()