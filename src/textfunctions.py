import random as rand
from textwrap import dedent
import datahandling as dt
import random

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

def source_identifier_detection_response() -> str:
    essay_message = dedent("""\
    Hi, it seems like your link has a source identifier in it. If you don't know what this means let me explain.
                
    A source identifier is how a company tracks what users are related to each other. Let's look at an example of a normal YouTube link:
    ```
    https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ```           
    Realize the `?si=` at the end? That contains the variables that YouTube uses to determine what video you're watching. Normally, this is used for the video ID. Now let's look at an evil version of that link:
    ```
    https://youtu.be/dQw4w9WgXcQ?si=Z45wYtKZvpZsduo2
    ```   
    `youtu.be` is YouTube's shortened domain. Realize the part that says `?si=`. That's the source identifier that tracks *who* sent the link. This appears if instead of copying from the url bar you click the "share" button. It's YouTube's way of tracking you and who you have relations with.

    To clean up the source identifier, simply remove everything after the `?si=`.
    ```
    https://youtu.be/dQw4w9WgXcQ
    ```   
    Other social media does similar things. Instagram uses `?igsh=`. Stay safe! :D
    """)

    regular_message = "Whoops, you left the source identifier in that url buddy."

    return regular_message if random.random() < 0.95 else essay_message