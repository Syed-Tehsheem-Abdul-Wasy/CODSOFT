import tkinter as tk
import random
import string

# Function to generate a random password
def Generate_Pass():
    Password_Len = int(Length_Entry.get())
    Password_Char = string.ascii_letters + string.digits + string.punctuation
    Generated_Password = ''.join(random.choice(Password_Char) for _ in range(Password_Len))
    Password_Var.set(Generated_Password)

# Create main tkinter window
root = tk.Tk()
root.title("Password Generator")

# Password length input
Length_Label = tk.Label(root, text="Enter password length:")
Length_Label.pack()
Length_Entry = tk.Entry(root)
Length_Entry.pack()

# Generate password button
Generate_Button = tk.Button(root, text="Generate Password", command=Generate_Pass)
Generate_Button.pack()

# Display generated password
Password_Var = tk.StringVar()
Password_Label = tk.Label(root, textvariable=Password_Var, font=("Courier", 12))
Password_Label.pack()

# Start the main event loop
root.mainloop()