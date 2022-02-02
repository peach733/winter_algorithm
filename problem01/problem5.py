'''
첫 번째 줄에는 별 N개, 두 번째 줄에는 별 N-2개, 마지막 줄에는 별 1개를 표시하는 프로그램을 작성하세요
예제)
입력
출력
5 -> ***** 
      *** 
       *
'''

starNum = int(input("Enter the number: "))

for i in range(starNum, 0, -2):
      print(" "*(int((starNum-i)/2))+"*"*(i))