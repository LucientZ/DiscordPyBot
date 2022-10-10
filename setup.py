import datahandling as dt
from helper import *

#########################
# DATA HELPER FUNCTIONS #
#########################


def print_copypastas() -> None:
    """
    Prints each copypasta in an easily readable format
    """
    copypastas = dt.get_copypasta_list()
    print()
    i = 0
    for copies in copypastas:
        if len(copies) > 25:
            copies = copies[:24] + "..."
        print(f"{i}: {copies}")
        i += 1


###########
# WIDGETS #
###########


def copypasta_widget() -> None:
    """
    Widget used for helping the user modify files related to copypastas.
    """
    user_in = ""

    while True:
        print(f"\n{cl.GREEN}------------------------------------------------------------{cl.END}")
        print(f"Here are the available copypasta options:\n\n1: Add Copypasta to list\n2: Get list of copypastas\n3: Remove a copypasta from list\n")
        user_in = input("Please enter an option (q to quit. b to go back): ")

        if user_in == "1":
            # Asks the user to enter a copypasta. If the input is 'b', skips adding the input to the list. 'q' quits the program.
            text = input("Enter copypasta to be added (q to quit. b to go back): ")
            if text != "b" and text != "q":
                dt.add_copypasta(text)
            elif text == "q":
                print("See you later :)")
                exit()
        elif user_in == "2":
            print_copypastas()
        elif user_in == "3":
            # Since the user must know what is in each index, print the copypastas so that the user can decide which one to remove.
            print_copypastas()
            # If the user input is 'b', skips removing an item from the list. 'q' quits the program.
            index = input("Enter an index to be deleted. (q to quit. b to go back)")
            if index != "b" and index != "q":
                try:
                    dt.delete_copypasta(int(index))
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


def fumo_widget() -> None:
    """
    Widget used for helping the user modify files related to fumo images.
    """
    user_in = ""

    while True:
        print(f"\n{cl.GREEN}------------------------------------------------------------{cl.END}")
        print(f"Here are the available fumo options:\n\n1: Add Fumo Image URL to list\n2: Get list of Fumo URLS\n3: Remove a Fumo Image URL from list\n")
        user_in = input("Please enter an option (q to quit. b to go back): ")


        if user_in == "1":
            print("STUB")
        elif user_in == "2":
            print("STUB")
        elif user_in == "3":
            print("STUB")
        elif user_in == "q":
            print("See you later :)")
            exit()
        elif user_in == "b":
            break

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
        print(f"Here are the available setup options:\n\n1: Copypasta List Modification\n2: Fumo Image URL List Modification\n3: WIP\n")
        user_in = input("Please enter an option (q to quit): ")

        if user_in == "1":
            copypasta_widget()
        elif user_in == "2":
            fumo_widget()
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

