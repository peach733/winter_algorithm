1. N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공 백으로 구분해서 주어진다. 
모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
예제)
입력
5
20 10 35 30 7
출력
7 35

2. "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다. OX퀴즈의 결과가 주어졌을 때, 
점수를 구하는 프로그램을 작성하시오. 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다. 
각 테스트 케이스마다 점수를 출력한다.
예제)
입력
5
OOXXOXXOOO 
OOXXOOXXOO 
OXOXOXOXOXOXOX 
OOOOOOOOOO 
OOOOXOOOOXOOOOX
출력
10
9
7
55
30

3. It is said that 90% of frosh expect to be above average in their class. 
You are to provide a reality check. The first line of standard input contains an integer C, the number of test cases. C data sets follow. 
Each data set begins with an integer, N, 
the number of people in the class (1 <= N <= 1000). 
N integers follow, separated by spaces, each giving the final grade (an integer between 0 and 100) of a student in the class.
For each case you are to output a line giving the percentage 
of students whose grade is above average, rounded to 3 decimal places.
예제)
입력
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
출력
40.000% 
57.143% 
33.333% 
66.667% 
55.556%

4. 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요. 
예제)
입력
4
출력
   * 
  * * 
 *   * 
*     *
      
5. 아래에 나와있는 출력 예제대로 표시하세요 예제)
입력
24
출력
              *
             * * 
            *****
           *     * 
          * *   * *
         ***** ***** 
        *           *
       * *         * * 
      *****       ***** 
     *     *     *     * 
    * *   * *   * *   * *
   ***** ***** ***** ***** 
  *          **           * 