print("Welcome to my computer quiz!")

playing = input("Do you want to play (yes/no)? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play !!")
score = 0

answer = input("What does the acronym URL stand for? ")
if answer.lower() == "uniform resource locator":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct Answer:","uniform resource locator")

answer = input("What is the binary representation of the decimal number 25? ")
if answer.lower() == "11001":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct Answer:","11001")

answer = input("Which data structure follows the LIFO (Last-In, First-Out) principle? ")
if answer.lower() == "stack":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct Answer:","stack")

answer = input("Which sorting algorithm has the best average-case time complexity? ")
if answer.lower() == "merge sort":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct Answer:","merge sort")

answer = input("What does the acronym HTML stand for? ")
if answer.lower() == "hyper text markup language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct Answer:","hyper text markup language")

answer = input("Which type of network topology connects all devices in a circular chain? ")
if answer.lower() == "ring topology":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct Answer:","ring topology")

answer = input("Which data structure is suitable for implementing a FIFO (First-In, First-Out) queue? ")
if answer.lower() == "linked list":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("Correct Answer:","linked list")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")