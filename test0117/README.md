1. N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
- 입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
- 출력
입력으로 주어진 숫자 N개의 합을 출력한다.
예제)
입력
5 54321
출력
15

2. 동혁이는 졸업을 하기 위해 일반 화학 실험을 들어야 한다.
마지막 실험은 어떤 혼합물을 만든 뒤 온도를 1분에 한 번씩 잰 후, 1분동안 변화한 온도를 표로 만들어야 한다.
뛰어난 프로그래머인 동혁이는 혼합물의 온도를 자동으로 측정해주는 프로그램을 만들었다. 
하지만, 깜빡하고 변화한 온도를 자동으로 계산해주는 프로그램을 만들지 않았다.
동혁이가 측정한 온도가 주어졌을 때, 변화한 온도를 구하는 프로그램을 작성하시오.
- 입력
동혁이가 측정한 혼합물의 온도가 순서대로 주어진다. 온도는 -10도와 200도 사이이고, 소수 점 둘째자리까지 적혀져 있을 수도 있다. 마지막 측정 후에는 999가 주어진다. 동혁이는 온도 를 적어도 2번 측정했다.
- 출력
주어진 각 온도와 이전 온도와의 차이를 출력한다. 첫 번째 측정할 온도는 이전 온도가 없으니 출력할 필요가 없다. 차이는 항상 소수점 둘째자리까지 출력한다.
예제)
입력
10.0
12.05
30.25
20
999
출력
2.05 
18.20
-10.25
        
3. We know that triangles have 3 sides. Triangles may be classified according to the lengths of those sides, as shown in this table:
l Equilateral: All three sides are of equal length.
l Isosceles: Two sides are of equal length, the other side is different. 
l Scalene: All three sides have different lengths.
There is one other possibility. It is possible to give three lengths of sides which would not form a valid traingle. For example 6, 3, 2. If the sum of the lengths of the two shortest sides is not greater than the length of the longest side, then the sides do not represent a triangle – the data is invalid.
- Input
Input consists of a number of lines, each line containing three positive integers, not more than 1,000, separated by single spaces. The last line of input will be 0 0 0 – do not process this line.
- Output
For each line of input, produce one line of output containing a single word (Equilateral, Isosceles, Scalene or Invalid) which is the classification of the lengths shown in the input.
For Example)
Input
7 7 7
6 5 4
3 2 5
6 2 6
0 0 0
Output
Equilateral
Scalene
Invalid
Isosceles