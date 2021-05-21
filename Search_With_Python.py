def mytrim(word):
    newword=''
    for i in word:
        if (i==',' or i=='.' or i=='"' or i==';' or i=='!'):
            continue
        else:
            newword=newword+i
    newword= newword.upper().strip()
    return(newword)
sword=input("Enter word to be searched: ")
sword=sword.upper().strip()
counter=0
f=open("Search_With_Python.txt","r")
for line in f:
    list=line.split()
    print(list)
    for word in list:
        if mytrim(word)==sword:
            counter=counter+1
if counter==0:
    print(f"\nThe word {sword} is not found")
else:
    print(f"\nThe word is {sword} is found {counter} times")