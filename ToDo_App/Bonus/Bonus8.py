

def get_average():
    file = open("files/data.txt",'r')
    local_contents = file.readlines()
    total = 0
    for item in local_contents:
        total = total + float(item)
    total = total/len(local_contents)
    return total


average = get_average()
print (average)




