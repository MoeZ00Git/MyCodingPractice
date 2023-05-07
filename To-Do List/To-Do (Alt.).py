with open('todo.txt', 'r',) as todolist:
    tdlist = todolist.readlines()
print(tdlist)
stdlist = open('savedtodo.txt', 'w')
print(tdlist)
print(''.join(tdlist))
userinput = input("type input here, in form done nth ('quit' to exit, 'save' to save and '*' to reprioritise): ")

def ListReOrder(Input, List, Number):
    if Number >= 1:
        TempVar = List[0:Number]
        del List[0:Number]
        print("The temp var is", TempVar)
        List = [Input[4:] + '\n'] + List
        List = TempVar + List
        return List
    else:
        List = [Input[4:] + '\n'] + List
        return List

while userinput != "quit":
    if userinput[0:4] == "done":
        del tdlist[int(userinput[5])-1]
        print(''.join(tdlist))
    if userinput[0:3] == "add":
        print(''.join(tdlist))
        inputpriority = input("at what priority (use numbers to indicate priority)? ")
        number = int(inputpriority) - 1
        tdlist = ListReOrder(userinput, tdlist, number)
        print(''.join(tdlist))
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
    userinput = input("type input here in form done nth ('quit' to exit, 'save' to save and '*' to reprioritise): ")

i = 1
LoopList = []
for item in tdlist:
    TempString = item
    del item
    item = str(i) + " : " + TempString
    i += 1
    LoopList += [item]
    tdlist = LoopList
finallist = ''.join(tdlist)
print(finallist)


Save = input("Save? ")
if Save.lower() == "y" or Save.lower() == "yes":
    stdlist.write(finallist)
    print(finallist)
else:
    print("Ok")
    

todolist.close()
stdlist.close()
