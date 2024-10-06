#To Do Liste
import os

#files
allLists = "listen.txt"
availableLists = open(allLists,"r").read() #alle verfügbaren listen hier, neue Zeile = neue Liste

print("The following lists are available, choose one or open a new one:")
print("0: New List")
print(availableLists.split("\n"))

c = 1 #counter
for i in availableLists.split("\n"):
    print(str(c) + ": " + i)
    c += 1

listChoice = input()