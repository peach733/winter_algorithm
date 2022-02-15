# 1. 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 다섯 가지이다.
# l push X: 정수 X를 스택에 넣는 연산이다.
# l pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# l size: 스택에 들어있는 정수의 개수를 출력한다.
# l empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# l top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다. 
# 예제)
# 입력
# 14 
# push 1 
# push 2 
# top 
# size 
# empty 
# pop 
# pop 
# pop 
# size 
# empty 
# pop 
# push 3 
# empty 
# top
# 출력
# 2
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3

def push(n):
    stack_size.append(n)

def pop():
    try:
        print(stack_size.pop())
    except:
        print(-1)

def size():
    return len(stack_size)

def empty():
    a = 1 if size() == 0 else 0
    print(a)

def top():
    try:
        print(stack_size[-1])
    except:
        print(-1)
    
stack_input = int(input())
stack_size = []

for _ in range(stack_input):
    stack_cmd = input().split()
    if stack_cmd[0] == 'push':
        push(stack_cmd[1])
    elif stack_cmd[0] == 'pop':
        pop()
    elif stack_cmd[0] == 'size':
        print(size())
    elif stack_cmd[0] == 'empty':
        empty()
    elif stack_cmd[0] == 'top':
        top()