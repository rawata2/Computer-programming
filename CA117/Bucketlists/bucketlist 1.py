
def namo(l1):
    x = 0
    sign = "+"
    for i in range(len(l1)): # some position i in l1 ranged somewhere in 1000 
        if i == 0:
            x = l1[i] # x is the position in l1
        elif l1[i] == "-": # if the position in l1 is "-"
            sign = "-"
        elif l1[i] == "+": # if the position in l1 is "+"
            sign = "+"
        else:
            if sign == "+": # if the sign  l1 is "+"
                x = x + l1[i] # add x (0) to the position in l1
            else:
                x = x - l1[i] # take x (0) away from the position in l1
    return x

lst1 = []

dict1 = {}
dict2 = {}

for i in range(1000): # for some position ranged somewhere in 1000
    l1 = input() # take input from user

    if l1 == "clear": # if "clear" is inputted by the user
        dict1.clear() # The clear command erases all existing variable definitions in dict 1
        dict2.clear() # The clear command erases all existing variable definitions in dict 2
        break # terminate the flow of excecution at the end of the loop as a result

    if len(l1) == 0:
        break # terminate the flow of excecution at the end of the loop if length of l1 is 0

    if l1[0] == 'd': # if 1st postion is "d" (in def)
        lst2 = l1.split(" ") # split l1 as a variable of lst2
        dict1.update({lst2[1]: lst2[2]}) # update existing dict so that lst2's 2nd postion is the same as its 3rd
        dict2.update({lst2[2]: lst2[1]}) # update existing dict so that lst2's 3rd postion is the same as its 1st


    if l1[1] == 'a': # if 2nd postion is "a" (in calc)
        lst3 = l1.split(" ") # split l1 as a variable of lst3
        lst3 = lst3[1:-1] # get the charcter from 2nd position to 2nd last
        lst4 = [] # also create a new list "lst4"
        for i in lst3: 
            if i == "-":
                lst4.append("-") # append "-" to the end of list 4
            elif i == "+":
                lst4.append("+") # append "-" to the end of list 4
            else:
                if i not in dict1: # if the same character that's in list  is not in dict 1
                    lst4.append('something') # append "something" to the end of list 4
                else:
                    lst4.append(int(dict1[i])) # else append the same character that's in list 3 and dict1 as an integer

        if 'something' in lst4: # if "something" in list 4
            l3 = lst3 + ["=", "unknown"] # create l3
            lst1.append(" ".join(l3))  
        else:
            x1 = namo(lst4)
            if str(x1) in dict2:
                x2 = dict2[str(x1)]
                l4 = lst3 + ["=", x2]
                lst1.append(" ".join(l4))
            else:
                l5 = lst3 + ["=", "unknown"]
                lst1.append(" ".join(l5))

for l in lst1:
    print(l)
