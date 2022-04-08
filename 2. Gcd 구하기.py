Gcd : 최대공약수 계산 알고리즘

gcd(8,12) = max{1,2,4} = 4 (최대공약수)

gcd_sub(차)
def gcd(a,b):
    while a != 0 and b != 0:
        if a > b: a = a - b
        else : b = b - a
    returan a + b
# 50번 while 문 반복후 a or b 가 0이 될 시 while 문 종료 후 a + b return
gdc(2,100) = gcd(2,98) = gcd(2,96) = gcd(2,94) ... gcd(2,0)
# 큰 수가 작은수보다 작아질 때 까지 반복

gcd_mod(나머지)
def gcd(a,b):
    while a != 0 and b != 0:
        if a > b: a = a % b
        else : b = b % a
    returan a + b
# 큰수에서 작은 수를 나눠서 나오는 나머지 계산 후 a + b return
gcd(2,100) = gcd(2,0) 

gdc_rec(재귀) - 자기함수를 재귀적으로 호출해서 도출
gcd(a,b) = gcd(a, b%a) or gcd(a%b, b)
# gcd_sub 함수의 재귀
def gcd_rec(a,b)
    if a*b == 0:
      return a + b
    if a > b:
      a = a - b
    else :
      b = b - a
    return gcd_rec(a, b)