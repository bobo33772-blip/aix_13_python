# # print(a)
# a = list("12345")
# print("-".join(a))
# a = ["1","2,","3"] #ok
# a = [1,2,3]
# a = [str(n) for n in a]
# print("-".join(a))

#짝수홀수 변환
a = range(5)
# [참일때값 if 조건식 else 거짓일때값 for 변수 in 자류구조}]
b= ["짝" if n%2==0 else"홀"
            for n in a]
print(b)