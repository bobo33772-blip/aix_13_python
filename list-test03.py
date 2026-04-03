names = []
scores =[]
names.append('홍')
scores.append(80)
names.append('김')
scores.append(90)
print(names)
print(scores)
# del names[1]
# names.pop(1)
# names.remove('김')
scores.clear()
print("scores=",scores)
print(names) 
############333
arr = [30,50,70,90]
# arr.sort()  # 정렬 기본은 오름차순
arr.sort(reverse=True) # 내림차순
print(arr)
