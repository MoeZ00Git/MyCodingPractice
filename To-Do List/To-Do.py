with open('todo.txt', 'r',) as todolist:
    tdlist = todolist.readlines()
print(tdlist)
stdlist = open('savedtodo.txt', 'w')
print(''.join(tdlist))
userinput = input("type input here ('quit' to exit, 'save' to save and '*' to reprioritise): ")

while userinput != "quit":
    #Method 1
    if userinput == "done 1":
        del tdlist[0]
        print(''.join(tdlist))
    elif userinput == "done 2":
        del tdlist[1]
        print(''.join(tdlist))
    elif userinput == "done 3":
        del tdlist[2]
        print(''.join(tdlist))
    elif userinput == "done 4":
        del tdlist[3]
        print(''.join(tdlist))
    elif userinput == "done 5":
        del tdlist[4]
        print(''.join(tdlist))
    #Method 2
    #Alternate code for efficiency
    #if userinput[0:4] == "done":
        #del tdlist[int(userinput[5])-1]
        #print(''.join(tdlist))
    #Method 1
    if userinput == "add go out for dinner":
        tdlist.append('go out for dinner')
        print(''.join(tdlist))
    #Method 2
    #Alternate code for any addition
    #if userinput[0:3] == "add":
        #tdlist.append(userinput[4:])
        #print(''.join(tdlist))
    if userinput == "save":
        stdlist.write(''.join(tdlist))
        print(''.join(tdlist))
    if userinput == "*":
        print(''.join(tdlist))
        ask = input("Which task is prioritised? ")
        tempvar = tdlist[int(ask)-1]
        del tdlist[int(ask)-1]
        tdlist = [tempvar] + tdlist
        print(''.join(tdlist))
    userinput = input("type input here ('quit' to exit, 'save' to save and '*' to reprioritise): ")
finallist = ''.join(tdlist)
print(finallist)
todolist.close()
stdlist.close()
