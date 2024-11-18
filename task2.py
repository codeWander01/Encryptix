#  TASK -2
#  PASSWORD GENERATOR TASK

import tkinter as tk
import random
import string

def generate_password():                                                                                                         
        len = int(lenEnter.get())
        char = string.ascii_letters + string.digits + string.punctuation
     
        passwrd = ''.join(random.choice(char) for _ in range(len))
        
        passwrd_entry.delete(0, tk.END) 
        passwrd_entry.insert(0, passwrd)

window = tk.Tk()
window.title("Password Generator Task")
window.geometry("500x500")

length_lbl = tk.Label(window, text="Enter Password Length:",bg="paleturquoise")
length_lbl.pack(pady=20)
lenEnter = tk.Entry(window, width=10)
lenEnter.pack()

# generating the password
generate_but = tk.Button(window, text="Click to Generate Password", command=generate_password,bg="darkorange")
generate_but.pack(pady=20)


passwrd_lbl = tk.Label(window, text="Here is Generated Password",bg="aquamarine")
passwrd_lbl.pack(pady=20)
passwrd_entry = tk.Entry(window, width=30)
passwrd_entry.pack()

# run main application
window.mainloop()