# 3. We know that triangles have 3 sides. Triangles may be classified 
# according to the lengths of those sides, as shown in this table:
# l Equilateral: All three sides are of equal length.
# l Isosceles: Two sides are of equal length, the other side is different. 
# l Scalene: All three sides have different lengths.
# There is one other possibility. 
# It is possible to give three lengths of sides which would not form a valid traingle. 
# For example 6, 3, 2. If the sum of the lengths of the two shortest sides is not greater 
# than the length of the longest side, then the sides do not represent 
# a triangle – the data is invalid.
# - Input
# Input consists of a number of lines, each line containing three positive integers, 
# not more than 1,000, separated by single spaces. 
# The last line of input will be 0 0 0 – do not process this line.
# - Output
# For each line of input, produce one line of output containing a single word 
# (Equilateral, Isosceles, Scalene or Invalid) which is the classification 
# of the lengths shown in the input.
# For Example)
# Input
# 7 7 7
# 6 5 4
# 3 2 5
# 6 2 6
# 0 0 0
# Output
# Equilateral 
# Scalene 
# Invalid 
# Isosceles

from ast import In


while True:
    a, b, c = map(int, input().split())

    if a == b == c:
        if a == 0 and b == 0 and c == 0:
            print('Invalud')
            break
        print('Equilateral')
    elif a == b or a == c or b == c:
        print('Isosceles')
    elif a > b + c or b > a + c or c > a + b:
        print('Scalene')
    else:
        print('Invaild')