print("Welcome to my computer quiz")

playing = input("Do you want to play?")

print(playing)

if playing != "yes":
    quit()

print("Okey! Let's Go :)")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('You are correct!')
else:
    print("Your intelligence fails!") 

answer = input("what does CPU stand for? ")
if answer == "central processing unit":
    print('You are correct!')
else:
    print("Your intelligence fails!")

answer = input("Who is the father of computer? ")
if answer == "charles babbage":
    print('You are correct!')
else:
    print("Your intelligence fails!")

answer = input("What is the full form of MICR? ")
if answer == "magnetic ink character reader":
    print('You are correct!')
else:
    print("Your intelligence fails")

answer = input("What does GUI stand for? ")
if answer == "graphical user interface":
    print('You are correct!')
else:
    print("Your intelligence fails")


