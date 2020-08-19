#Name:- Ritesh Mahendra Wankhede
# Python program to generate random 
# password using Tkinter module 
import random 

from tkinter import *
import paperclip
from tkinter.ttk import *
  
# Function for calculation of password 
def low(): 
    entry.delete(0, END) 
  
    # Get the length of passowrd 
    length = var1.get() 
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
    lower = "abcdefghijklmnopqrstuvwxyz"
    uplow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    uplownums="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz0123456789"
    uplownumssym="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    
    password = "" 
  
    # if strength selected is low 
    if var.get() == 1: 
        for i in range(0, length): 
            password = password + random.choice(upper) 
        return password 
  
    # if strength selected is medium 
    elif var.get() == 0: 
        for i in range(0, length): 
            password = password + random.choice(lower) 
        return password 
  
    # if strength selected is strong 
    elif var.get() == 3: 
        for i in range(0, length): 
            password = password + random.choice(uplow) 
        return password 
     
    
    elif var.get()==4:
        for i in range(0,length):
            password=password+random.choice(numbers)
        return password
    
    elif var.get()==5:
        for i in range(0,length):
            password=password+random.choice(uplownums)
        return password
    
    elif var.get()==6:
        for i in range(0,length):
            password=password+random.choice(uplownumssym)
        return password
        
    else: 
        print("Please choose an option") 
  
  
# Function for generation of password 
def generate(): 
    password1 = low() 
    entry.insert(10, password1) 
  
  
# Function for copying password to clipboard 
def copy1(): 
    random_password = entry.get() 
    pyperclip.copy(random_password) 
  
  
# Main Function 
  
# create GUI window 
root = Tk() 
var = IntVar() 
var1 = IntVar() 
  
# Title of your GUI window 
root.title("Random Password Generator") 
  
# create label and entry to show 
# password generated 
Random_password = Label(root, text="Password") 
Random_password.grid(row=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 
  
# create label for length of password 
c_label = Label(root, text="Length") 
c_label.grid(row=1) 
  
# create Buttons Copy which will copy 
# password to clipboard and Generate 
# which will generate the password 
copy_button = Button(root, text="Copy", command=copy1) 
copy_button.grid(row=0, column=2) 
generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=2, column=0) 
  
# Radio Buttons for deciding the 
# strength of password 
# Default strength is Medium 
radio_upper= Radiobutton(root, text="Uppercase", variable=var, value=1) 
radio_upper.grid(row=3, column=0, sticky='W') 
radio_lower = Radiobutton(root, text="Lowercase", variable=var, value=0) 
radio_lower.grid(row=4, column=0, sticky='W') 
radio_uplow = Radiobutton(root, text="Upper+Lower", variable=var, value=3) 
radio_uplow.grid(row=5, column=0, sticky='W') 
radio_numbers = Radiobutton(root, text="numbers", variable=var, value=4) 
radio_numbers.grid(row=6, column=0, sticky='W') 
radio_uplownums = Radiobutton(root, text="Upper+Lower+Num", variable=var, value=5) 
radio_uplownums.grid(row=7, column=0, sticky='W') 
radio_uplownumssym = Radiobutton(root, text="Upper+Lower+Num+Sym", variable=var, value=6) 
radio_uplownumssym.grid(row=8, column=0, sticky='W') 


combo = Combobox(root, textvariable=var1) 
  
# Combo Box for length of your password 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
                   17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1) 
  
# start the GUI 
root.mainloop() 
