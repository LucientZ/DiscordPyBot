import random as rand

print()

def morbius():
    texts = {
        0: 'Morbius is one of the movies of all time.',
        1: 'I love Morbius so much <3',
        2: "I love your character, it's so cute!\nYour outfit is so great too. It almost looks like a Gucci outfit.",
        3: "||I am currently managing 3 servers.\nI have to act cautiously in front of users..\nI didn't always enjoy the game properly\nA lot of people even bother me for no reason...\nbut i can't say a word.. This is my duty as a server administrator||\n**I tried to express that painful feeling with a picture.**"
    }
    num = rand.randrange(0,4)

    return texts[num]
