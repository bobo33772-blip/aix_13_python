t1 = (1,3,5)
print(t1)
print(t1[1])
# t1[1] = 4 # 오류. 튜플은 변경불가능
t2 = [3]
print(type(t2)) # <class 'list'>
t2 = (3)
print(type(t2)) # <class 'int'>
# 학생들의 점수를 입력받아 총점과 평균계산
def calc_total_avg(*values):
    total = 0
    avg = 0
    total = sum(values)
    avg = total/len(values)
    return total, avg # 소괄호 생략되어있음 -> 튜플

t, a = calc_total_avg(10,30,50)
print("total",t) # total
print("avg",a) # avg

a,b = 10, 20
print(a,b)
a,b = b,a
print(a,b)

# print(calc_total_avg)

def print_func(fn):
    fn(); fn(); fn()
def hello():
    print("HELLO")
print_func(hello)

"""
숫자맞추기게임(UpDown)
1~100사이 임의의숫자를 컴퓨터가 정한것을
스무고개형식으로 맞추는 게임
출력예시)
1~100사이 숫자 입력>> 70
낮춰주세요
후보숫자>> 1 2 3 4 5 6........68 69
1~100사이 숫자 입력>> 60
높여주세요
후보숫자>> 61 62 63 64...68 69
1~100사이 숫자 입력>> 65
낮춰주세요
후보숫자>> 61 62 63 64
6번째시도 : 1~100사이 숫자 입력>> 63
정답입니다
"""

print("### 숫자맞추기게임 v0.1 ###")
#1~100사이 임의의정수를 저장
import random
com = random.randint(1,100)
count, low, high = 1,1,100
while True:
    user = int(input(f"{count}번째 시도: 1~100사이 숫자 입력>> "))
    count += 1
    if com == user:
        print("정답입니다")
        break # 반복문 종료
    if com < user:
        print("낮춰주세요")
        high=user-1
    else:
        print("높여주세요")
        low=user+1
    print("후보 숫자:",list(range(low,high+1)))
    if count > 6:
        print("정답은",com,"당신은 바보입니까?")
        break
