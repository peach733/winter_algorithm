# 1. 수가 주어지면 각 자리 수를 오름차순으로 정렬하세요.
# 예제)
# 입력
# 31549
# 출력
# 13459

list_sort = list(map(int, input()))

list_sort.sort()

for i in list_sort:
    print(i, end='')