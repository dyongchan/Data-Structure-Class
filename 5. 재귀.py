from tkinter import N


재귀(Recursion) : 재귀함수 = 함수 내부에서 한번 이상 자신의 함수(Algorithms)를 호출

예시1)
1 + 2 + ... + n
sum(n) = 1 + 2 + 3 ... + (n-1) /sumn(n-1)/ + n 

def sum(n):
    if n == 1: # return 1
    return sum(n-1) + N

sum(4) = sum(3) + 4 / sum(3) = sum(2) + 3 / sum(2) = sum(1) + 2 / sum(1) = 1
따라서 1부터 return후 sum(4) = sum(3) + 4 = 10 # 재귀호출

수행시간 T(n) : sum(n)의 수행시간

if n == 1 : 비교연산 1회
sum(n-1) + n : 덧셈연산 1회 / 총 2회

T(n) = T(n-1) + C(상수)
점화식 풀기 : T(n-1) + C = T(n-2 + C) + C = T(n-2) + 2C ...
= T(n - (n-1)) + (n-1) * C
= T(1) [= 1 or C] + (n-1) * C = C * n

T1(초항), T2, ... T(n)(n번째 항) = C * n

T(n) = C * n = O(n)

재귀함수의 특징
1. n==1 test # 바닥조건(base case) : T(1) = 1 or C
2. n!=1 # 재귀호출 : T(n)에 관한 점화식
1,2 를 이용하여 전개 시 T(n) = O() 로 표기 가능

예시2)
sum(a,b) = a + (a+1) + ... + b(-1) + b (a <= b)
sum(3,8) = 3 + 4 + 5 + 6 + 7 + 8 / sum(3,7) [재귀적] + 8
- sum(3,5) = sum(a,m) # 5 = (3+8)/2 =5.5 = 5(소숫점 제거)
- sum (6,8) = sum(m+1,b)

def sum(a,b):
    if a==b: # return a / 비교연산 1회
    if a>b: # return 0 / 비교연산 1회
    m = (a+b)//2 # 비교연산 1회 + 덧셈연산 1회 + 몫연산 1회
    return sum(a,m) [왼쪽 반] + sum(m+1,b) [오른 쪽 반] # 자기함수 내에서 2번 호출 (1회이상도 상관없음)
# sum 끼리 더하는 연산 1회 = 총 6회 (상수번)
T(n) = T(n/2) + T(n/2) + C, T(1) = C
T(n) = 2 * T(n/2) + C

점화식 : T(n) = 2 * T(n/2) + C (n = 2^k) # 간단한 계산을 위해서 가정
= 2(2 * 2 * T(n/2^2)) + 2*C + C ...
= 2^k * T(n/2^k) + C(1+2+2^2...+2^(k-1)) # 공비가 2인 등비수열
= C * 2^k + C * (2^K-1) / 2-1 = 2c * 2^k - C = 2C2^k - C = 2Cn - C # O(n)

예시3)
reverse 함수 : A = [1,2,3,4,5] - A = [5,4,3,2,1]

1. 
reverse(A) = reverse() + A[0]
= reverse(A[1:]) (리스트의 거꾸로 된 값이 배열) + A[:1] (맨 첫번째항의 리스트)

T(n) = T(n-1) + C(리스트끼리의 연결 기본연산) = O(n)

2.
reverse(A,start,stop) = A[start]...A[stop-1]를 A[stop-1]..[...]..A[start]
[...] = reverse(A[start+1]...A[stop-2]) # reverse(A,start+1,stop-2)

T(n) = T(n-2) [2개는 이미 자기 자리가 있음] + C(맨앞과 뒤를 바꾸는 연산)
= T(n-4) + C + C # 앞뒤 두 개씩 고정 후 바꾸는 연산
= T(1) + (n/2)C # O(n)
