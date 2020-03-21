from tkinter import *
from tkinter import messagebox
import webbrowser
import numpy as numpy
import os, time
import ast

tank_numbers_set = set()
url = 'https://www.youtube.com/watch?v=heAc2XhF1uA'

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def Average(lst): 
    return sum(lst) / len(lst)

def calculate_number_of_all_tanks():
    entry_text = input_field.get()
    tank_number_list = []
    if (entry_text == ""):
        result_label.config(text="Insert a tank number or a comma separated list of tank numbers to calculate the probable number of all tanks")
    elif (is_number(entry_text) and int(entry_text) >= 0): 
        tank_numbers_set.add(int(input_field.get()))

        for tank_number in tank_numbers_set:
            tank_number_list.append(tank_number)

        result_label.config(text="The total amount of tanks produced probably is about " + str(int(Average(tank_number_list)*2)) + " tanks")
        tank_numbers_label.config(text="You have registered the following tank numbers: " + str(tank_numbers_set))

    elif ("." in entry_text or "-" in entry_text):
        result_label.config(text="\"" + input_field.get() + " \"" + "is not a valid, positive integer or list of integers!")

    else:
        try:
            res = ast.literal_eval(input_field.get())
            for tank_number in res:
                tank_number_list.append(tank_number)
                tank_numbers_set.add(int(tank_number))

            result_label.config(text="The total amount of tanks produced probably is about " + str(int(Average(tank_number_list)*2)) + " tanks")
            tank_numbers_label.config(text="You have registered the following tank numbers: " + str(tank_numbers_set))
        except:
            result_label.config(text="\"" + input_field.get() + " \"" + "is not a valid integer or list of integers!")

def reset():
        print("Reset program...")
        entry_text = ""
        tank_number_list = []
        result_label.config(text="")
        tank_numbers_label.config(text="")
        tank_numbers_set.clear()

def open_URL():
    webbrowser.open(url)
        
def action_get_info_dialog():

	m_text = "\
************************\n\
Autor: Michael Persch\n\
Date: 18.03.20\n\
Version: 0.5\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")
        
window = Tk()
window.resizable(0, 0)
window.title("Tank Calculator")

my_label = Label(window, text="Enter a tank number or list of comma separated numbers from the set of all tanks: ")

result_label = Label(window)

tank_numbers_label = Label(window)

input_field = Entry(window, bd=5, width=40)

calculate_button = Button(window, text="Calculate", command=calculate_number_of_all_tanks)
reset_button = Button(window, text="Reset", command=reset)

my_label.grid(row = 0, column = 0)
input_field.grid(row = 0, column = 1)
calculate_button.grid(row = 1, column = 0)
reset_button.grid(row = 1, column = 1)
result_label.grid(row = 2, column = 0, columnspan = 2)
tank_numbers_label.grid(row = 3, column = 0, columnspan = 2)

menu_bar = Menu(window)

action_menu = Menu(menu_bar, tearoff=0)
help_menu = Menu(menu_bar, tearoff=0)

action_menu.add_command(label="Calculate", command=calculate_number_of_all_tanks)
action_menu.add_separator()
action_menu.add_command(label="Reset", command=reset)
action_menu.add_separator()
action_menu.add_command(label="Learn more...", command=open_URL)
action_menu.add_separator()
action_menu.add_command(label="Exit", command=window.quit)

help_menu.add_command(label="Info!", command=action_get_info_dialog)

menu_bar.add_cascade(label="Actions", menu=action_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)          

window.mainloop()