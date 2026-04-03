# 인사말함수
def hello():
    print("안녕하세요")
def hello_ntimes(msg="안녕하세요",n=1):
    for i in range(n):
        print(msg)

# hello_ntimes("방가방가",5)
# gugudan(3) -> 3단 구구단 출력
# gugudan() -> 2단 구구단 출력

# def gugudan(n=2):
#     for i in range(1,10):
#         print(f"{n}*{i}={n*i}")
# gugudan()

# def gugudan(n=2,n2=-1):
#     if n2 == -1:
#         for i in range(1,10):
#             print(f"{n}*{i}={n*i}")
#     else:
#         for j in range(n,n2+1):
#             for i in range(1,10):
#                 print(f"{j}*{i}={j*i}")
# gugudan(2,5)
# n = [10,20,30]
# for i in n:
#     print("변수 =",i)

# list = [100,200,300]
# for i in list:
#  print(i+10)

# l = ["김밥","라면","튀김"]
# for i in l:
#     print("오늘의 메뉴:",i)

# def print_coin():
#     for i in range(100):
#         print("비트코인")
    
# print_coin()


