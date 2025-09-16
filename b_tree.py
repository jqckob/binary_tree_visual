import tkinter as tk
from random import randint

#App window configuration
window = tk.Tk()
window.geometry("600x600")
window.config(bg="#BCBCBC")
window.title("Binary Tree")

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
    global r, recent
    size = 1.5
    if not root:
        new_node.show(x, y)
        recent = new_node
        return new_node
    if new_node.key >= root.key:
        if root.right:
           size+=0.15
           root.right = adding_node(new_node, root.right, x+dx, y+dy, dx//size)
        else: 
            root.right = new_node
            recent = root.right
            canvas.create_line(x, y+r, x+dx, y+dy-r)
            root.right.show(x+dx, y+dy)
    else:
        if root.left:
            size+=0.15
            root.left = adding_node(new_node, root.left, x-dx, y+dy, dx//size)
        else:
            root.left = new_node
            recent = new_node
            canvas.create_line(x, y+r, x-dx, y+dy-r)
            root.left.show(x-dx, y+dy)
    return root


def Add_button():
    global root
    global x, y
    text = text_box_add.get().strip()
    if text:
        key = int(text)
        text_box_add.delete(0, tk.END)
        root = adding_node(node(key), root, x, y)

def only_num(char):
    return char.isdigit()

#Buttons, Labels and others
btn_frame =tk.Frame(window, bg="#BCBCBC", width=150)
btn_frame.pack(side="left", fill="y", pady=10, padx=10)
label_1 = tk.Label(btn_frame, text="Functions", font=("Arial", 16))
label_1.grid(row=0, columnspan=3, pady=5)
is_num = (btn_frame.register(only_num), '%S')


#Entry
entry_value = str(randint(0, 10))

def on_click(event):
    global entry_value
    if text_box_add.get() == entry_value:
        text_box_add.delete(0, tk.END)  
        text_box_add.config(fg="black")

def out_click(event):
    if text_box_add.get() == "":
        text_box_add.config(fg="#BCBCBC")
        text_box_add.insert(0, entry_value)

def Remove_recent():
    global recent
    pass

text_box_add = tk.Entry(btn_frame, width=12,font=("Arial", 12) ,fg="#BCBCBC",validate="key", validatecommand=is_num)
text_box_add.insert(0, entry_value)
text_box_add.grid(row=1, pady=5)

text_box_add.bind("<FocusIn>", on_click)
text_box_add.bind("<FocusOut>", out_click)

btn_add = tk.Button(btn_frame, text="Add", font=("Arial", 10),command= Add_button)
btn_add.grid(row = 1, column=1, padx=5, pady=5)

#btn_rm_recent = tk.Button(btn_frame, text="Remove recent",font=("Arial", 10), command = Remove_recent)
#btn_rm_recent.grid(row=2, columnspan=3)

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


root = None
recent = None
for i in range(0, 10):
    root = adding_node(node(randint(0, 100)), root, x, y)


window.mainloop()