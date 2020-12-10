name = input("Enter your name: ")
j = len(name)
for i in range(len(name)):
    print ( ' '*(len(name)-i), name[i], ' '*(i*2)+'->'+name[i],)
