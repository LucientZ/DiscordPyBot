import os, json, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adds parent directory to PATH
from textfunctions import *
from test_utils import *


def test_morbius() -> None:
    """
    Tbh, this doesn't really need a test, but it's here for completion sake. Tests if morbius returns a morbius quote
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

    for i in range(40):
        assert(morbius() in texts.values())
            

def test_get_fumo_url() -> None:
    """
    Tests if fumo urls were initialized correctly. There should be one url of a funny face.
    """
    
    assert(not get_fumo_url("fake") == "")
    assert(get_fumo_url("example") == "https://cdn.discordapp.com/attachments/390692666897203211/979153065259175946/Screenshot_20220520-193448_Gallery.jpg")


def test_format_msg() -> None:
    """
    Tests if format_msg formats a message correctly. Surrounds submessage with modifier for markdown formatting.
    """
    message = "The quick brown fox jumped over the lazy dog"

    assert(format_msg(message, "The") == "**The** quick brown fox jumped over the lazy dog")
    assert(format_msg(message, "the") == "The quick brown fox jumped over **the** lazy dog")
    assert(format_msg(message, "o", "*_") == "The quick br*_o_*wn f*_o_*x jumped *_o_*ver the lazy d*_o_*g")
    assert(format_msg("okayokay", "okay", "*") == "*okayokay*")


def test_mom() -> None:
    """
    Tests if mom returns the correct string. Should be the case since the function is simple.
    """
    for i in range(20):
        message = mom()
        assert(message == "Your Mom" or message == "Your Dad :sunglasses:")
