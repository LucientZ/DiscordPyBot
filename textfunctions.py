import random as rand


#Silly messages to send in channels if something funny happens. Gives a random output.
def morbius():
    texts = {
        0: 'Morbius is one of the movies of all time.',
        1: 'I love Morbius so much <3',
        2: "I love your character, it's so cute!\nYour outfit is so great too. It almost looks like a Gucci outfit.",
        3: "Omg Morbius :flushed:"
    }
    return texts[rand.randrange(0,4)]

def copypasta():
    texts = {
        0: "||I am currently managing 3 servers.\nI have to act cautiously in front of users..\nI didn't always enjoy the game properly\nA lot of people even bother me for no reason...\nbut i can't say a word.. This is my duty as a server administrator||\n**I tried to express that painful feeling with a picture.**",
        1: "A thermonuclear weapon, fusion weapon or hydrogen bomb (H bomb) is a second-generation nuclear weapon design. Its greater sophistication affords it vastly greater destructive power than first-generation atomic bombs, a more compact size, a lower mass or a combination of these benefits. Characteristics of nuclear fusion reactions make possible the use of non-fissile depleted uranium as the weapon's main fuel, thus allowing more efficient use of scarce fissile material such as uranium-235 or plutonium-239",
        2: "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly but gets faster each minute after you hear this signal bodeboop. A sing lap should be completed every time you hear this sound. ding Remember to run in a straight line and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark. Get ready!… Start.",
        3: "Hey, did you know that in terms of ma-",
        4: "でもそんなんじゃだめ もうそんなんじゃほら 心は進化するよ もっともっと",
        5: "Connection terminated. I'm sorry to interrupt you, Elizabeth, if you still even remember that name, But I'm afraid you've been misinformed.\nYou are not here to receive a gift, nor have you been called here by the individual you assume, although, you have indeed been called.\nYou have all been called here, into a labyrinth of sounds and smells, misdirection and misfortune. A labyrinth with no exit, a maze with no prize. You don't even realize that you are trapped. Your lust for blood has driven you in endless circles, chasing the cries of children in some unseen chamber, always seeming so near, yet somehow out of reach, but you will never find them. None of you will. This is where your story ends.\nAnd to you, my brave volunteer, who somehow found this job listing not intended for you, although there was a way out planned for you, I have a feeling that's not what you want. I have a feeling that you are right where you want to be. I am remaining as well. I am nearby. This place will not be remembered, and the memory of everything that started this can finally begin to fade away. As the agony of every tragedy should.\nAnd to you monsters trapped in the corridors, be still and give up your spirits. They don't belong to you.\nFor most of you, I believe there is peace and perhaps more waiting for you after the smoke clears. Although, for one of you, the darkest pit of Hell has opened to swallow you whole, so don't keep the devil waiting, old friend.\nMy daughter, if you can hear me, I knew you would return as well. It's in your nature to protect the innocent. I'm sorry that on that day, the day you were shut out and left to die, no one was there to lift you up into their arms the way you lifted others into yours, and then, what became of you. I should have known you wouldn't be content to disappear, not my daughter. I couldn't save you then, so let me save you now. It's time to rest - for you, and for those you have carried in your arms.\nThis ends for all of us. End communication."
    }
    return texts[rand.randrange(0,6)]

