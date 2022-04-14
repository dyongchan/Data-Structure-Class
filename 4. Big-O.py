
알고리즘의 시간복잡도 (time complexity) : Big-O 표기법 # 최고차항으로 간단하게 수행시간을 표기한다.

알고리즘 예시 3가지 이용

1. Algorithm1 : T1(n) = 2n - 1 # 1차함수

2. Algorithm2 : T2(n) = 4n - 1 # 1차함수

3. Algorithm3 : T3(n) = 3/2n^2 - 3/2bn + 1 # 2차함수

- Algorithm2가 Algorithm1 보다 2배 느리다.

- Algorithm3는 n < 5/3 면 Algorithm2 보다 빠르다.
- Algorithm3는 n > 5/3 면 항상 Algorithm2 보다 느리다.
- Algorithm3는 모든 n에 대하여 Algorithm1보다 느리다.
# 그래프를 통하여 확인가능

T1(n) , T2(n) : n에 대하여 선형적으로 증가한다. (1차함수 - 직선의 특징) # 최고차항 n
T3(n) : n에 대하여 제곱으로 증가한다. # 최고차항 n^2 
= 무한대로 보낼때 T3(n)이 훨씬 빠르게 증가한다.
= 함숫값을 결정하는 중요한 것 : 증가율 - 최고차항이 중요

T1(n) = 2n - 1 / T1(n) = O(n)
T2(n) = 4n - 1 / T2(m) = O(n)
T3(n) = 3/2n^2 - 3/2bn + 1 /  T3(n) = O(n^2)\
# 증가율을 기준으로 하므로 계수는 신경쓰지 않고 차수만 적는다.
# O(n)은 O(n^2)의 집합에 포함된다.

''' 표기법
1. 최고차항만 남긴다
2. 최고차항 계수(상수)는 생략
Big-O(최고차항)
'''

예시1)
def increment_one(a): # a라는 매개변수에 값을 증가시켜주는 함수
    return a + 1 # T(n) = 1 / 최고차항 : n^0 - O(1)

예시2)
def numberof_bits(n): # n라는 값을 받아서 2진수로 몇비트가 필요한지 보는 함수
    count = 0
    while n > 0: # while 총 4번 기본연산 및 log2^n번 돈다
        n = n//2 # 정수 나눗셈 : 몫만표현
        count += 1 
    return count

n = 8 이 주어질 때,
n = 8 - 4 - 2 - 1 - 0 / count = 3 # 0이되면 빠져나오게 됨
n = n/2 - n/2^2 - ... [ n/2^count = 1 ] / n = 2^count / log2^n = count
따라서 T(n) = c*log2^n + 1 = O(log2^n)
# log2^n은 n 보다 수행시간이 빠르다 - 그래프로 확인가능