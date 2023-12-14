import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

GRAY = "#4a4a4a"
WHITE = "#ffffff"


# ---------------------- Password Generator --------------------#
def password_generator():
    letters_symbols = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
        '#', '$', '%', '&', '(', ')', '*', '+'
    ]
    password_entry.delete(0, 'end')
    password = ""
    number = 12
    for num in range(number):
        n = random.choice(letters_symbols)
        password += n

    password_entry.insert(0, password)
    pyperclip.copy(password)

# --------------------- Search JSON Data ----------------------#
def search_exising_passwords():
    search_website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if search_website in data:
            search_email = data[search_website]['email']
            search_password = data[search_website]['password']
            messagebox.showinfo(title=f"{search_website}", message=f"Email: {search_email} \nPassword: "
                                                               f"{search_password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_website} exists.")



# --------------------- Save Password -------------------------#

def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    website_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    if len(website) == 0:
        messagebox.showinfo(title="Input Website", message="You did not enter a website.")
    elif len(email) == 0:
        messagebox.showinfo(title="Input Email", message="You did not enter a email.")
    elif len(password) == 0:
        messagebox.showinfo(title="Input Password", message="You did not enter a password.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)


# --------------------- User Interface ------------------------#

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=GRAY)

# Centering Window on the Screen and creating window size.
window_width = 700
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Creating Canvas
canvas = tk.Canvas(width=200, height=200, bg=GRAY, highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Creating Labels
website_label = tk.Label(text="Website:", font=("Arial", 16), fg=WHITE, bg=GRAY, pady=0)
website_label.grid(column=0, row=1)

email_username_label = tk.Label(text="E-Mail/Username:", font=("Arial", 16), fg=WHITE, bg=GRAY, padx=5, pady=0)
email_username_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:", font=("Arial", 16), fg=WHITE, bg=GRAY, padx=0, pady=0)
password_label.grid(column=0, row=3)

# Creating input boxes
website_entry = tk.Entry(window, width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = tk.Entry(window, width=61)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "random@gmail.com")

password_entry = tk.Entry(window, width=33, show="*")
password_entry.grid(column=1, row=3)

# Creating buttons
generate_pass_button = tk.Button(text="Generate Password", width=22, command=password_generator)
generate_pass_button.grid(column=2, row=3, columnspan=1)

add_button = tk.Button(text="Add", width=52, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tk.Button(text="Search", width=22, command=search_exising_passwords)
search_button.grid(column=2, row=1, columnspan=1)

window.mainloop()
