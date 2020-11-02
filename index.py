# importing everything
from tkinter import *

# setting the up the screen
root = Tk()
root.title('GUI calculater')

# making the display box
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# making the buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg="#1477DA")
button_2 = Button(root, text="2", padx=40, pady=20, bg="#1477DA")
button_3 = Button(root, text="3", padx=40, pady=20, bg="#1477DA")
button_4 = Button(root, text="4", padx=40, pady=20, bg="#1477DA")
button_5 = Button(root, text="5", padx=40, pady=20, bg="#1477DA")
button_6 = Button(root, text="6", padx=40, pady=20, bg="#1477DA")
button_7 = Button(root, text="7", padx=40, pady=20, bg="#1477DA")
button_8 = Button(root, text="8", padx=40, pady=20, bg="#1477DA")
button_9 = Button(root, text="9", padx=40, pady=20, bg="#1477DA")
button_0 = Button(root, text="0", padx=40, pady=20, bg="#1477DA")
button_clear = Button(root, text="Clear", padx=79, pady=20, bg="green")
button_add = Button(root, text="+", padx=39, pady=20, bg="red")
button_equal = Button(root, text="=", padx=91, pady=20, bg="yellow")

# displaying the buttons on the screen
# row 3 buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
# row 2 buttons
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
# row 1 buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
# special buttons
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)


