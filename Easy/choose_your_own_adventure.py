name = input("Type your name: ")
print("Welcome,", name, "You have entered the Lost Temple. Your mission is to find the Golden Crown and escape alive.")

answer = input("You see three doors: 1. RED door, 2. BLUE door, 3. BLACK door. Which door do you choose(red/blue/black)? ")

if answer == "red":
    print("You enter a room with a sleeping dragon.")
    answer = input("What do you do? 1. Fight the dragon, 2. Sneak past the dragon, 3. Take the dragon's treasure(1/2/3)? ")

    if answer == "1":
        answer = input("There were three weapons. What you want to choose: 1.Sword, 2.Shield, 3.Thor's Mjolnir? ").lower()

        if answer == "sword":
            print("You kill the dragon and You found the golden crown and escape alive.")
        elif answer == "shield":
            print("You faught hard with dragon but at the end dragon will kill you and you loose.")
        else:
            print("Dragon will kill you immediatly and You Loose! Because You are not worthy to pick up the Thor's Mjolnir HaHaHa.")

    elif answer == '2':
        print("You will escape alive but without taking the golden crown so you loose.")

    elif answer == "3":
        print("You will take the golden crown but before you escape alive from temple, dragon will kill you and you loose.")

elif answer == "blue":
    print("You enter a room filled with water.")
    answer = input("The water level is rising! You see: 1. A ladder, 2. A small tunnel, 3. A floating wooden box(1/2/3)? ")

    if answer == "1":
        print("you will survive for a long time but at the end when water's level goes fully above, you will die and you loose. ")
    elif answer == "2":
        print("You will successfully escape the temple with golden crown through small tunnel and you win!")
    elif answer == "3":
        print("You will float but when water's level goes fully above, you will die and you loose.")


elif answer == "black":
    print("You enter a dark room.")
    answer = input("A mysterious old man says: [I can give you one item]. Choose: 1. Sword, 2. Torch, 3. Key? ").lower()

    if answer == "sword":
        print("You will accidently killed that mysterious man by sword because the room is dark and you can't seen it and you loose.")
    elif answer == "torch":
        print("Now you see everything in the room and you pick up golden crown and escape alive and you win!")
    elif answer == "key":
        print("You have a key of box in which golden crown is but you see nothing because of the dark room and you loose.")

else:
    print("Invalid choice. Please choose red, blue, or black.")

print("Thank You!",name,"for playing." )
