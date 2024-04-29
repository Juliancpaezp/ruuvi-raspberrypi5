import tkinter as tk
from tkinter import Canvas

def draw_shape(shape):
    canvas.delete("all")
    if shape == "Triangle":
        canvas.create_polygon(50, 50, 150, 150, 50, 150, fill="blue")
    elif shape == "Circle":
        canvas.create_oval(50, 50, 150, 150, fill="red")
    elif shape == "Square":
        canvas.create_rectangle(50, 50, 150, 150, fill="green")

root = tk.Tk()
root.title("Shape Drawer")

shapes = ["Triangle", "Circle", "Square"]
selected_shape = tk.StringVar(root)
selected_shape.set(shapes[0])

shape_dropdown = tk.OptionMenu(root, selected_shape, *shapes, command=lambda _: draw_shape(selected_shape.get()))
shape_dropdown.pack(pady=10)

canvas = Canvas(root, width=200, height=200)
canvas.pack()

draw_shape(selected_shape.get())

root.mainloop()
