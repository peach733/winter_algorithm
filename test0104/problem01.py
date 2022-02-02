yeardif = input("Enter the Year: ")
yeardiff = int(yeardif)

if yeardiff % 4 == 0 and yeardiff % 100 != 0:
  print("윤년입니다.")
else:
  print("윤년이 아닙니다.")