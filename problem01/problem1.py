'''
1. 철수는 이번 데이터베이스 과목에서 절대평가로 점수를 받았으나 학점을 알고싶습니다. 
점수를 입력하였을 때 학점으로 출력하는 프로그램을 작성하세요. (점수 기준은 아래와 같습니다.)
점수 -> 학점
96~100 -> A+
91~95 -> A
86~90 -> B+
81~85 -> B
76~80 -> C+
71~75 -> C
66~70 -> D+
61~65 -> D
0~60 -> F
100점을 초과하거나 0점 미만일 시
입력값이 잘 못 되었습니다.
예제) 입력 : 25 출력 : F
'''

gradeUser = int(input("Enter the your score: "))
if gradeUser > 100 or gradeUser < 0:
    print("It's wrong score. Please, retry.")
elif 95 < gradeUser <= 100:
    print("A+")
elif 90 < gradeUser <= 95:
    print("A")
elif 85 < gradeUser <= 90:
    print("B+")
elif 70 < gradeUser <= 85:
    print("B")
elif 65 < gradeUser <= 70:
    print("C+")
elif 60 < gradeUser <= 65:
    print("C")
elif 0 <= gradeUser <= 60:
    print("F")