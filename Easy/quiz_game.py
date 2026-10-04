print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! Let's play :)")
score = 0
question = 0

answer = input("What does CPU stand for? ")
question += 1
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
question += 1
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
question += 1
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
question += 1
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ATM stand for? ")
question += 1
if answer.lower() == "automated teller machine":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CU stand for? ")
question += 1
if answer.lower() == "control unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {str(score)} questions correct")
print(f"You got {str(round(((score/question)*100),2))}%")