def convert_metres(length_list):
    try:
        int(length_list[0])
    except ValueError:
        print("Please enter a number for feet")
    try:
        int(length_list[1])
    except ValueError:
        print("Please enter a number for inches")
    feet = int(length_list[0])
    inches =  int(length_list[1])
    total_inches = inches + (feet*12)
    print(f"{feet} and {inches} is equal to metres: {total_inches/39.3701}")


feet_inches = input("Enter Feet and inches")
divided = feet_inches.split()
convert_metres(divided)






