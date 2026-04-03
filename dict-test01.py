m1 = {"name":"어벤저스 엔드게임","type":"히어로 무비"}
# print(m1)
# 학생정보
# 정의 할 때 중괄호, 변수 print 할 때 대괄호
st1 = {"name":"홍길동", "hakbun":1120}
print(st1["name"]) # 홍길동
print(st1["hakbun"]) #1120
scoredict = {
    "홍길동":{"국어":80,"영어":70,"수학":90},
    "김길동":{"국어":70,"영어":70,"수학":90}
    }
print("홍길동의 수학점수",scoredict["홍길동"]["수학"])

n = "홍길동"
# 키는 immutable objuct만 가능. 불변객체
dic1 = {
    n : 90
}
print(dic1)
dic2 = {
    "abc": 90
    }
print(dic2)
dict3 = dict() #빈 사전
print(dict3)
dict3["a"] = 70
dict3["b"] = 80
dict3["a"] = 100
print(dict3)
print("삭제후",dict3)
# del dict3("a")
# scores = dict()
# scores["홍길동"] = {
#     "guk":80, "mate":90, "eng":90
# }
# scores["박길동"]= {
#     "guk":80, "mate":90, "eng":70
# }
# name = input("학생이름>> ")
# # if name in scores:
# #     print(f"{name}의 점수 {scores[name]}")
# # else:
# #     print(f"{name}은 미등록학생")
# value = scores.get(name)
# if value == None: 
#     print(f"{name}은 미등록학생")
# else:
#     print(f"{name}의 점수 {scores[name]}")
scores2 = {
    "홍":70, "김":80, "강":75, "권":90
}
for k in scores2:
    print(f"{k} {scores2[k]}")