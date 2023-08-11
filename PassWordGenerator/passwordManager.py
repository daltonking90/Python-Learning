from tkinter import *
from tkinter import messagebox
import json
from passWordGenerator import PassWordGenerator
import pyperclip

EMAIL_VARIABLE = "daltonking90"
SAVE_FILE = "entries.json"


def generate_password():
    password_generator = PassWordGenerator()
    generated_password = password_generator.create_password()
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)  # copies the password to your clipboard for direct use

def save_entries_to_file(filename):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # messagebox.show(title="Verify text", message="Are you sure this is correct?")

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Whoops!", message="Something was left blank!")
    else:
        try:
            with open(filename, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        data = {
            "website": website,
            "email": email,
            "password": password
        }
        existing_data.append(data)

        with open(filename, "w") as file:
            json.dump(existing_data, file, indent=4)

        reset_entries()
        message_label.config(text="Data saved successfully!")
        window.after(10000, reset_label)


def reset_entries():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    email_entry.insert(END, EMAIL_VARIABLE)
    password_entry.delete(0, END)
    website_entry.focus()


def reset_label():
    message_label.config(text="")


# Canvas setup
window = Tk()
window.title("Password Manager")  # title line
window.config(padx=20, pady=30)

canvas = Canvas(height=200, width=300)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", anchor="e")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", anchor="e")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", anchor="e")
password_label.grid(row=3, column=0)
message_label = Label()
message_label.grid(row=5, column=1)

# Entries aka input rows
website_entry = Entry(width=70)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()  # places the cursor here
email_entry = Entry(width=70)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(END, EMAIL_VARIABLE)  # END makes the cursor appear at the end of the line of text initially
password_entry = Entry(width=42, show="*")
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_password_button = Button(text="Generate Password", command=lambda: generate_password())
generate_password_button.grid(row=3, column=2, sticky="w")
add_button = Button(text="Add", width=59, command=lambda: save_entries_to_file(SAVE_FILE))
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
