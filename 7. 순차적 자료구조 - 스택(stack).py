
from msilib.schema import Class
from os import popen


순차적 자료구조 - 스택(stack)

삽입 : push / 삭제 : pop
# 가장 아래부터 저장이 되고 최근 자료부터 빼내어 지는 자료 구조

top : 가장 위의 값 리턴
len(lenth) : stack에 저장된 값의 개수를 리턴

Class 및 Stack
S = Stack() : 클래스 이름 # 자동으로 생성 함수가 불리워짐
S = push(10)
S.push(2)
print(S.pop()) # 2가 지워지고 리턴
print(S.top()) # 지우지 않고 가장 위의 값 리턴 : 10
print(len(S)) # 1개 저장되어 있으니 1 리턴 / S.__len__() 을 불러온 후 return


Class Stack: # Stack은 대부분 대문자로 선언
    def __init__(self): # 생성 함수 (객체 생성)
        self.items = [] # 데이터 저장을 위한 빈 리스트 준비 / push : 새로운 값 들어옴 / pop : 값 제거

    def push(self, val): # self라는 객체에서 시작해야 함
        # self : S / value : 10
        self.items.append(val)
# 가장 오른쪽에 값 추가 : O(1)
    def pop(self):
      try: # pop할 item이 없으면
          return self.items.pop()
      except IndexError: # indexError 발생
        print("Stack is empty")
# 가장 오른쪽에 값 제거 : O(1) / append, pop으로 다른 list의 값들이 움직이는 것이 아님
    def top(self):
      try:
          return self.items[-1] # -1 은 가장 오른쪽 값의 index를 가리킨다
      excpet IndexError:
          print("Stack is empty")
# 가장 오른쪽의 값 보기 : O(1)
    def __len__(self): # len()로 호출하면 stack의 item 수 반환
        return len(self.items)
# 리스트 내 저장된 값의 개수 보기 : O(1) / items 라는 list에 항상 개수를 관리하기 때문에 return만 함

예시1) 괄호 맞추기
- (2+5)*7 - ((3-1)/2+7)
- "(()())" # 쌍 3쌍
- "(()))(" # 쌍 3쌍 / 짝이 안맞음
- 문제 
입력 : 왼쪽, 오른쪽 괄호의 문자열
출력 : 괄호쌍이 맞춰져 있으면 True 아니면 False
- 관찰
....(.....).... / 왼쪽 괄호부터 쌍을 맞춰나감
# 왼쪽 괄호는 자신에 맞는 오른쪽 괄호가 나타날 때 까지 기다려야함
# 왼쪽괄호가 Stack 속에서 기다린다. 

짝이 맞는 왼쪽괄호를 Stack으로 정리 예시 # True
(1(2)2(3)3)1
- (1 (2 )2 / (2 pop을 통해서 )2와 결합
- (1 (3 )3 / (3 pop을 통해서 )3과 결합
- (1 )1 / (1 pop을 통해서 )1과 결합
- stack에는 아무것도 남지 않게 됨.

짝 맞지 않는 왼쪽괄호를 Stack으로 정리 예시1)
(1)1)2
- (1 )1 / (1 pop을 통해서 )1과 결합
- )2는 남게됨 / pop을 했지만 비어있는 Stack이 된 것

짝 맞지 않는 왼쪽괄호를 Stack으로 정리 예시2)
(1)1(2
- (1 )1 / (1 pop을 통해서 )1과 결합
- (2는 Stack에 남게됨
# 예시1), 예시2) False

code로 표기해보기

S = Stack()
for p in parseq:
    if p == '(': S.push(p)
    elif p == ')': S.pop()
    else: print("Not allowed Symbol") # 괄호 오른쪽이 더 많다
if len(S) > 0: return False # 괄호 왼쪽이 더 많다
else: return True 