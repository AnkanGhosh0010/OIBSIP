# Random Password Generator GUI 
# Author:  Ankan Ghosh | 18.3.24 | Oasis Infobyte Task 1
'''Develop an advanced password generator with a graphical
   user interface (GUI) using Tkinter or PyQt. Enhance it 
   by including options for password complexity, adherence 
   to security rules, and clipboard integration for easy copying.
'''

import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip


#tkinter initalization: 
root = tk.Tk()
root.title("RPG")

# variables
password_length_var = tk.StringVar(value="12")
password_var = tk.StringVar(value="")
include_letters_var = tk.BooleanVar(value=True)
include_numbers_var = tk.BooleanVar(value=True)
include_symbols_var = tk.BooleanVar(value=True)

# main frame
main_frame = ttk.Frame(root, padding="20").grid(row=0, column=0)

# password length 
ttk.Label(main_frame, text="Password Length:").grid(row=0, column=0)
ttk.Label(main_frame, text="                ").grid(row=0, column=2) #just to adjust the mainframe size
password_length_entry = ttk.Entry(main_frame, textvariable=password_length_var, width=5).grid(row=0, column=1) 

# character types checkbox
include_letters_cb = ttk.Checkbutton(main_frame, text="Include Letters", variable=include_letters_var).grid(row=1, column=0)
include_numbers_cb = ttk.Checkbutton(main_frame, text="Include Numbers", variable=include_numbers_var).grid(row=2, column=0)
include_symbols_cb = ttk.Checkbutton(main_frame, text="Include Symbols", variable=include_symbols_var).grid(row=3, column=0)

def generate_password():
    length = int(password_length_var.get())
    include_letters = include_letters_var.get()
    include_numbers = include_numbers_var.get()
    include_symbols = include_symbols_var.get()

    # error! incase no character type selected 
    if not include_letters and not include_numbers and not include_symbols:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    chars = ""
    if include_letters:
        chars += string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    # random password
    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    pyperclip.copy(password)


# generate button
generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2)


# password display
ttk.Label(main_frame, text="Generated Password:").grid(row=5, column=0)
password_label = ttk.Label(main_frame, textvariable=password_var).grid(row=5, column=1)


# copy to clipboard button
copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
