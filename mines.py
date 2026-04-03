# 지뢰찾기(빨리 터트리기)
# 10x10 영역에 3개의 지뢰를 매설
# 최소의 시도로 모두 터트리기
# 실력대로 해보기
# 초급(5x5-2), 중급(7x7-4), 고급(10x10-7)
# 레벨을 선택하세요
# 1 - 초급(5x5) 지뢰 2개 
# 2 - 중급(7x7) 지뢰 4개 
# 3 - 고급(10x10) 지뢰 6개
# 선택 레벨>> 
while True:
    level = input("레벨 선택 (1:초급, 2:중급, 3:고급) >> ")

    if level == "1":
        size = 5
        M = 2
        break
    elif level == "2":
        size = 7
        M = 4
        break
    elif level == "3":
        size = 10
        M = 6
        break
    else:
        print("잘못 입력했습니다. 다시 입력하세요.")

import random

mines = []
for i in range(size):
    mines.append(['+']*size)
nums = [] #계산용
for i in range(size):
    nums.append([0]*size)
# 임의의지점에 지뢰 저장(3개)
mine_count = 0
while mine_count < M:
    row = random.randint(0,size-1)
    col = random.randint(0,size-1)
    #폭탄이 같은자리인경우 배치취소
    if nums[row][col] >= 9: continue 
    mine_count += 1 # 배치폭탄 갯수 1 증가
    nums[row][col]=9
    # 이웃한 8개 방의 숫자를 1증가 , 오류 방지를 위한 if문
    if row !=0 and col !=0 : nums[row-1][col-1] += 1
    if row !=0 : nums[row-1][col] += 1
    if row !=0 and col !=size-1 : nums[row-1][col+1] += 1
    if col !=size-1 : nums[row][col+1] += 1
    if row !=size-1 and col !=size-1 :nums[row+1][col+1] += 1
    if row !=size-1 :nums[row+1][col] += 1
    if row !=size-1 and col !=0 :nums[row+1][col-1] += 1
    if col !=0 :nums[row][col-1] += 1
# 확인
# for i in nums:
#print(i)
remain_mine = mine_count# 남은 폭탄갯수
tries = 0
while remain_mine !=0:
    print(f"남은 지뢰: {remain_mine}개")
    msg=f'지뢰의 좌표를 입력하세요(0~{size-1},0~{size-1}) x,y>> '
    ans = input(msg)
    try:
        u_row, u_col = ans.split(',')
        u_row, u_col = int(u_row), int(u_col)
        if not (0 <= u_row < size and 0 <= u_col < size):
            print("좌표를 잘못 입력하였습니다.")
            continue
    except:
        print("좌표를 잘못 입력하였습니다.")
        continue
    tries += 1
    if nums[u_row][u_col] >= 9: #지뢰 찾으면
        mines[u_row][u_col]="$"
        remain_mine -= 1 #남은 폭탄 갯수
    else:
        mines[u_row][u_col]=str(nums[u_row][u_col])
        # mines 리스트 출력
    for m in mines:
         print(" ".join(m))
print(f"{tries}번 만에 성공!")