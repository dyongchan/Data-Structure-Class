
순차적 자료구조 - 큐(queue) # First In First Out 규칙의 순차적 자료구조

insert : enqueue / Stack의 push

delete : dequeue / Stack의 pop

enqueue(5)
enqueue(-2)
dequeue() # 5 리턴
enqueue(10)
dequeue() # -2 리턴

front 와 rear로 구분하여 queue 만듬

예시1)
items 라는 list 선언
front-index 를 가리키는 변수를 가리키는 class 선언
# front-index : queue 속 가장 처음의 index

class Queue:
  def __init__(self):
    self.items = [] # 빈리스트로 초기화
    self.front-index = 0
  def enqueue(self,val):
    self.items.append(val)
  def dequeue(self):
    if self.front-index == len(self.items):
        print("Q is empty") # 초리 front-index = 0
    else:
      X = self.items[front-index]
      self.front-index += 1 # front-index의 값 추출 후 + 1
    return X