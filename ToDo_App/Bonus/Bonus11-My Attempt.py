Score = 0

data = [{
    "Question": "What are dolphins?",
    "Options":["Birds","insects","cats","fish"],
    "Correct_Answer": "fish"
        },
        {
    "Question": "What are spiders?",
    "Options":["Birds","insects","cats","fish"],
    "Correct_Answer": "insects"
}]

for q in data:
    print(q["Question"])
    for o in q["Options"]:
        print(o)
    user_input = input("Enter your answer: ")
    if user_input == q["Correct_Answer"]:
        Score += 1
        print(f"Correct: Your current score is {Score}")
    else:
        print(f"Wrong: Your current score is {Score}")







