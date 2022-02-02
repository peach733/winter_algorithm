'''
흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 
사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. 
"Quadrant n"은 "제n사분면"이라는 뜻이다.
예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 
점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 
단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다. (단, x좌표와 y좌표는 0이 될 수없다)
예제)
입력 : 9 -13 
출력 : 4
입력 : 1 1 
출력 : 1
'''

putNumber = input("Enter the Number(two piece): ")
sperateNum = putNumber.split(" ")

if int(sperateNum[0]) > 0 and int(sperateNum[1]) > 0:
    print("1")
elif int(sperateNum[0]) < 0 and int(sperateNum[1]) > 0:
    print("2")
elif int(sperateNum[0]) < 0 and int(sperateNum[1]) < 0:
    print("3")
elif int(sperateNum[0]) > 0 and int(sperateNum[1]) < 0:
    print("4")