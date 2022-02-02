# 3. It is said that 90% of frosh expect to be above average in their class. 
# You are to provide a reality check. The first line of standard input contains an integer C, 
# the number of test cases. C data sets follow. 
# Each data set begins with an integer, N, 
# the number of people in the class (1 <= N <= 1000). 
# N integers follow, separated by spaces, each giving the final grade (an integer between 0 and 100) of a student in the class.
# For each case you are to output a line giving the percentage 
# of students whose grade is above average, rounded to 3 decimal places.
# 예제)
# 입력
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91
# 출력
# 40.000% 
# 57.143% 
# 33.333% 
# 66.667% 
# 55.556%

all_scores = int(input())

for i in range(all_scores):
    score_class = list(map(int, input().split()))
    avg = 0
    sum = 0
    score = 0
    for j in score_class:
        sum += j
    sum = sum - int(score_class[0])
    avg = sum/int(score_class[0])
    
    for k in score_class:
        if k > avg:
            score += 1
        else:
            score += 0
    
    all_avg = float(score / int(score_class[0])*100)
    print(format(all_avg, ".3f")+'%')