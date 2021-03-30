def load_contacts(filename):
  d = {}
  with open(filename, 'r') as fin:
    for line in fin:
      name, number, email = line.strip().split()
      d[name] = (number, email)
  return d

d = load_contacts(sys.argv[1]) #d is a global variable here

for line in sys.stdin:
  name = line.strip()
  print(f'Name: {name}')
  if name in d:
    number, email = d[name]
    print(f'Phone: {number}')
    print(f'Phone: {email}')
  else:
      print('No such contact')