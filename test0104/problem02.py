starcount = input("Enter the Star Numebr: ")
starnum = int(starcount)

for i in range(starnum+1):
  print(" " * (starnum - i) + "*" * i, end='\n')