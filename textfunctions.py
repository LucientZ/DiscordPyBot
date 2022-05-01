import random as rand
import helper
#Silly messages to send in channels if something funny happens. Gives a random output.

def copypasta_text():
    """
    Returns a random string from a list of copypastas

    Parameters:
    None

    Returns:
    str: random copypasta from a dictionary
    """
    texts = {
        0: "||I am currently managing 3 servers.\nI have to act cautiously in front of users..\nI didn't always enjoy the game properly\nA lot of people even bother me for no reason...\nbut i can't say a word.. This is my duty as a server administrator||\n**I tried to express that painful feeling with a picture.**",
        1: "A thermonuclear weapon, fusion weapon or hydrogen bomb (H bomb) is a second-generation nuclear weapon design. Its greater sophistication affords it vastly greater destructive power than first-generation atomic bombs, a more compact size, a lower mass or a combination of these benefits. Characteristics of nuclear fusion reactions make possible the use of non-fissile depleted uranium as the weapon's main fuel, thus allowing more efficient use of scarce fissile material such as uranium-235 or plutonium-239",
        2: "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly but gets faster each minute after you hear this signal bodeboop. A sing lap should be completed every time you hear this sound. ding Remember to run in a straight line and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark. Get ready!… Start.",
        3: "Hey, did you know that in terms of ma-",
        4: "早上好中国\n现在我有冰激淋 我很喜欢冰激淋\n但是《速度与激情9》比冰激淋……",
        5: "Connection terminated. I'm sorry to interrupt you, Elizabeth, if you still even remember that name, But I'm afraid you've been misinformed.\nYou are not here to receive a gift, nor have you been called here by the individual you assume, although, you have indeed been called.\nYou have all been called here, into a labyrinth of sounds and smells, misdirection and misfortune. A labyrinth with no exit, a maze with no prize. You don't even realize that you are trapped. Your lust for blood has driven you in ENDless circles, chasing the cries of children in some unseen chamber, always seeming so near, yet somehow out of reach, but you will never find them. None of you will. This is where your story ENDs.",
        6: "The missile knows where it is at all times. It knows this because it knows where it isn't. By subtracting where it is from where it isn't, or where it isn't from where it is, it obtains a difference, or deviation. The guidance subsystem uses deviations to generate corrective commands to drive the missile from a position where it is to a position where it isn't, and arriving at a position where it wasn't, it now is. Consequently, the position where it is is now the position that it wasn't, and it follows that the position where it was is now the position that it isn't. In the event that the position that it is in is not the position that it wasn't, the system has acquired a variation, a variation being the difference between where the missile is and where it wasn't. If variation is considered to be a significant factor, it too may be corrected by the GEA. However, the missile must also know where it was. The missile guidance computer scenario works as follows: Because a variation has modified some of the information the missile has obtained, it is not sure just where it is. However, it is sure where it isn't, within reason, and it knows where it was. It now subtracts where it should be from where it wasn't, or vice versa, and by differentiating this from the algebraic sum of where it shouldn't be and where it was, it is able to obtain the deviation and its variation, which is called error.",
        7: "Fucking dirty-ass peasants\n\nI didn't want to be a landsknecht, you know. I wanted to be a condottiere, making buttloads of money off the Italian Wars. Wars that are half-fighting, half-measuring contest, and I'm not talking about our halberds. But nooo, the fucking peasants had to rebel in Germany. Fucking forested-as-hell Germany, where the princes are poor and the guilds are stingy. And the schedule! God's wounds, the time they make us awake at! Fucking German-born officers, always with their damn discipline. I could have even gone into a Swiss mercenary company, but no. Landsknechte. Fucking hell. Maybe I'll take out my anger on the next band of fleeing peasants we come across. It's not really my fault; this peasant 's war was their fault, so really, I'm contributing to the war effort. I mean, our pay comes from their harvest anyway, so it's like giving myself an advance on my money! Well, their money. And you know, communication can be slow on a battlefield. Maybe I couldn't hear the captain yelling at me to stop, yelling that they're just innocent peasants trying to escape before they get caught up in their brothers' folley? Well, they shouldn't have crossed my path. Here they come now; maybe I'll get Gerhard to come along with me. He's always up for a good bit of murder and pillage. Wait... Those aren't peasants. They're wearing proper armor and they've got pikes. Oh shit, are those Swiss? That flag is looking awfully red from this distance. Hey guys, anyone else see those mercenaries over there? Um... Guys? Shit, they must have turned at that last crossroads. Wait, what's that noise? Eh, it was probably nothing. Just a hare. Fucking hell, I've had enough of this German weather. I'm deserting back to Italy. Hey, look at that tree. It's got a branch hanging off of another branch straight down. Hang on... That doesn't look like a branch. Shit, is that a noose?"
    }
    return texts[rand.randrange(0,7)]

def morbius():
    """
    Returns a random string from a list of copypastas that are Morbius themed
    This code is quite redundant, meaning if it is planned to make more like this, a general function should be written
    Parameters:
    None
    Returns:
    str: random copypasta from a dictionary
    """
    texts = {
        0: 'Morbius is one of the movies of all time.',
        1: 'I love Morbius so much <3',
        2: "I love your character, it's so cute!\nYour outfit is so great too. It almost looks like a Gucci outfit.",
        3: "Omg Morbius :flushed:"
    }
    return texts[rand.randrange(0,4)]


def fumo(character):
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
        2: "cirno"
    }
    texts = {
        "reimu": helper.fumo_images.reimu[rand.randrange(0,len(helper.fumo_images.reimu))],
        "flandre": helper.fumo_images.flandre[rand.randrange(0,len(helper.fumo_images.flandre))],
        "cirno": helper.fumo_images.cirno[rand.randrange(0,len(helper.fumo_images.cirno))]
    }
    try:
        return texts[character.lower()]
    except:
        return texts[characters[rand.randrange(0,3)]]


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



print(f"{helper.colors.GREEN}{helper.colors.BOLD}textfunctions.py{helper.colors.END}{helper.colors.GREEN} initialized{helper.colors.END}")
