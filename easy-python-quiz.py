print("Welcome a quiz programmed in Python!")
name = input("What's your name?: ")
print(f"Welcome {name} thanks for trying out my Python quiz!")

playing = input("Would you like to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Okay let's play!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Good try! Let's try that again.")
    answer = input("What does CPU stand for? ")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct answer!")
    score += 1
else:
    print("Good try! Let's try that again.")
    answer = input("What does RAM stand for? ")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Good try! Let's try that again.")
    answer = input("What does GPU stand for? ")

answer = input("In Cloud Computing what does a VM stand for? ")
if answer.lower() == "virtual machine":
    print("Correct answer!")
    score += 1
else:
    print("Good try! Let's try that again.")
    answer = input("In Cloud Computing what does a VM stand for? ")

answer = input("In AWS Cloud Computing what does S3 stand for? ")
if answer.lower() == "simple storage service":
    print("Correct answer!")
    score += 1
else:
    print("Good try! Let's try that again.")
    answer = input("In AWS Cloud Computing what does S3 stand for? ")

answer = input("What does an OS stand for? ")
if answer.lower() == "operating system":
    print("Correct answer!")
    score += 1
else:
    print("Good try! Let's try that again.")
    answer = input("What does an OS stand for? ")

print(f"Great work! You got {score} questions correct!")
print(f"Great work! You got {(score / 6) * 100:.1f}%!")