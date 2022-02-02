# 2. N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하세요. 
# 예제)
# 입력
# 5 
# 5
# 2
# 1
# 6
# 4
# 출력
# 1
# 2
# 4
# 5 
# 6

count = int(input())
output_list = []

for i in range(count):
    output_list.append(int(input()))
    output_list.sort()
print()

for n in output_list:
    print(n)