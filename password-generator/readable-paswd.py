import random

wordlist=[]
spec= ['@', '$', '#', '^', '&']

with open("wikipedia.txt", 'r') as file:
    data = file.readlines()

    for line in data:
        #print(line)
        words= line.split()

        for item in words :
            if len(item)>5:
                wordlist.append(item.capitalize())

word = random.choice(wordlist)
schar= random.choice(spec)
num= str(random.randint(10, 99))

print(word+schar+num)

