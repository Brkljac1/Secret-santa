import os
import random
name=input("Enter name: ")
namelist=[]
secretSanta=[]
while(name != ''):
    namelist.append(name)
    name=input("Enter name(write enter to stop): ")

while(namelist):#so while it isn't empty
    os.system("cls")
    name=input("Enter your name: ")
    pair = name
    while(pair==name):
        pair = random.choice(namelist)
    #when it gets a unique element from a list
    namelist.remove(pair)
    secretSanta.append((name,pair))
    print(name + " you got a gift receiver... go to your file to see who it is... ")
    n=input()
os.system("cls")
while(secretSanta):
    temp=(secretSanta.pop())
    filename="C:\Projects\sitniprojekti\secret santa\Santa"+temp[0]+".txt"
    f=open(filename,"w")
    f.write('(giver,receiver)\n')
    f.write("("+temp[0]+","+temp[1]+")")
    f.close()
    #toSomeone.txt



#tamara
#milica
#sandra
#katarina
#anastasija
#kristina
#gordan
#vuk
#arijana
#andjela
#naum
