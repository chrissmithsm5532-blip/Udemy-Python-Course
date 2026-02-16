date = input("What is today's date: (dd-mm-yyyy): ")
mood = input("What is your mood: 1-10: ")
description = input("What is your description: of the day\n")

with open (rf"Journal\{date}.txt", "w") as file:
    file.write(mood+'\n\n')
    file.write(description)

