# 2. 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 출력하도록 작성해주세요.
# array와 commands 변수는 아래 예시와 같이 정해진 값으로 진행합니다. 
# 예시)
# 입력
# array
# [1, 5, 2, 6, 3, 7, 4]
# command
# [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# 출력
# [5,6,3]

# 리스트 입력
list_input = list(map(int, input().split()))
print(list_input)
print()

# command 입력
command_list = []
for i in range(3):
    command_list.append(list(map(int, input().split())))
print(command_list)
print()

# 출력
answer = []
for command in command_list:
    new_array = list_input[command[0]-1:command[1]]
    new_array.sort()
    answer.append(new_array[command[2]-1])

print(answer)