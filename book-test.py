# a = input("> 1번째 숫자: ")
# b = input("> 2번째 숫자: ")
# print()

# # print("{} + {} = {}".format(int(a),int(b),int(a)+int(b)))

# string = "hello"
# string.upper()
# print("A 지점:",string)
# print("B 지점:",string.upper())

# r = int(input("구의 반지름을 입력해주세요: "))
# pi = 3.141592
# print()
# print(f"구의 부피는 {(4/3)*pi*r**3}입니다.")
# print(f"구의 겉넓이는 {4*pi*r**2}입니다.")

# a = float(input("밑변의 길이를 입력해주세요: "))
# b = float(input("높이의 길이를 입력해주세요: "))
# c = a**2+b**2
# print(f"= 빗변의 길이는 {c**(1/2)}입니다.")

ans = input("입력:")
import datetime
now = datetime.datetime.now()

if ans in ["안녕","안녕하세요"]:
    print("> 안녕하세요")
if "몇 시" in ans:
    print(f"지금은 {now.hour}시 입니다.")
else:
    print(">",ans)

num = int(input("정수를 입력해주세요: "))

if num%2 == 0:
    print(f"{num}은 2로 나누어 떨어지는 숫자입니다.")
else :
    print(f"{num}은 2로 나누어 떨어지는 숫자가 아닙니다.")
if num%3 == 0:
    print(f"{num}은 3로 나누어 떨어지는 숫자입니다.")
else :
    print(f"{num}은 3로 나누어 떨어지는 숫자가 아닙니다.")
if num%4 == 0:
    print(f"{num}은 4로 나누어 떨어지는 숫자입니다.")
else :
    print(f"{num}은 4로 나누어 떨어지는 숫자가 아닙니다.")
if num%5 == 0:
    print(f"{num}은 5로 나누어 떨어지는 숫자입니다.")
else :
    print(f"{num}은 5로 나누어 떨어지는 숫자가 아닙니다.")
    
list_a = [0,1,2,3,4,5,6,7]
list_a.remove(3)
print(list_a)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number > 100:
        print("- 100 이상의 수:",number)

for number in numbers:
    if number%2 == 0:
        print(number,"는 짝수입니다.")
    else :
        print(number,"는 홀수입니다.")

for number in numbers:
    if len(str(number)) == 1:
        print(number,"는 1 자릿수입니다.")
    if len(str(number)) == 2:
        print(number,"는 2 자릿수입니다.")
    if len(str(number)) == 3:
        print(number,"는 3 자릿수입니다.")

numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number-1)%3].append(number)
print(output)

numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(numbers)//2) :
    j = i*2+1
    print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j]**2
print(numbers)