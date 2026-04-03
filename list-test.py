#댄동회원관리
names = ['홍','김','박']
print(names[0])
print(names[1:2])
print(names[1:])
n = names[1:] #복사본 생성
names[1] = '이'
print(names)
print(names[1:][0])
print(n[0])

arr = [[1,2,3],[4,5,6]]
print(arr[0])
print(arr[1])
print(arr[0][-1])

a = [10,20,30]
b = [40,50,60]
print(a+b)
print(a+b)
print(a*3)
print(f"홍길동의 길이= {len("홍길동")}")
print(len(a+b))
print(len(a*9))
