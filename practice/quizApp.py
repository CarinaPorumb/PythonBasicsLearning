# Quiz App
import random

print(" >> Quiz App << ")
name = input("Please enter your name: ")
print("Welcome " + name + "!")
print("You'll have to answer with Y(Yes) or N(No) to each question.")
print("The score will be displayed at the end of the quiz.")
print()
questionList = [["Have you ever tried to lick your elbow just to see if you could?", 'Y'],
                ["Do unicorns exist in reality?", 'N'],
                ["Is the Earth flat?", 'N'],
                ["Is it possible to eat just one potato chip?", 'N'],
                ["Do socks mysteriously disappear in the washing machine?", 'Y']]
random.shuffle(questionList)
print("There are " + str(len(questionList)) + " questions.")

score = 0
for question in questionList:
    print()
    print(question[0])
    answer = input("Your answer (Y/N):  ")
    if answer.upper() == question[1]:
        score += 1
        print("Correct!")
    else:
        print("Are you sure?!")

print()
if score == 0:
    print("Your score is " + str(score) + ". Sorry, please give it another try.")
elif score <= 4:
    print("Your score is " + str(score) + ". Congratulations!")
else:
    print("Congratulations! Your score is " + str(score) + ", you've reached the maximum score!")