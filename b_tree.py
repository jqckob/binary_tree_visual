import tkinter as tk
import random

#App window configuration
window = tk.Tk()
window.geometry("600x600")
window.config(bg="#BCBCBC")
window.title("Binary Tree")
#Buttons
btn_frame =tk.Frame(window, bg="#BCBCBC", width=150)
btn_frame.pack(side="left", fill="y", pady=10, padx=10)
text_box_add = tk.Entry(btn_frame, width=20)
text_box_add.grid()

#Frame Canvas
frame = tk.Frame(window)
frame.pack(side="right", fill="both", expand=True)

#Canvas for tree
canvas_width = 450
canvas_height = 500
canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
canvas.grid(row=2, column=3)
#
r = 15
x = canvas_width//2
y = canvas_height//10
dy = 50
#class for nodes
class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def show(self, x, y):
        global canvas
        global r
        canvas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill="#727272")
        canvas.create_text(x,y, text=str(self.key), fill="black", font=("Arial", 16))
#ADDING NODES
def adding_node(new_node, root, x,y ,dx=60, dy=50):
    global r
    size = 1.5
    if not root:
        new_node.show(x, y)
        return new_node
    if new_node.key >= root.key:
        if root.right:
           size+=0.15
           root.right = adding_node(new_node, root.right, x+dx, y+dy, dx//size)
        else: 
            root.right = new_node
            canvas.create_line(x, y+r, x+dx, y+dy-r)
            root.right.show(x+dx, y+dy)
    else:
        if root.left:
            size+=0.15
            root.left = adding_node(new_node, root.left, x-dx, y+dy, dx//size)
        else:
            root.left = new_node
            canvas.create_line(x, y+r, x-dx, y+dy-r)
            root.left.show(x-dx, y+dy)
    return root

root = None
for i in range(0, 20):
    root = adding_node(node(random.randint(0, 100)), root, x, y)

window.mainloop()