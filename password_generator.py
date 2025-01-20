import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols= ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
pswd=[]
for i in range(1,5):
    l = random.choice(letters)
    pswd.append(l)
for i in range(1,3):
    n = random.choice(numbers)
    pswd.append(n)
for i in range(1,4):
    s = random.choice(symbols)
    pswd.append(s)

print("The password is: "+''.join(pswd))

random.shuffle(pswd)

print("The password is: "+''.join(pswd))
