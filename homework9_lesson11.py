replacements = ['fruits','fruit','vegetables','vegetable','Fruits','Fruit','Vegetables','Vegetable']

def censor(file,replacements:list):
    with open(file, 'r') as f:
        data = f.read()
        for word in replacements:
            print(word)
            data = data.replace(word,"***")
        with open("newfile.txt", 'w') as new_file:
            new_file.write(data)
    return

censor("textfile.txt",replacements)
