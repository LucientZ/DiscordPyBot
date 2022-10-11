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

def print_fumo_names() -> None:
    """
    Prints each fumo name in an easily readable format
    """
    fumos = dt.get_json_dict("textdata/urls.json")["fumo"]
    print()
    i = 0
    for name in fumos:
        print(f"{i}: {name}")
        i += 1


def print_fumo_urls(name: str) -> None:
    """
    Prints each fumo image URL in an easily readable format
    """
    fumos = dt.get_json_dict("textdata/urls.json")["fumo"]
    if name in fumos:
        print(f"\nSize of list: {len(fumos[name])}")
        i = 0
        for url in fumos[name]:
            if len(url) > 150:
                url = url[:149] + "..."
            print(f"{i}: {url}")
            i += 1
    else:
        print(f"\n{name} not in list of fumos")



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
        print(f"Here are the available copypasta options:\n\n1: Add Copypasta to list\n2: Remove a copypasta from list\n3: Get list of copypastas\n")
        user_in = input("Please enter an option (q to quit. b to go back): ")

        if user_in == "1":
            # Asks the user to enter a copypasta. If the input is 'b', skips adding the input to the list.
            text = input("Enter copypasta to be added (b to go back): ")
            if text != "b" and text != "q":
                try:
                    dt.add_copypasta(text)
                except Exception as e:
                    print(f"{cl.RED}ERROR: Issue adding copypasta to list: {e}{cl.END}")
        elif user_in == "2":
            # Since the user must know what is in each index, print the copypastas so that the user can decide which one to remove.
            print_copypastas()
            # If the user input is 'b', skips removing an item from the list.
            index = input("Enter an index to be deleted. (b to go back): ")
            if index != "b":
                try:
                    dt.delete_copypasta(int(index))
                except ValueError:
                    print(f"{cl.RED}{cl.BOLD}Error: Invalid value. Please enter in index number (eg: 0, 1, 2...){cl.END}\n")
                except Exception as e:
                        print(f"{cl.RED}Error: Issue removing copypasta at index [{index}]: {e}{cl.END}")
        elif user_in == "3":
            print_copypastas()
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
        print(f"Here are the available fumo options:\n\n1: Add Fumo Image URL to list\n2: Remove a Fumo Image URL from list\n3: Get a list of Fumo Names\n4: Get list of Fumo URLS\n")
        user_in = input("Please enter an option (q to quit. b to go back): ")


        if user_in == "1":
            name = input("\nPlease enter the name of the fumo (b to go back): ")
            if name != "b":
                url = input("\nPlease enter URL for fumo image (b to go back): ")
                if url != "b":
                    try:
                        dt.add_fumo_url(name, url, True)
                    except Exception as e:
                        print(f"{cl.RED}ERROR: Issue adding URL ['{url}'] to ['{name}']: {e}{cl.END}")

        elif user_in == "2":
            name = input("\nPlease enter the name of the fumo (b to go back): ")
            if name != "b":
                print_fumo_urls(name)
                index = input("\nPlease enter index to remove (b to go back): ")
                if index != "b":
                    try:
                        dt.remove_fumo_url(name, int(index))
                    except ValueError:
                        print(f"{cl.RED}{cl.BOLD}ERROR: Invalid value. Please enter in index number (eg: 0, 1, 2...){cl.END}\n")
                    except Exception as e:
                        print(f"{cl.RED}ERROR: Issue removing URL at index [{index}]: {e}{cl.END}")
        elif user_in == "3":
            print_fumo_names()
        elif user_in == "4":
            name = input("\nPlease enter the name of the fumo (b to go back): ")
            if name != "b":
                print_fumo_urls(name)
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
