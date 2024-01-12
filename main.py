# this is the start of tkinter window
from tkinter import *
from PIL import ImageTk, Image
window = Tk()
import random 
window.title("password generation")
canvas = Canvas(height=200, width=200)

original_image = Image.open("lock.png")

# Resize the image to fit within the canvas
resized_image = original_image.resize((200, 200))

# Convert the resized image to PhotoImage
logo_img = ImageTk.PhotoImage(resized_image)

# Create the image on the canvas
canvas.create_image(100, 100, anchor=CENTER, image=logo_img)
canvas.grid(row=0,column=1)
website_name = Label(text="Website Name")
website_name.grid(row=1, column=0)
email = Label(text="Email")
email.grid(row=2, column=0)
password = Label(text="Password")
password.grid(row=3, column=0)

website_entry =Entry(width=35)
website_entry.grid(row=1, column=1)
email_entry = Entry()
email_entry.grid(row=2, column=1)
password_entry = Entry(width= 35)
password_entry.grid(row=3, column=1)

def generate_password_func():
    password = random.randint(0,10)
    password_entry.insert(0, password)
    

generate_password = Button(text="Generate Password",command=generate_password_func)
generate_password.grid(row=3, column=2)

def add_password_func():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("passwords.txt", "a") as f:
        f.write(website + " |")
        f.write(email + " |")
        f.write(password + "\n")

add_password = Button(text="Add", command=add_password_func)
add_password.grid(row=4,column=1)


window.mainloop()