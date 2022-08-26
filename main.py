from tkinter import *
from tkinter import messagebox
import random
#Generate password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    passowrd_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for sym in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    passowrd_list = passowrd_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(passowrd_list)
    

    password_input.insert(END, string=f"{password}")

def save():
    web = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if web == "" or email == "" or password == "":
        messagebox.showinfo(title="Error", message="You have left some fields empty")
    
    else:
        ok = messagebox.askokcancel(title=web, message=f"You entered the following details\n Website: {web}\n Email: {email}\n Password: {password}")

        if ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web} | {email} | {password}\n")
            
            email_input.delete(0, END)
            website_input.delete(0, END)
            password_input.delete(0, END)


window = Tk()                   
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image_insert = PhotoImage(file="Password Manager\\logo.png")
canvas.create_image(100, 100, image=image_insert)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_label.config(font=("Arial", 10, "bold"))

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_label.config(font=("Arial", 10, "bold"))

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.focus()

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_label.config(font=("Arial", 10, "bold"))

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)

add_button = Button(text="Add", command=save, width=36)
add_button.grid(row=4, column=1, columnspan=2)









    













window.mainloop()