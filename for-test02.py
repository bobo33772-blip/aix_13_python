nums = list(range(1,46))
# print('nums',nums)
mylotto = [] #로또번호저장용
for a in [1,2,3,4,5,6]:
    import random
    r = random.randint(0,len(nums)-1)
    mylotto.append(nums[r]) #로또번호저장
    nums.pop(r) #저장한 번호 삭제. 중복선택불가
mylotto.sort()
print('mylotto', mylotto)