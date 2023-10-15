'''
A class that represents a rectangle and renders it using tkinter.
'''
import tkinter as tk
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def render(self):
        top = tk.Toplevel()
        top.title("Rectangle")
        canvas = tk.Canvas(top, width=self.width, height=self.height)
        canvas.pack()
        canvas.create_line(0, 0, self.width, 0)
        canvas.create_line(self.width, 0, self.width, self.height)
        canvas.create_line(self.width, self.height, 0, self.height)
        canvas.create_line(0, self.height, 0, 0)
        top.mainloop()