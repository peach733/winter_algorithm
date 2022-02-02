# 4. 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요. 
# 예제)
# 입력
# 4
# 출력
#    * 
#   * * 
#  *   * 
# *     *

star_count = int(input())

for i in range(star_count):
    for j in range(star_count*2):
        if(j == star_count-1-i):
            print("*", end="")
        elif(j == star_count+i-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()