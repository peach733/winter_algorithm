# 1. 수가 주어지면 각 자리의 수를 내림차순으로 정렬해보자.
# 예제)
# 입력 : 1354
# 출력 : 5431

list_regul = list(map(int, input()))
list_regul.sort(reverse = True)

for i in list_regul:
    print(i, end='')