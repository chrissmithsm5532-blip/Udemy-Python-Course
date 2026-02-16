import csv

with open("weather.csv","r") as file:
    data = list(csv.reader(file))


for stat,temp in data:
    if stat == "Station":
        continue
    else:
        print(f"Station:{stat}....Temperature:{temp}")

city_input = input("Enter a city:  ")

for row in data[1:]:
    if row[0] == city_input:
        print(row[1])



