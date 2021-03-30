def name(s1):
  list1 = []
  for i in s1:
    if i !=" " and i.isalpha()==True:
        list1.append(i.lower())
    list2 = list(set(list1))
    list2.sort()
    list3 =["abcdefghijklmnopqrstuvwxyz"]
    ans = []
    for i in list3:
       if i not in list2:
         ans.append(i) 
    if len(ans)== 0:
       return ("Pangram")
    else:
       return("missing""+",jain(ans))