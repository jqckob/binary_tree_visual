import tkinter as tk
from random import randint, sample

#App window configuration
window = tk.Tk()
window.geometry("900x700")
window.config(bg="#BCBCBC")
window.title("Binary Tree")

bg_c = "#BCBCBC"

#class for nodes
class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.x_s = None
        self.y_s = None
        self.parent = None
        self.oval = None
        self.text_node = None
    def show(self, x, y):
        global canvas
        global r
        canvas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill="#727272")
        canvas.create_text(x,y, text=str(self.key), fill="black", font=("Arial", 16))
    def finded(self, x_s, y_s):
        global canvas, r
        self.oval = canvas.create_oval(x_s-r, y_s-r, x_s+r, y_s+r, outline="black", fill="#CE0909")
        self.text_node =canvas.create_text(x_s,y_s, text=str(self.key), fill="black", font=("Arial", 16))
    def rm_rec(self):
        if self.oval:
            canvas.delete(self.oval)
            self.oval = None
        if self.text_node:
            canvas.delete(self.text_node)
            self.text_node = None    

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
            recent.parent = root
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
            recent.parent = root
            canvas.create_line(x-r, y, x-dx, y+dy-r)
            root.left.show(x-dx, y+dy)
    return root

added_nodes = []

def Add_button():
    global root, added_nodes
    global x, y
    text = text_box_add.get().strip()
    if text:
        key = int(text)
        text_box_add.delete(0, tk.END)
        added_nodes.append(key)
        root = adding_node(node(key), root, x, y)

def only_num(char):
    return char.isdigit()

#Buttons, Labels and others
btn_frame =tk.Frame(window, bg="#BCBCBC", width=150)
btn_frame.pack(side="left", fill="y", pady=10, padx=10)
label_1 = tk.Label(btn_frame, text="Functions", font=("Arial", 16), bg=bg_c)
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


#REMOVING RECENT
def Remove_recent():
    global recent, added_nodes, label_rm, root
    if not added_nodes:
        label_rm.config(text="No Tree", fg ="Red")
        return
    removed = added_nodes.pop()
    label_rm.config(text=f"Removed: {removed}", fg="Black")
    canvas.delete("all")
    root = None
    for key in added_nodes:
        root = adding_node(node(key), root, x, y)

rm_recent = tk.Button(btn_frame, font=("Arial", 10), bg=bg_c, text="Remove Recent", command=Remove_recent)
label_rm = tk.Label(btn_frame, font=("Arial", 10), bg=bg_c, text="")
label_rm.grid(row=3, column=1, padx=5)
rm_recent.grid(row=3, column=0, pady=5)

#Remove Whole Tree

def Remove_all():
    global added_nodes, root, label_rm_all, canvas
    if not root:
        label_rm_all.config(text="No Tree",fg ="Red")
        return
    root = None
    canvas.delete("all")
    added_nodes.clear()
    label_rm_all.config(text="Tree Removed", fg="Black")

btn_all_rm = tk.Button(btn_frame, text="Remove all", font=("Arial", 10), bg=bg_c, command=Remove_all)
btn_all_rm.grid(row=4, column=0)

label_rm_all = tk.Label(btn_frame, font=("Arial", 10), bg=bg_c, text="")
label_rm_all.grid(row=4, column=1, padx=5)

#random tree
def randomize():
    global x, y, root, added_nodes
    global repeater
    #Deleting previous tree:
    root = None
    canvas.delete("all")
    added_nodes.clear()

    amount = int(box_amount.get().strip())
    v_range = int(box_range.get().strip())
    if repeater.get() == 0:
        repeat_label.config(text="")
        for i in range(0, amount):
            key = randint(0, v_range)
            added_nodes.append(key)
            root = adding_node(node(key), root, x, y)
    else:
        max_unique = v_range+1
        if amount > max_unique:
            amount = max_unique
            repeat_label.config(text=f"Max unique: {max_unique}", fg="Red")
        else:
            repeat_label.config(text="")

        values = sample(range(0, v_range+1), amount)
        for value in values:
            added_nodes.append(value)
            root = adding_node(node(value), root, x, y)

#Find function
def find_value(node, key=None):
    find_label.config(text="", bg=bg_c, fg="Black")
    if node == None and key == None:
        global root
        if root:
            node = root
            reset_tree(node)
        else:
            find_label.config(text="No Tree", fg ="Red")
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
btn_add = tk.Button(btn_frame, text="Add", font=("Arial", 10),bg=bg_c,command= Add_button)
btn_add.grid(row = 1, column=1, padx=5, pady=5)

