import random as rand
import helper as hlp
import datahandling as dt

#Silly messages to send in channels if something funny happens. Gives a random output.
def copypasta_text() -> str: # pragma: no cover
    """
    Returns a random string from a list of copypastas

    Parameters:
    None

    Returns:
    str: random copypasta from a dictionary
    """
    texts = dt.get_copypasta_list()
    return texts[rand.randrange(0,len(texts))]


def morbius() -> str:
    """
    Returns a random string from a list of copypastas that are Morbius themed
    
    Parameters:
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


def get_fumo_url(character: str) -> str:
    """
    Returns a random fumo character unless specified

    Parameters:
    character (str): name of character to return fumo image of

    Returns:
    str: random fumo image link
    """
    character = character.lower()

    fumos = dt.get_json_dict("data/textdata/urls.json")["fumo"]

    if character in fumos:
        return fumos[character][rand.randrange(0,len(fumos[character]))]
    else:
        character = rand.choice(list(fumos))
        return fumos[character][rand.randrange(0,len(fumos[character]))]


def format_msg(msg: str, submsg: str, modifier: str = '**') -> str:
    """
    Formats a string so that a selected substring (non case-sensative) will have a markdown modifier surround it.
    eg: the chicken broke the house --> **the** chicken broke **the** house.
    eg: the chicken broke the house --> *_the_* chicken broke *_the_* house.
    Modifiers will be reversed after the submessage. Modifiers happening twice in succession will be replaced with an empty string as to keep formatting conciseness.
    
    Parameters:
    msg (str): Message to be modified
    submsg (str): Part of message to be surrounded
    modifier (str): String to surround occurences of submsg

    Returns:
    str: modified msg
    """

    msg = msg.replace(submsg, modifier + submsg + modifier[::-1])
    
    # Edgecase handling where there are one or more submessages next to each other
    if modifier + modifier in msg: 
        msg = msg.replace(modifier + modifier, "")

    return msg


def mom() -> str: # pragma: no cover
    """
    returns string "Your Mom" 95% of the time. returns string "Your Dad :sunglasses:" 5% of the time

    Parameters:
    none

    Returns:
    str: random message
    """
    num = rand.randrange(0,20)
    if num == 19:
        return "Your Dad :sunglasses:"
    else:
        return "Your Mom"
