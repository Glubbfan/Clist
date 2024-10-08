'''
To Do Liste

Commands for lists:
always "#" before a command
example: #a would add something
following commands are available:
#a = add an item, #a shop groceries (add item "shop groceries")
#d = delete an item, example command: #d2 (delete second item)
#f = item finished/done, example command: #f3 (finished third item)
#c = change item, example command: #c1 buy new water (change first item to "buy new water)
#k = end the program (k because its far away from the other letters to stop accidental use)
'''

import os

#files
cwd = os.getcwd()
allLists = cwd + "listen.txt"
availableLists = None
if os.path.exists(allLists):
    availableLists = open(allLists,"r").read()
else:
    availableLists = open(allLists, "a+").close()
    availableLists = open(allLists, "r").read()

print("The following lists are available, choose one or open a new one:")
print("0: New List")

c = 1 #counter
if availableLists != "":
    for i in availableLists.split("\n"):
        if i != "":
            print(str(c) + ": " + i)
            c += 1

listChoice = input()

if not listChoice:
    pass
elif int(listChoice) > 0:
    print(availableLists.split("\n")[int(listChoice) - 1])
elif int(listChoice) == 0:
    print("Ok neue List ist noch zu erledigen")