#random button
label_rand = tk.Label(btn_frame, text="Random Tree", bg=bg_c,font=("Arial", 16))
label_rand.grid(row=5, columnspan=3, pady=5)

btn_random = tk.Button(btn_frame, text="Generate", bg=bg_c,font=("Arial", 10), height=5, command=randomize)
btn_random.grid(row=7, column=2, rowspan=2)

box_amount = tk.Entry(btn_frame, width=5, font=("Arial", 12),validate="key", validatecommand=is_num)
box_amount.insert(0, str(randint(5, 10)))
box_amount.grid(row=7, column=1, padx=5)
label_amount = tk.Label(btn_frame, font=("Arial", 10), bg=bg_c,text="Amount: ")
label_amount.grid(row=7, column=0)
#repeating numbers
repeater = tk.IntVar()
repeat_on = tk.Radiobutton(btn_frame, font=("Arial", 10), text="repeat", bg=bg_c,variable=repeater, value=0)
repeat_off = tk.Radiobutton(btn_frame, font=("Arial", 10), text="unique",bg=bg_c, variable=repeater, value=1)

repeat_on.grid(row=9, column=0)
repeat_off.grid(row=10, column=0)

repeat_label = tk.Label(btn_frame, font=("Arial", 10), bg=bg_c)
repeat_label.grid(row=10, column=1, columnspan=2)

box_range = tk.Entry(btn_frame, width=5, font=("Arial", 12),validate="key", validatecommand=is_num )
box_range.insert(0, str(randint(5, 10)))
box_range.grid(row=8, column=1, padx=5)
label_range = tk.Label(btn_frame, font=("Arial", 10), bg=bg_c,text="Max range: ")
label_range.grid(row=8, column=0)

#Finding
box_find =tk.Entry(btn_frame, width=5, font=("Arial", 12), validate="key", validatecommand=is_num)
box_find.grid(row=2, column=0)

btn_find = tk.Button(btn_frame, text="Find", font=("Arial", 10), bg=bg_c, command=lambda: find_value(None))
btn_find.grid(row=2, column=1)

find_label = tk.Label(btn_frame, font=("Arial", 10), bg=bg_c, text="")
find_label.grid(row=2, column=2)

#Writing out nodes: inorder, postorder, preorder

def traversal(node):
    if not node:
        return []
    res = []
    if write_out.get() == 0:  # INORDER
        res.extend(traversal(node.left))
        res.append(node.key)
        res.extend(traversal(node.right))
    elif write_out.get() == 1:  # PREORDER
        res.append(node.key)
        res.extend(traversal(node.left))
        res.extend(traversal(node.right))
    else:  # POSTORDER
        res.extend(traversal(node.left))
        res.extend(traversal(node.right))
        res.append(node.key)
    return res


label_write = tk.Label(btn_frame, text="WRITE OUT",bg=bg_c, font=("Arial", 16))
label_write.grid(row=11, columnspan=3, pady=5)
write_out = tk.IntVar()
btn_inorder = tk.Radiobutton(btn_frame, text="INORDER",bg=bg_c, font=("Arial", 10),variable=write_out, value=0)
btn_preorder = tk.Radiobutton(btn_frame, text="PREORDER",bg=bg_c, font=("Arial", 10),variable=write_out, value=1)
btn_postorder = tk.Radiobutton(btn_frame, text="POSTORDER", bg=bg_c,font=("Arial", 10),variable=write_out, value=2)

btn_inorder.grid(row=12, column=0)
btn_preorder.grid(row=13, column=0)
btn_postorder.grid(row=14, column=0)

root = None
recent = None

def show_result():
    if root:
        order = traversal(root)
        label_res.config(text=f"{order}")
    else:
        label_res.config(text="Tree is empty", fg ="Red")

result_frame = tk.Frame(btn_frame, bg=bg_c)
result_frame.grid(row=12, column=1, rowspan=3, columnspan=2, sticky="nw")

label_result = tk.Button(result_frame, text="RESULT", bg=bg_c, font=("Arial", 10), command=show_result)
label_result.grid(row=12, column=2, columnspan=3)
label_res = tk.Message(result_frame, text="", font=("Arial", 10), bg=bg_c)

#Frame Canvas
frame = tk.Frame(window)
frame.pack(side="right", fill="both", expand=True)

#Canvas for tree
canvas_width = 700
canvas_height = 700
canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
canvas.grid(row=2, column=3)
#
r = 15
x = canvas_width//2
y = canvas_height//10
dy = 50


label_res.grid(row=13, column=1, columnspan=2)


window.mainloop()