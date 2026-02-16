filenames = ['1.doc','1.report','1.presentation']

filenames = [file.replace('.','-') + '.txt' for file in filenames]

print (filenames)