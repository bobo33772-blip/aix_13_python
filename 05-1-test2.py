# def print_n_times(*values,n=1): # 가변 매개변수가 앞에오면 오류
#     # n번 반복합니다
#     for i in range(n):
#         # values는 리스트처럼 활용합니다.
#         for value in values:
#             print(value)
#             # 단순한 줄바꿈
#         print()
# print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍",n=3)
# # 키워드 매개변수는 뒤쪽에 ex)n=3
# def return_test():
#     return 100
# value=return_test()
# print (value)

# greeting(이름) -> 출력: 안녕하세요 이름님
def greeting(name):
    return"안녕하세요 "+name+"님"

ans = greeting("홍길동") # -> 안녕하세요 홍길동님
print(ans)
# 입력받는 숫자들의 평균을 반환하는 함수
# ans = calc_avg(10,20,40,50,)
# ans = calc_avg(10,20)

# def calc_avg(*values):
#     tot = 0
#     for i in values:
#         tot += i
#     return tot / len(values)
# ans = calc_avg(10,20,40,50)
# print(ans)

# def calc_avg(*values):
#     return sum(values)/len(values)
# ans = calc_avg(10,20,40,50)
# print(ans)

# # 점수를 입력받아 학점을 반환하는 함수를 작성하시오.
# # 함수 이름: get_grade()
# def get_grade(s):
#     if s>=90:
#         return"A"
#     if s>=80:
#         return"B"
#     if s>=70:
#         return"C"
#     return "F"
# ans = get_grade(71)
# print(ans)

# 가위,바위,보 중 하나는 임의로 반환하는 함수
# 이름: get_gbb()
# ## 사용예시
# import random
# def get_gbb():
#     r = random.randint(0,2)
#     arr = '가위,바위,보'.split(',')
#     return arr[r]

# ans = get_gbb()
# print(ans)

# def fac(n):
#     if n==0:
#         return 1
#     return n * fac(n-1)
    


# ans = fac(3)
# print(ans)

