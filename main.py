# this is the start of tkinter window
from tkinter import *
from PIL import ImageTk, Image
window = Tk()
window.title("password generation")
canvas = Canvas(height=200, width=200)
logo_img = ImageTk.PhotoImage(Image.open("lock.png"))
canvas.create_image(image = logo_img)
window.mainloop()