#print("my first code")
#print("this is an example", 2 + 3, "of something you can do")
#
print("hello", end=" ")
print("world")

name = "tom" 
age = 18
print(f"{name} is {age} years old")

print(342 + 699)
print(34 * 12)
print(78 / 6)
print(839 - 432)
print(10 % 7)
print(5 ** 2)
print(2 ** 100)

a = 265 
b = 5924 
result = a +b 
print(result)

a = 6 * 4 
b = 5 ** 2 
c = 4 % 3 
result = a + b - c
print("result is:", result)

import random
 
# List of random responses to be given after each answer
responses = [
    "Cool!",
    "Nice!",
    "Wow, great!"
]
 
# Function to ask a question and provide a random response
def ask_question(question):
    answer = input(question + " ")
    print(random.choice(responses))
    print()# For spacing between questions
 
# List of questions to be filled in by students
questions = [
    "What's your name?",
    "What's your favorite hobby?",    # Example question
    "What's your favorite movie?", 
    "Where have you come to Uni from?",
    "How has Uni been for you so far?",
]
 
# Function to randomly select and ask two questions
def icebreaker():
    print("Let's break the ice! I'll ask you five random questions:")
    selected_questions = random.sample(questions, 5)  # Randomly select 2 questions
    for question in selected_questions:
        ask_question(question)
 
# Call the icebreaker function to start the program
icebreaker()




print("testing")