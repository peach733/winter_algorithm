# 3. 예제를 보고 규칙을 유추한 후 별을 찍는 프로그램을 작성하세요 예제)
# 입력
# 출력
# 3
#   * 
#  ** 
# *** 
#  ** 
#   *

star = int(input("Enter the star count: "))

for i in range(1, star+1):
    for j in range(star-i, 0, -1):
        print(" ", end='')
    for k in range(i):
        print("*", end='')
    
    print()

for stars in range(1, star):
    for n in range(stars):
        print(" ", end='')
    for m in range(star-stars):
        print("*", end='')
    
    print()