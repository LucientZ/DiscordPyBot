import datahandling as dt
from helper import *

###########################
# DATA HANDLING FUNCTIONS #
###########################







def print_copypastas() -> None:
    copypastas = dt.get_copypasta_list()
    print()
    i = 0
    for copies in copypastas:
        if len(copies) > 25:
            copies = copies[:24] + "..."
        print(f"{i}: {copies}")
        i += 1

def delete_copypasta(index: int) -> None:
    try:
        copypastas = dt.get_copypasta_list()
        copy = copypastas.pop(index)
        with open("textdata/copypasta.dat", "w") as f:
            for copies in copypastas:
                f.write(copies + "\n\n")
            print(f"'{copy}'removed from textdata/copypasta.dat")
    except IndexError:
        print(f"{cl.YELLOW}Index number [{index}] not in range{cl.END}")

###########
# WIDGETS #
###########


def copypasta_widget() -> None:

    user_in = ""

    while True:
        print(f"\n{cl.GREEN}------------------------------------------------------------{cl.END}")
        print(f"Here are the available copypasta options:\n\n1: Add Copypasta to list\n2: Get list of copypastas\n3: Remove a copypasta from list\n")
        user_in = input("Please enter an option (q to quit. b to go back): ")

        if user_in == "1":
            text = input("Enter copypasta to be added (q to quit. b to go back): ")
            if text != "b" and text != "q":
                dt.add_copypasta(text)
            elif text == "q":
                print("See you later :)")
                exit()

        elif user_in == "2":
            print_copypastas()

        elif user_in == "3":
            print_copypastas()
            index = input("Enter an index to be deleted. (q to quit. b to go back)")
            if index != "b" and index != "q":
                try:
                    delete_copypasta(int(index))
                except ValueError:
                    print(f"{cl.YELLOW}{cl.BOLD}Invalid value. Please enter in index number (eg: 1, 2, 3...){cl.END}\n")
            elif index == "q":
                exit()

        elif user_in == "q":
            print("See you later :)")
            exit()
        
        elif user_in == "b":
            break

        else:
            print("Unknown option. Please enter a number, 'q', or 'b'")

        input("\nPress Enter to continue...")


def main():
    # Initializes all files that are to be worked with
    dt.init_guild_config()
    dt.init_file("textdata/copypasta.dat")
    dt.init_json("textdata/urls.json")
    dt.add_json_dict_keys("textdata/urls.json", "fumo", "misc")


    print(f"\n{cl.BLUE}Welcome to this bot's setup application.{cl.END}")

    while True:
        print(f"\n{cl.BLUE}------------------------------------------------------------{cl.END}")
        print(f"Here are the available setup options:\n\n1: Modify copypasta list\n2: Modify fumo image urls\n3: WIP\n")
        user_in = input("Please enter an option (q to quit): ")

        if user_in == "1":
            copypasta_widget()
        elif user_in == "2":
            print("stub")
        elif user_in == "3":
            print("stub")
        elif user_in == "q":
            print("See you later :)")
            exit()
        else:
            print(f"{cl.BOLD}{cl.YELLOW}Unknown option. Please enter a number, 'q', or 'b'{cl.END}")
            input("\nPress Enter to continue...")
        


if __name__ == "__main__":
    main()

