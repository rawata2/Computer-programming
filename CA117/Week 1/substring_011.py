#!/usr/bin/env/python3
list = ['Rump Rumpelstiltskin','rump Rumpelstiltskin','stilt Rumpelstiltskin','stiLT Rumpelstiltskin','pest Rumpelstiltskin','up Rumpelstiltskin']

for i in list:
  [left, right] = i.strip().lower().split()
  print(left in right)
    
# lecturer uses def, return , pass
# if _name_ == '_main_':
#   main()