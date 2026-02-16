password = input ("Enter your password")

result = {}

if len(password) >=8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
       digit= True
result["contains_number"] = digit


capital = False

for i in password:
    if i.isupper():
        capital = True

result["contains_capital"] = capital
print(result)

if all(result.values()):
    print("Strong Password")
else :
    print("Weak Password")



