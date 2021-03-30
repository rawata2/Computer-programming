def load_contacts(filename):
  d = {}
  with open(filename, 'r') as fin:
    for line in fin:
      name, number = line.strip().split()
      d[name] = number
  return d

d = load_contacts(sys.argv[1]) #d is a global variable here

for line in sys.stdin:
  name = line.strip()
  print(f'Name: {name}')
  if name in d:
    print(f'Phone: {d[name]}')
  else:
      print('No such contact')

w = 0
x = 0
for entry in freq:
    if w < len(entry):
        w = len(entry)
    if x < len(str(freq[entry])):
        x = len(str(freq[entry]))

for (k, v) in sorted(freq.items()):
    print(f'{k:>{w}} : {v:>{x}}')

# def count(elements): 
#     # check if each word has '.' at its last. If so then ignore '.' 
#     if elements[-1] == '.': 
#         elements = elements[0:len(elements) - 1] 
   
#     # if there exists a key as "elements" then simply 
#     # increase its value. 
#     if elements in dictionary: 
#         dictionary[elements] += 1
   
#     # if the dictionary does not have the key as "elements"  
#     # then create a key "elements" and assign its value to 1. 
#     else: 
#         dictionary.update({elements: 1}) 
   
   
# # driver input to check the program. 
   
# Sentence = "Apple Mango Orange Mango Guava Guava Mango"
   
# # Declare a dictionary 
# dictionary = {} 
   
# # split all the word of the string. 
# lst = Sentence.split() 
   
# # take each word from lst and pass it to the method count. 
# for elements in lst: 
#     count(elements) 
   
# # print the keys and its corresponding values. 
# for allKeys in dictionary: 
#     print ("Frequency of ", allKeys, end = " ") 
#     print (":", end = " ") 
#     print (dictionary[allKeys], end = " ") 
#     print()