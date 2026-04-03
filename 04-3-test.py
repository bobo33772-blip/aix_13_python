# print(range(3))
# print(list(range(3)))
# # print(list(range(1,46)))
# print(list(range(1,46,5)))
# print(list(range(5,1,-1)))
# # 3단구구단출력
# # 3*1=3
# # 3*2=6
# print(list(range(3,28,3)))
# dan = 5
# for i in range(1,10):
#     print(f"{dan}*{i}={dan*i}")
### 구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i}*{j}={i*j}")
# i=0
# while i<3: #i가 3보다 작은 동안 실행
#     print(f"i={i}")
#     i+=1 #생략하면 무한반복 crtl+c 로 종료
# print(f"while end i={i}")
# print("end")

# i=0
# while i<10: #0~9
#     print(f"i={i}")
#     i+=1
#     if i==2:
#         break

# ns = [5,15,6,20,7,25]
# for n in ns:
#     if n<10:
#         continue
#     print(n)

# a = [5,1,3]
# print(min(a))
# print(max(a))
# print(sum(a))
# print("avg=",sum(a)/len(a))
# a.sort()
# print("sorted",a)
# r=reversed(a)
# for v in r:
#     print(v)

a=[1,3,5]
b = ([i*10 for i in a])
print(b)

# #짝수만추출
# # a = [i for i in range(10) if i%2==0]
# # print(a)
# a = list("12345")
# print("-".join(a))
# a = ["1","2,","3"] #ok
a = [1,2,3]
a = [str(n) for n in a]
print("-".join(a))
