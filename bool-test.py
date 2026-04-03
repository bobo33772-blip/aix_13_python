print(10 == 100)
print(10 != 100) #  != : 다르다
print(10<=100)
print(10>=100)
a = "가방"
b = "하마"
print( a == b)
print( a < b) # 글자의 순서 
c = 35
print( 10 < c < 30)
print( 10 < c < 20)
if c < 30:
    print("c는 30보다 작음") # if문 들여쓰기 필수 탭 누르기
else:
    print( "c는 30보다 큼")
print("END")
score = 99
grade = ""
if score > 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >=70:
    grade = "C"
else:
    grade = "F"
print(f"{score}의 학점은 {grade}")
#################
score = 78
if score <= 100 and score >= 90:
    grade = "A"
elif score <= 89 and score >=80:
    grade = "B"
else:
    grade = "F"
print(f"{score}의 학점은 {grade}")