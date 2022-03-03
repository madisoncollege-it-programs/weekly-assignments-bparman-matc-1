#!/usr/bin/env python3

print("""You enter a dark room with two doors.
Do you go through door #1, door #2, or door 3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ============================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.\n")

    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    # == Insanity Logic ======================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    else:
        print("N) The insanity rots your eyes into a pool of muck.")
        print("N) Good job!")

#== Door Number 3 Logic =====================
elif door == "3":
    print("You stare into the icy cold blue-gray eyes of the Night King.\n")

    print("1. Run as fast as you can away from the Night King.")
    print("2. Grab the sword convently placed next to the door and do battle with the Night King.")
    print("3. Dragon Call!")
    #== Night King ==========================
    NightKing = input("-> ")

    if NightKing == "1":
        print("1) The Night King manipulates the weahter dropping the tempature well below zero, turning any puddles into ice. You slip on one of these puddles and are knocked unconscious.")
    elif NightKing == "2":
        print("2) The Night King shatters your sword with his touch")
    elif NightKing == "3":
        print("3) A Dragon appears on the horizon and melts the Night King with its dragon breath")
    else:
        print("N) You faint and roll into the fetal position")
        print("N) Great Reflexes! The Night King thinks you're dead and travels back to Westeros")
else:
    print("You did not select a door??? Good Call :)")
