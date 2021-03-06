import random as rand
from helper import *
import datahandling as dt
#Silly messages to send in channels if something funny happens. Gives a random output.
def copypasta_text():
    """
    Returns a random string from a list of copypastas

    Parameters:
    None

    Returns:
    str: random copypasta from a dictionary
    """

    # Some of these texts contain strong language. These are all requests from other users
    texts = dt.get_copypasta_list()
    return texts[rand.randrange(0,len(texts))]

def morbius():
    """
    Returns a random string from a list of copypastas that are Morbius themed
    
    None
    Returns:
    str: random copypasta from a dictionary
    """
    texts = {
        0: 'Morbius is one of the movies of all time.',
        1: 'I love Morbius so much <3',
        2: "I love your character, it's so cute!\nYour outfit is so great too. It almost looks like a Gucci outfit.\nIs that a tail, or is it your hair?\nWow. The best of both worlds. You're really such a unique character... It's mesmerizing. Anyway, I forgot the question.",
        3: "Omg Morbius :flushed:",
        4: "It's Morbin time",
        5: "I'm literally Morbing right now this is awesome!!",
        6: "A good morb is eventually morb. A bad morb is morbed forever...",
        7: "I do not know with what weapons World War III will be fought, but what I do know is that Morbius is the top movie on Apple TV.",
        8: '*Jared Leto looks through a collection of sheets of paper*\n\nCamera person: "What are you reading?"\n\nJared: "Uh, nothing really just uh..."\n\n*Camera person pans towards Jared\'s collection of papers*\n\nJared: "no no no no no"\n\nCamera person: "What are you reading? Come on!"\n\n*Paper shows the text "MORBIUS 2: IT\'S MORBIN\' TIME written by Bartholomew Cubbins" while theme from Curb your Enthusiasm plays in the background*'
    }
    return texts[rand.randrange(0,9)]


def get_fumo_url(character):
    """
    Returns a random fumo character unless specified

    Parameters:
    character (str): name of character to return fumo image of

    Returns:
    str: random fumo image link
    """
    
    characters = {
        0: "reimu",
        1: "flandre",
        2: "cirno",
        3: "hayasaka",
        4: "aqua"
    }
    texts = {
        "reimu": fumo_images.reimu[rand.randrange(0,len(fumo_images.reimu))],
        "flandre": fumo_images.flandre[rand.randrange(0,len(fumo_images.flandre))],
        "flan": fumo_images.flandre[rand.randrange(0,len(fumo_images.flandre))],
        "cirno": fumo_images.cirno[rand.randrange(0,len(fumo_images.cirno))],
        "hayasaka": fumo_images.hayasaka[rand.randrange(0,len(fumo_images.hayasaka))],
        "aqua": fumo_images.aqua[rand.randrange(0,len(fumo_images.aqua))]
    }
    try:
        return texts[character.lower()]
    except:
        return texts[characters[rand.randrange(0,5)]]


def format_msg(msg, submsg, modifier = '**'):
    """
    Formats a string so that a selected substring (non case-sensative) will have a modifier surround it.
    eg: the chicken broke the house --> **the** chicken broke **the** house
    
    Parameters:
    msg (str): Message to be modified
    submsg (str): Part of message to be surrounded
    modifier (str): String to surround occurences of submsg

    Returns:
    str: modified msg
    """
    if not type(msg) == str:
        raise TypeError("Argument 1: msg not type string")
    elif not type(submsg) == str:
        raise TypeError("Argument 2: submsg not type string")


    submsg_length = len(submsg)
    i = len(msg) - submsg_length

    # Iterates backwards in string to make replacing easier
    # i == -1 is so it checks the first index as well
    while(not i == -1):
        temp_str = msg[i:i+submsg_length]
        if temp_str.lower() == submsg.lower():
            # Operation that wraps modifier around submsg
            msg = msg[:i] + modifier + temp_str + modifier + msg[i + submsg_length:]
        i -= 1
        
    return msg

def mom():
    num = rand.randrange(0,20)
    if num == 19:
        return "Your Dad :sunglasses:"
    else:
        return "Your Mom"



print(f"{cl.GREEN}{cl.BOLD}textfunctions.py{cl.END}{cl.GREEN} initialized{cl.END}")
