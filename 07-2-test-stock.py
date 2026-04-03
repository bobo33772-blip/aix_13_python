from urllib import request
from bs4 import BeautifulSoup

#삼성전자 주가 추출

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90+%EC%A3%BC%EA%B0%80&ackey=wfcjfng5"
target = request.urlopen(url) # 접속정보 등록
soup = BeautifulSoup(target, "html.parser")

tag = "a._target > strong" # 주가
stock = soup.select_one(tag).get_text() # 포함한 모든 글자 추출
stock = ' '.join(stock.split())
print('stock:',stock)
print("end")