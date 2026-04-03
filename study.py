# 1. M7 종목과 수익률을 담은 리스트 (혼공파 4장: 리스트 기본)
# 순서: GOOGL, TSLA, META, AMZN, AAPL, NVDA, MSFT
m7_returns = [3.4, 2.6, 1.2, 1.1, 0.7, 0.7, -0.2]

# 2. 내림차순 정렬 (큰 숫자부터 작은 숫자 순서)
# reverse=True 옵션을 넣으면 내림차순이 됩니다.
m7_returns.sort(reverse=True)

print(f"내림차순 정렬된 수익률: {m7_returns}")
# 평균을 계산하는 함수 정의 (혼공파 5장: 함수)
def calculate_average(returns_list):
    # sum(): 리스트 안의 숫자를 다 더함
    # len(): 리스트 안의 데이터 개수를 셈
    total = sum(returns_list)
    count = len(returns_list)
    
    average = total / count
    return average

# 함수 실행 및 결과 출력
m7_avg = calculate_average(m7_returns)

# round(값, 2)를 사용해 소수점 둘째 자리까지 반올림합니다.
print(f"M7 종목의 오늘 평균 수익률은 {round(m7_avg, 2)}% 입니다.")