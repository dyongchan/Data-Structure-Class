
순차적 자료구조 - 스택(stack) : 계산기 코드
- "2+3*5" 와 같은 수식(입력)을 연산자 계산 순위에 따라 계산 후 출력
"2+3*5" 를 '2'+'3'*'5' # '2' : 피연산자(operand) / +,* : 연산자(operator)
# 피연산자, 연산자 : 토큰(token) - 의미가 있는 단위

이항연산자(binary operator) : 항이 두 개가 필요한 연산
2+3 / 3*5

단항연산자(unary operator) : 항이 한 개만 있는 연산
+(단항)3-(이항)6

infix 수식 : 연산자가 두 피연산자 사이에 있는 형식의 수식  # postfix로 바꾸면 결과값 계산이 쉬워짐
2 + 3 * 5 
postfix 수식 :
2 3 5 * +

infix를 postfix로 바꾸기
입력 : +,-,*,(,), 숫자(영문자)로 구성된 infix 수식
출력 : postfix 수식

1. 피연산자의 순서는 그대로
2. 연산자의 우선순위에 따라 Stack내 pop을 통해 순서 변경

예시1)
1. 괄호치기 (2+3(3*5))
2. 연산자의 오른쪽 괄호 다음으로 연산자 이동 # 안쪽 괄호부터 시행하되 자신이 속한 괄호 오른쪽으로 이동
3. 괄호 제거
= 2 3 5 * +

예시2)
3*(2+5)*4
1. 괄호치기 # 같은 연산자의 결합법칙은 왼쪽부터
((3*(2+5))*4)
2. 연산자의 오른쪽 괄호 다음으로 연산자 이동
3. 괄호 지우기
3 2 5 + * 4 *

'''
- A + B * C = A B C * + # 각각의 항이 token으로 총 5개의 token 존재
# 연산자의 우선순위가 높은 것이 오른쪽으로 위치함
# Stack 내에서 + 가 * 보다 우선순위가 낮으므로 차례로 push 후 pop됨 
- A * B + C = A B * C + 
# +가 Stack 내에있는 우선순위가 높은 연산자들을 pop 시켜서 뽑아낸다.
- ( A + B ) * C = A B + C *  # 각각 7개의 token 존재
# ( : 우선순위가 제일 낮음 / ) : 우선순위 제일 높음
# ) 만나기 전까지는 괄호 속 연산자는 Stack에 쌓임
# ) 나타날 시 ( 가 나타날 때 까지 모두 pop해야함 / 괄호로 둘러싸인 연산자를 가장 먼저 계산하겠다.
'''

code 작성
리스트 : outstack - posfix의 수식으로 표현
스택 : opstack - 연산자를 담는 stack
for each token in expr:
    if token == operand:
        outstack.append(token)
    if token == '(':
        opstack.push(token)
    if token == ')':
        # opstak에 저장된 연산자 pop 한다.
        # '(' 를 pop 할 때 까지 pop해서 outstack에 append
    if token in '+*-/':
        # opstack에 token보다 우선순위가 높은 연산자 모두 pop
        # 이후 자신이 push
opstack에 남아있는 연산자 모두 pop 후 outstack으로 표현

예시1)
6 + (3 - 2) * 4 = 6 3 2 - 4 * +
1. 6 outstack , + opstack
2. '(' opstack, 3 outstack
3. 2 outstack, ')' = = - pop, '(' pop
4. * opstack, 4 outstack
5. * pop, + pop

for each token in postfix.exr:
if token == operand:
    S.push(token)
if token in '+,-,*,/':
    a = S.POP() # 2 retrun
    b = S.pop() # 3 retrun 후 3 - 2 = 1
    S.push(a token b) # token : +,-,*,/
# 두번의 pop과 연산자의 계산 후 1번의 push
1. a = 4 pop, b = 1 pop, 후 * 연산자 및 push
2. a = 4 pop, b = 6 pop, 후 + 연산자 및 push # = 10 (Stack에 남아있는 값)