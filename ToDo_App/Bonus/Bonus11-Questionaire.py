import json
with open("questions.json","r") as file:
    content = file.read()

data = json.loads(content)
score =0

for question in data:
    print (question["question"])
    for index,alternative in enumerate(question["alternatives"]):
        print(index+1,alternative)
    user_input = int(input("Enter your choice: "))
    question["User_Choice"] = user_input

for question in data:
    if question["User_Choice"] == int(question["CorrectAnswer"]):
        score += 1

print (f"You Scored: {score}")

