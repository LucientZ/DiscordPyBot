
def get_token() -> str:
    # Opens token.dat and obtains


    TOKEN = ""
    choice = ""

    #At the moment, this code assumes the only error is token.dat not existing
    try:
        # opens up token.dat which should only contain the bot token
        with open('token.dat') as tokenfile:
            print("Logging in with TOKEN from token.dat")
            TOKEN = tokenfile.read()

            if(TOKEN == " "):
                # If TOKEN == " ", this means that token.dat is empty
                
                while(choice != "Y" and choice != "n"):
                    choice = input("\nIt looks like there isn't anything in token.dat.\nWould you like to add a token to this file? (It is recommended that this is done manually) [Y/n] ")
                
                if(choice == 'Y'):
                    TOKEN = input('\nPlease enter the bot token: ')
                    write_token(TOKEN)
                else:
                    print("\nNo token will be added to token.dat")
                    TOKEN = input('Please enter the bot token: ')

    except:
        while(choice != "Y" and choice != "n"):
            choice = input("\nIt looks like there isn't a file named 'token.dat' in this directory.\nWould you like to create this file? [Y/n] ")
            print(choice)

        if(choice == 'Y'):
            TOKEN = input('\nPlease enter the bot token: ')
            write_token(TOKEN)
        else:
            print("\ntoken.dat will not be created")
            TOKEN = input('Please enter the bot token: ')

        
    return TOKEN

def write_token(TOKEN) -> None:
    tokenfile = open("token.dat", "w")
    tokenfile.write(TOKEN)
    tokenfile.close()

