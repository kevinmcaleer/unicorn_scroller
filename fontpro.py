import tkinter as tk
import tkinter.ttk as ttk
from time import sleep

window = tk.Tk()

height = 5
text = f"Size: {height}"  
details = ttk.Label(text=text)
details.pack()

btn1 = ttk.Button(text='click me')
btn1.pack()

window.mainloop()