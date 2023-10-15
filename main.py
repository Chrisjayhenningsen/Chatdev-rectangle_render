'''
A program that prompts the user for two numerical variables, then renders a rectangle with orthogonal lines of the same relative size as the two variables given.
'''
import tkinter as tk
import tkinter.messagebox as messagebox
from rectangle import Rectangle
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rectangle Renderer")
        self.geometry("400x300")
        self.label1 = tk.Label(self, text="Enter width:")
        self.label1.pack()
        self.entry1 = tk.Entry(self)
        self.entry1.pack()
        self.label2 = tk.Label(self, text="Enter height:")
        self.label2.pack()
        self.entry2 = tk.Entry(self)
        self.entry2.pack()
        self.button = tk.Button(self, text="Render", command=self.render_rectangle)
        self.button.pack()
    def render_rectangle(self):
        try:
            width = int(self.entry1.get())
            height = int(self.entry2.get())
            rectangle = Rectangle(width, height)
            rectangle.render()
        except Exception:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values for width and height.")
if __name__ == "__main__":
    app = Application()
    app.mainloop()