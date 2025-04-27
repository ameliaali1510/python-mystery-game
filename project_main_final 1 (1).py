import time 

import sys 

global name 

def type_text(text, delay=0.05): 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

name = input("Enter your name:") 

readychoice = input("Are you ready?")   
if readychoice.lower() == "yes":
   type_text("Game loading...")
else:
    type_text("You were not brave enough!") 
    sys.exit()



type_text(f"Welcome to the haunting of Ravenswood Manor, {name}.") 
type_text("You stand at the entrance of the old mansion, its weathered facade hinting at the dark secrets within.") 
type_text("The once-grand structure is now a shadow of its former self, with crumbling stone walls and ivy snaking up its sides.") 
type_text("For centuries, Ravenswood Manor has loomed over the misty countryside.") 
type_text("Locally known by its ominous nickname, Greys Manor, for its supposed ghostly apparitions.") 
type_text("Decades ago, the entire family mysteriously vanished without a trace, leaving behind only unanswered questions and an ominous curse.") 
time.sleep(2)
type_text("As you approach the door, you read the sign attached next to it.")
type_text("Knock on the door to enter.")


type_text("Would you like to >open< or >knock<")

option1 = input(">>>").lower() 

if option1 == "knock": 
    type_text("The door swings open with a loud bang.") 
    type_text("As you step through the threshold, the door slams shut behind you.") 
    type_text("locked.")

elif option1 == "open": 
    type_text("Cold skeletal hands spring from underneath you.") 
    type_text("You are dragged into the cold, crushing ground.") 
    type_text("You have died!")
    sys.exit() 

else:
    type_text("That wasnt an option, listen next time!") 
    sys.exit()


type_text("As you step cautiously into dimly lit room the heavy wooden door creaks shut behind you, echoing through the silence.") 
type_text("The faint light from a flickering candle casts eerie shadows on the ancient wallpaper.") 
type_text("You take a few steps forward and turn to come face to face with a large and dusty mirror.") 
type_text("You see the face of an elderly woman...a friend? A relative?") 
type_text("You feel the mirror pulling you towards it.") 
time.sleep(2)
type_text("Do you: >step away< or >step towards<") 

option2 = input(">>>").lower() 


if option2 == "step away":
    type_text("You take a deep breath, and with major effort, step away from the mirror.")
    type_text("You feel a weight lift off your shoulders as you hurriedly walk away.") 
elif option2 == "step towards":
    type_text("You step towards the dusty mirror, it suddenly shatters.") 
    type_text("You feel your very soul being pulled into the shattered crystal prison.") 
    type_text("You have died.")
    sys.exit()

else:
    type_text("You were too bold. Curiosity killed the cat!") 
    sys.exit() 

type_text("Suddenly, the temperature drops, and a cold draft chills your bones.") 
type_text("In that moment, you catch a glimpse of a shadowy figure standing at the far end of the room, its eyes glowing with a sinister light.")
type_text("You feel that you only have 2 options...")
time.sleep(2)
type_text("Do you: >confront< or >retreat<")

option3 = input(">>>").lower()

if option3 == "confront":
    type_text("The figure vanishes leaving behind an ornate key on the ground.") 
    type_text("You quickly pick up the key, thinking it might be useful later.") 

elif option3 == "retreat":
    type_text("You turn back, but suddenly icy hands grab you from behind.") 
    type_text("You try to scream, but the shadows creep in and the darkness consumes you.") 
    type_text("You have died.")
    sys.exit() 

else:
    type_text("You thought you might have escaped, but the house had other plans!") 
    sys.exit() 

type_text("You reach the door and insert the mysterious key into the lock.") 
type_text("It fits perfectly.") 
type_text("The door swings open, revealing an old library draped in shadows. Ancient books and tomes line the walls.") 
type_text("You notice a single book glowing faintly on a wooden table.") 
type_text("Do you >read< or >ignore<") 

option4 = input(">>>").lower() 
if option4 == "read": 
    type_text("As you open the book and begin to read, the book starts to violently shake.") 
    type_text("Ghostly figures emerge from the pages of the book, pulling you into the void.")
    type_text("The last thing you hear is a faint whisper - another soul for the manor.") 
    type_text("You have died.")
    sys.exit() 

elif option4 == "ignore": 
    type_text("You decide to ignore the cursed book and step away.") 

else:
    type_text("Only the Gamemaster decides your fate.") 
    sys.exit() 

type_text("As you step away from the book, you see another large tome sticking out from a library shelf.") 
type_text("Something tells you this could be your escape.") 
time.sleep(2)
type_text("Now you must choose - would you like to >pull< or >ignore<")

finaloption = input(">>>").lower()

if finaloption == "pull":
    type_text("You pull on the book and hear a grinding sound. A passageway has opened through a shelf!") 
    type_text("You begin to feel the shadows around you press in.") 
    type_text("You quickly rush through and find yourself outside in an ancient graveyard.") 
    type_text("Congratulations, you have escaped the haunting of Ravenwood Manor.") 
    sys.exit()

elif finaloption == "ignore":
    type_text("You begin to feel the shadows around you press in.") 
    type_text("You frantically look around the room, but there is no escape!")
    type_text("Like countless others before, you have fallen to the horrors of Ravenswood Manor. Your fate is now sealed within its cursed walls.")
    type_text("Better luck next time.")

else:
    type_text("You have sealed your own fate. Take heed and next time, follow the instructions.") 

type_text(f"Thank you for playing, {name}")
sys.exit()