from pydoc import doc


알고리즘의 시간복잡도 (time complexity)
# 알고리즘 수행시간의 정의

기본연산을 얼마나 수행하는가
A = [, , , , , ,] / n : input size
1. 모든 입력에 대하여 기본연산 횟수를 더한 후 평균 # 무한한 입력일 시 현실적으로 불가능
2. 가장 안좋은 입력(worst case input)에 대한 기본연산 횟수를 측정 : worstcase time complexity
# 어떤 입력에 대해서도 worstcase time complexity 보다 수행시간이 크지 않다.

알고리즘 수행시간 = 최악의 입력에 대한 기본연산 횟수로 정의

'''
예시1) 
algorithm arrayMax(A,n):
    currentMax = A[0] # 대입의 기본연산 1회
    for i = 1 to n-1 do
        if currentMax < A[i]: # 비교의 기본연산 1회
            current = A[i] # 비교문장이 참 일때만 수행
    return currentMax
비교문장이 계속 참이되어 기본수행을 계속 수행 하는 것이 최악의 경우
# A가 오름차순의 array 구조 일 때 가장 최악의 수행시간이 됨.

A[0]의 선언 : 기본연산 1회
for 문 : 1 부터 n-1번까지 수행
if 문 : 비교문의 항상 참으로 기본연산 계속 시행 
for 문 * if 문의 기본연산 : 2n-2 / + 1 (A[0])의 명시 = 2n-1
T(n) : 2n-1 # n = 6 / T(6) = 12-1 = 11
'''
'''
예시2)
algorithm sum1(A,n): # n에 비례하여 수행시간 상승 (1차식)
    sum = 0 # 대입 : 기본연산 1회
    for i = 0 to n-1 doc # n번 돈다
        if A[i]%2 == 0: # 나머지, 비교 2회 기본연산 / 짝수이면
            sum += A[i] # sum = sum + A{i}
    return sum

A : 모든값이 짝수 : worstcase 입력
T(n) = 4n + 1
# n에 비례하여 수행시간 상승 (1차식)
'''
'''
예시3)
algorithm sum2(A,n):
    sum = 0 # 기본연산 1회
    for i = 0 to n-1 do # n번 반복
        for j = i to n-1 do # i = 0,1,2...n-1 / j = 1+2+3+...+n = n(n+1)/2 
            sum +=A[i] * A[j] # 기본연산 3회 [n(n+1)/2 만큼 반복]
    return sum

T(n) = n(n+1)/2 * 3 + 1 = 3/2 n^2 + 3/2 n + 1
# n의 제곱에 비례하여 수행시간 상승 (2차식)
'''
