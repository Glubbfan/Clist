#To Do Liste
import os

#files
allLists = "listen.txt"
availableLists = open(allLists,"r").read() #alle verfügbaren listen hier, neue Zeile = neue Liste

print("The following lists are available, choose one or open a new one:")
print("0: New List")

c = 1 #counter
for i in availableLists.split("\n"):
    print(str(c) + ": " + i)
    c += 1

listChoice = input()

if int(listChoice) > 0:
    print(availableLists.split("\n")[int(listChoice) - 1])
elif int(listChoice) == 0:
    print("Ok neue List ist noch zu erledigen")