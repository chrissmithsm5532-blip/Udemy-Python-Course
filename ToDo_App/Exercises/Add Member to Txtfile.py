file = open("members.txt","r")
data = file.read()
file.close()
new_member = input('Enter your new member name: ')
file = open('members.txt','w')
file.write(data + "\n" + new_member)
file.close()



