from customtkinter import *
from tkinter import messagebox
import sqlite3

def ct():
    conn = sqlite3.connect('restaurant.db')
    cursor = conn.cursor()
    conn.execute('''CREATE TABLE IF NOT EXISTS orderss (
    name TEXT,
    dish TEXT,
    drink TEXT)
    ''')
    conn.commit()
    conn.close()

def insert_employee(name, dish, drink):
    conn = sqlite3.connect('restaurant.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orderss (name,dish,drink) VALUES (?,?,?)',
                   (name, dish, drink))
    conn.commit()
    conn.close()

def insert():
    name = name_entry.get()
    dish = var1.get()
    drink = var2.get()
    insert_employee(name, dish, drink)

ct()

root = CTk()
root.geometry('620x230')
root.config(bg='#161C25')
root.resizable(False,False)

font1 = ('Arial', 20, 'bold')

title = CTkLabel(root, text='Welcome to the restaurant app', font=CTkFont(size=30))
title.pack(pady=15)

name_label = CTkLabel(root, font=font1, text='Enter your name here:', bg_color='#161C25', text_color='#fff')
name_label.place(x=20, y=60)

name_entry = CTkEntry(root, font=font1, fg_color='#161C25', width=360)
name_entry.place(x=240, y=60)

dish_label = CTkLabel(root, font=font1, text='Chose your dish:', bg_color='#161C25')
dish_label.place(x=20, y=100)

options = ['soup', 'borscht', 'potatoes with cutlets', 'cabbage rolls', 'french fries', 'burger']
var1 = StringVar()

dish_options = CTkComboBox(root, font=font1, width=410, variable=var1, values=options, state='readonly')
dish_options.set('burger')
dish_options.place(x=190, y=100)

drink_label = CTkLabel(root, font=font1, text='Chose your drink:', bg_color='#161C25')
drink_label.place(x=20, y=140)

optionn = ['coffe(latte)', 'coffe(Americano)', 'coffe(Glasse)', 'tea(Green)', 'tea(White)','tea(Black)', 'lemonade(Berry)','lemonade(Coconut)','lemonade(Tropical)', 'cocktail(Mojito)', 'cocktail(Bumblebee)','cocktail(Classic)', 'martini(Rosato)', 'martini(Fiero)','martini(Bianco)', 'beer(Brown Ale)','beer(Porter)','beer(Stout)']
var2 = StringVar()

drink_options = CTkComboBox(root, font=font1, width=400, variable=var2, values=optionn, state='readonly')
drink_options.set('coffe(latte)')
drink_options.place(x=200, y=140)

add_bnt = CTkButton(root, font=font1, text='Add your order', width=600, command=insert)
add_bnt.place(x=10, y=180)

root.mainloop()