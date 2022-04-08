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
