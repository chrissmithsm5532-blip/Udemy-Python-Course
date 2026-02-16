filelist = ['a.txt','b.txt','c.txt']

for filename in filelist:
    file = open(f'../files/{filename}','r')
    content = file.read()
    print(content)
    file.close()

