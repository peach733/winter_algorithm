# 5. 아래에 나와있는 출력 예제대로 표시하세요.
# 예제)
# 입력
# 24
# 출력
#               *
#              * * 
#             *****
#            *     * 
#           * *   * *
#          ***** ***** 
#         *           *
#        * *         * * 
#       *****       ***** 
#      *     *     *     * 
#     * *   * *   * *   * *
#    ***** ***** ***** ***** 
#   *          **           * 

star_count = int(input())

star = [[' ']*2*star_count for _ in range(star_count)]

def Solution(h, y, x):
    if h == 3:
        star[y][x] = '*'
        star[y+1][x-1] = '*'
        star[y+1][x+1] = '*'
        for i in range(x-2, x+3):
            star[y+2][i] = '*'
    else:
        nh = h//2
        Solution(nh, y, x)
        Solution(nh, y+nh, x-nh)
        Solution(nh, y+nh, x+nh)

Solution(star_count, 0, star_count-1)

for r in star:
    print("".join(r))