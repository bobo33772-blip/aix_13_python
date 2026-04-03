s = "abc"
s2 = 'abc'
s3 = """abc"""
# 줄바꿈을 가능하게 하는 트리플따옴표 
s4 = '''
강나루 건너서
밀밭길을
구름에 달 가듯이
가는 나그네
'''
print(s4)
# /s2 = 'TOM's Bear' 따옴표 오류를 없애는 방법 2가지
s2 = "TOM's Bear"
print(s2)
s2 = 'TOM\'s Bear'
print(s2)
s5 = "홍길동"
s6 = "안녕하세요"
print(s5+" "+s6)
# print(s5 + 5) # 오류 : 문자열 + 수식은 오류, 이후 코드동작 x
# print("홍길동"" " * 3)
print((s5+" ") * 3)
print("홍길동"[0]) # 홍
print("홍길동"[1]) # 길
print("홍길동"[2]) # 동
print(s5[0]) # 홍
print(s5[1]) # 길
print(s5[2]) # 동
print(s5[-1]) # 동
print(s5[-2]) # 길
print(s5[-3]) # 홍