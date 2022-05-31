import datahandling as dt
import os
from helper import *

# TODO add GUI with tkinter to streamline
# Most of this code is temporary and should not exist on release

user_in = ""
dt.init_file("textdata/copypasta.dat")
option_text = "1: Add Copypasta to s-copypasta list\n2: Get list of copypasta\n3: Remove a copypasta"

print("\nWelcome to this bot's setup application. Here are the available options:\n")
print(option_text, "\n")

def add_copypasta():
    text = input("Enter copypasta to be added: ")
    with open("textdata/copypasta.dat", "a") as f:
        f.write(text + "\n\n")
        print(text, "added to textdata/copypasta.dat")
    print("\nHere are the available options for commands:\n\n" + option_text + '\n')


def get_copypastas():
    copypastas = dt.get_copypasta_list()
    print()
    i = 0
    for copies in copypastas:
        print(i, ":",copies)
        i += 1
    print("\nHere are the available options for commands:\n\n" + option_text + '\n')


def delete_copypasta():
    copypastas = dt.get_copypasta_list()
    i = 0
    for copies in copypastas:
        print(i, ":",copies)
        i += 1
    index = input("Enter an index to remove: ")

    try:
        copy = copypastas.pop(int(index))
        with open("textdata/copypasta.dat", "w") as f:
            for copies in copypastas:
                f.write(copies + "\n\n")
            print(copy, "removed from textdata/copypasta.dat")
    except IndexError:
        print(index,"not in range")
    except TypeError as e:
        print(e)

    print("\nHere are the available options for commands:\n\n" + option_text + '\n')

while True:
    options = {
        "1": add_copypasta,
        "2": get_copypastas,
        "3": delete_copypasta
    }
    user_in = input("Please enter an option (q to quit): ")
    try:
        options[user_in]()
    except KeyError:
        if user_in == "q":
            break
        print("Unknown option. Please enter a number or 'q'")
    
