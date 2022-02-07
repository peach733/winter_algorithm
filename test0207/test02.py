# 2. 수직선 위에 N개의 좌표 x1, x2, ..., xn이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# xi를 좌표 압축한 결과 X'i의 값은 xi > xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# x1, x2, ..., xn에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
# 입력
# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 x1, x2, ..., xn이 주어진다.
# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
# 예제)
# 입력
# 5
# 2 4 –10 4 -9
# 출력
# 2 3 0 3 1
# 입력
# 6
# 1000 999 1000 999 1000 999
# 출력
# 1 0 1 0 1 0

import sys
n = int(input())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numset = set(numbers)
a = list(numset)
a.sort()

numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i

for i in numbers:
    print(numdict[i], end=' ')