from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("Helvetica", 18, "normal")
BLACK = "#000000"
MAROON = "#3D0000"
DARK_RED = "#950101"
RED = "#FF0000"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_numbers + pass_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="Fields Missing", message="Website field is empty. Please enter a website.")
        return
    elif len(password) == 0:
        messagebox.showerror(title="Fields Missing", message="Password field is empty. Please enter a password.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Website: {website}"
                                                  f" \nEmail: {username} \nPassword: {password} \n Is it okay to save?")
    if is_ok:
        with open("data.txt", "a") as info_doc:
            info_doc.write(f"{website} | {username} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BLACK)

canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT, fg=DARK_RED, bg=BLACK)
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:", font=FONT, fg=DARK_RED, bg=BLACK)
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=FONT, fg=DARK_RED, bg=BLACK)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(font=FONT, width=35, bg=DARK_RED)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
username_entry = Entry(font=FONT, width=35, bg=DARK_RED)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "grady.debonair@gmail.com")
password_entry = Entry(font=FONT, width=22, bg=DARK_RED)
password_entry.grid(column=1, row=3)

# Buttons
generate_pass_button = Button(text="Generate Password", font=("Helvetica", 12, "normal"), bg=DARK_RED,
                              command=generate_password)
generate_pass_button.grid(column=2, row=3, padx=8)
add_button = Button(text="Add", width=36, font=("Helvetica", 12, "normal"), bg=DARK_RED, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
