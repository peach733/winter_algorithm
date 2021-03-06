# 3. 수 많은 회원들의 정보가 현재 가입 순으로 되어있어 이를 정렬하고자 합니다. 
# 나이 순으 로 정렬한 후 나이가 같다면 먼저 가입한 회원이 앞으로 오는 순서로 정렬하는 프로그램을 작성하세요.
# - 입력
# 첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1 보다 크거나 같으며, 
# 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 
# 입력은 가입한 순서로 주어진다.
# - 출력
# 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 
# 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
# 예제)
# 입력
# 3
# 21 Junkyu
# 21 Dohyun 
# 20 Sunyoung
# 출력
# 20 Sunyoung 
# 21 Junkyu
# 21 Dohyun

N = int(input())

data = []

for i in range(N):
    data.append(list(input().split()))

data.sort(key= lambda x : int(x[0]))
print()

for i,j in data:
    print(i,j)