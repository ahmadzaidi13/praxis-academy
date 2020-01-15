import tkinter as tk

window = tk.Tk()
window.title("pencari nilai akar")

canvas1 = tk.Canvas(window, width = 200, height = 200)
canvas1.pack()

input1 = tk.Entry(window)
canvas1.create_window(100, 100, window=input1)


# mencari nilai cos
import math
def cosvalue():
    x1 = input1.get()
    x2 = int(x1)
    label1 = tk.Label(window, text = math.sqrt(x2))
    canvas1.create_window(100,140, window=label1)


#tombol
tombol1 = tk.Button(text='cari nilai akar', command=cosvalue)
canvas1.create_window(100, 120, window=tombol1)

window.mainloop()