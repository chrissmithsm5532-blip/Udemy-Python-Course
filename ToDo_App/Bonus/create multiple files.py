contents = ['Content a2','Content b','Content c']

filenames = ["content_a.txt","content_b.txt","content_c.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"../files/{filename}",'w')
    file.write(content)
    file.close()




