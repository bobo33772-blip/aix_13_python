# 구구단출력 - 3단
# 3 * 1 = 3
# 3 * 2 = 6
dan = 3
# print( str(dan) + " * ") 더 간단한 방법 format
print("{} * {} = {}".format(dan,1,dan*1))
print("{} * {:5d} = {}".format(dan,1,dan*1))
print("{} * {:05d} = {}".format(dan,1,dan*1))

print("헬로 python 프로그래밍".upper())
a = """
    헬로 파이썬 프로그래밍    
"""
print(a.strip()) # 공백 제거
print(a.strip()+"/")
print(a.strip()+"/")
print("안녕123".isalnum()) # 문자열이 알파벳 또는 숫자로만 구성되어있는지 확인
print("abc abc programming".find("ab"))
print("abc abc programming".find("p"))
print("abc abc programming".find("g",2))
a = "안녕하세요"
print( "안녕" in a)
print( "힘드네요" in a)
b = "홍,김,박,강".split(",")
print(b)
b = "100,200,300,400".split(",")
print(b)
print(int(b[0])+int(b[1]))
print(b[0]+b[1])
#합과 평균
total = 0
mean = 0
total = int(b[0]) + int(b[1]) + int(b[2]) + int(b[3])
print("total={}".format(total))
print("Average{}".format(total/4))
print("total="+str(total))
print(f"total={total}")
print(f"평균={total/4}")
# 구구단 3단 
dan = 3
print(f"{dan} * {1} = {dan*1}")
print(f"{dan} * {2} = {dan*2}")
print(f"{dan} * {3} = {dan*3}")

# 생년을 입력받아 나이를 계산해서 출력하기
year = input("태어난해 4자리를 입력하세요")
age = 2026 - int(year)
print(f"당신은 {age}살 입니다")
