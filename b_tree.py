import tkinter as tk
from random import randint, sample

#App window configuration
window = tk.Tk()
window.geometry("800x600")
window.config(bg="#BCBCBC")
window.title("Binary Tree")

#class for nodes
class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.x_s = None
        self.y_s = None
    def show(self, x, y):
        global canvas
        global r
        canvas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill="#727272")
        canvas.create_text(x,y, text=str(self.key), fill="black", font=("Arial", 16))
    def finded(self, x_s, y_s):
        global canvas, r
        canvas.create_oval(x_s-r, y_s-r, x_s+r, y_s+r, outline="black", fill="#CE0909")
        canvas.create_text(x_s,y_s, text=str(self.key), fill="black", font=("Arial", 16))

#ADDING NODES
def adding_node(new_node, root, x,y ,dx=80, dy=30):
    global r, recent
    size = 1.5
    if not root:
        new_node.x_s = x
        new_node.y_s = y
        new_node.show(x, y)
        recent = new_node
        return new_node
    if new_node.key >= root.key:
        if root.right:
           if size>1.3: size-=0.1
           root.right = adding_node(new_node, root.right, x+dx, y+dy, dx/size)
        else: 
            new_node.x_s = x+dx
            new_node.y_s = y+dy
            root.right = new_node
            recent = root.right
            canvas.create_line(x+r, y, x+dx, y+dy-r)
            root.right.show(x+dx, y+dy)
    else:
        if root.left:
            if size>1.3: size-=0.1
            root.left = adding_node(new_node, root.left, x-dx, y+dy, dx/size)
        else:
            new_node.x_s = x-dx
            new_node.y_s = y+dy
            root.left = new_node
            recent = new_node
            canvas.create_line(x-r, y, x-dx, y+dy-r)
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

#random tree
def randomize():
    global x, y, root
    global repeater
    #Deleting previous tree:
    if root:
        root = None
        canvas.delete("all")
    amount = int(box_amount.get().strip())
    v_range = int(box_range.get().strip())
    if repeater.get() == 0:
        repeat_label.config(text="")
        for i in range(0, amount):
            root = adding_node(node(randint(0, v_range)), root, x, y)
    else:
        max_unique = v_range+1
        s = set()
        if amount > max_unique:
            amount = max_unique
            repeat_label.config(text=f"Max unique: {max_unique}")
        else:
            repeat_label.config(text="")

        values = sample(range(0, v_range+1), amount)
        for value in values:
            root = adding_node(node(value), root, x, y)

#Find function
def find_value(node, key=None):
    find_label.config(text="")
    if node == None and key == None:
        global root
        if root:
            node = root
            reset_tree(node)
        else:
            find_label.config(text="No Tree")
            return False
    if key == None:
        if box_find.get().strip() == "":
            find_label.config(text="Invalid")
            return False
        else:
            key = int(box_find.get().strip())
            box_find.delete(0, tk.END)
    if node == None:
        find_label.config(text="Not Found")
        return False
    if key == node.key:
        node.finded(node.x_s, node.y_s)
        find_label.config(text="Found")
        return True
    if key < node.key:
        find_value(node.left, key)
    else:
        find_value(node.right, key)
    
def reset_tree(node):
    if node is None:
        return
    node.show(node.x_s, node.y_s)
    reset_tree(node.left)
    reset_tree(node.right)

text_box_add = tk.Entry(btn_frame, width=5,font=("Arial", 12) ,fg="#BCBCBC",validate="key", validatecommand=is_num)
text_box_add.insert(0, entry_value)
text_box_add.grid(row=1, pady=5)

text_box_add.bind("<FocusIn>", on_click)
text_box_add.bind("<FocusOut>", out_click)

#Add button
btn_add = tk.Button(btn_frame, text="Add", font=("Arial", 10),command= Add_button)
btn_add.grid(row = 1, column=1, padx=5, pady=5)

#random button
label_rand = tk.Label(btn_frame, text="Random Tree", font=("Arial", 16))
label_rand.grid(row=5, columnspan=3, pady=5)

btn_random = tk.Button(btn_frame, text="Generate", font=("Arial", 10), height=5, command=randomize)
btn_random.grid(row=7, column=2, rowspan=2)

box_amount = tk.Entry(btn_frame, width=5, font=("Arial", 12), validate="key", validatecommand=is_num)
box_amount.insert(0, str(randint(5, 10)))
box_amount.grid(row=7, column=1, padx=5)
label_amount = tk.Label(btn_frame, font=("Arial", 10), text="Amount: ")
label_amount.grid(row=7, column=0)
#repeating numbers
repeater = tk.IntVar()
repeat_on = tk.Radiobutton(btn_frame, font=("Arial", 10), text="repeat numbers", variable=repeater, value=0)
repeat_off = tk.Radiobutton(btn_frame, font=("Arial", 10), text="don't repeat numbers", variable=repeater, value=1)

repeat_on.grid(row=9, column=0)
repeat_off.grid(row=10, column=0)

repeat_label = tk.Label(btn_frame, font=("Arial", 10))
repeat_label.grid(row=10, column=1, columnspan=2)

box_range = tk.Entry(btn_frame, width=5, font=("Arial", 12), validate="key", validatecommand=is_num )
box_range.insert(0, str(randint(5, 10)))
box_range.grid(row=8, column=1, padx=5)
label_range = tk.Label(btn_frame, font=("Arial", 10), text="Max range: ")
label_range.grid(row=8, column=0)

#Finding
box_find =tk.Entry(btn_frame, width=5, font=("Arial", 12), validate="key", validatecommand=is_num)
box_find.grid(row=2, column=0)

btn_find = tk.Button(btn_frame, text="Find", font=("Arial", 10), command=lambda: find_value(None))
btn_find.grid(row=2, column=1)

find_label = tk.Label(btn_frame, font=("Arial", 10), text="")
find_label.grid(row=2, column=2)

#Frame Canvas
frame = tk.Frame(window)
frame.pack(side="right", fill="both", expand=True)

#Canvas for tree
canvas_width = 600
canvas_height = 600
canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
canvas.grid(row=2, column=3)
#
r = 15
x = canvas_width//2
y = canvas_height//10
dy = 50

root = None
recent = None


window.mainloop()