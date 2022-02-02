# 2. 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# l X가 3으로 나누어 떨어지면, 3으로 나눈다. 
# l X가 2로 나누어 떨어지면, 2로 나눈다.
# l 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
# 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
# 둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 
# 정답이 여러 가지인 경우에는 아무거나 출력한다.
# 예제)
# 입력
# 2
# 출력
# 1
# 입력
# 10
# 출력
# 3

division_number = int(input())

d = [0] * (division_number+1)

for i in range(2, division_number+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    
print(d[division_number])