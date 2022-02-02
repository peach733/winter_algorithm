'''
2. 영희는 스탑워치로 등산한 시간을 측정하였습니다. 
그러나 스탑워치의 숫자가 초로 기재가 되어있어서 얼마나 운동했는지 알 수가 없어서 변환이 필요합니다. 
알아보기 쉽도록 시, 분, 초로 변환하세요.
예제)
입력 : 3600
출력 : 1시간 0분 0초
입력 : 7273
출력 : 2시간 1분 13초
'''

putTime = int(input("Enter the Time: "))

hours = putTime // 3600
minute = putTime % 3600
minutes = minute // 60
second = minute % 60
print(hours, "시간", minutes, "분", second, "초")