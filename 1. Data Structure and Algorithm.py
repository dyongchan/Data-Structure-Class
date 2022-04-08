from ast import Not
from pydoc import doc


Data Structure (자료구조), Algorithm(알고리즘)

자료(data) - 저장공간(memory) + 읽기,쓰기,삽입,삭제,탐색과 같은 연산 = 구조

알고리즘 : 자료에 유한한 횟수의 연산을 통해 값을 입력하여 정답을 출력하는 것

Data Structure의 예시

1. 변수(variable) 
a = 5 # 쓰기연산 (5가있는 객체의 주소가 a에 저장된다.)
print(a) # 읽기연산

2. 배열(array), 리스트(List)
A = [3,-1,5,7] # A[0] = 3, A[1] = -1, A[2] = 5, A[3] = 7 / 각 원소으 Index
읽기,쓰기 : A[3]
삽입 : A.append() : 마지막의 값 추가 / A.Insert() : 특정위치에 삽입
삭제 : A.pop() : 마지막 값 삭제 후 리턴 / A.pop(2) : 2번째 index의 값 삭제 후 리턴

3. 자료구조와 알고리즘의 성능 
가상컴퓨터(Virtual Machine)
가상언어 (Pseudo Language)
가상코드 (Pseudo Code)

Virtual Machine (가상컴퓨터) # 초기 - Turing Machine - RAM(Random Access Machine)
RAM = CPU + Memory + 기본연산 # 단위시간에 수행되는 연산

기본연산 : 1의 단위시간
- 배정, 대입, 복사 : A = B : 1(일) 시간 # A = 쓰기 / B = 읽기
- 산술연산 : +. -, *, / : 1(일) 시간
# %, 버림, 올림, 반올림 : RAM model 에서 기본연산으로 정의되지 않는다
- 비교연산 : >, >=, <, <=, ==, != # A < B | = | A - B < 0
- 논리연산 : AND, OR, Not
- 비트연산 : bit-AND, OR, NOR

Pseudo/Virtual Language (가상언어) # RAM 에서 제공하는 기본연산이 표현가능 / 제어 기능 제공
- 배정, 산술, 비교, 논리, bit-논리 : 기본연산 표현
- 비교 : if, if else, if elseif(elif)...else
- 반복 : for, while
- 함수 : 정의, 호출, return

Pseudo Code (가상코드) 
예시) algorithm ArrayMax(A,n) # algorithm ArrayMax 라는 이름의 가상코드를 기술 / (A,n) : 입력
input : n개의 정수를 갖는 배열 A / output : A의 수중에서 최대값 리턴
currentMax = A[0] # 기본연산 1회
for i = 1 to n - 1 doc # ㅕ를 증가시키며 대입연산 수행 
# c : for(i=1; i<n,; i++) / python : for i in range(1,n)
    if currentMax < A[i]
        currentMax = A[i]
return currentMax
A = [3, -1, 9, 2, 12] # 대입연산 수행해보기 / n(기본연산) = 7회
A = 무한히 많은 입력 및 n이 존재할 경우 # n = 입력의 크기