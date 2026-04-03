from urllib import request
from bs4 import BeautifulSoup

#뉴스 기사 추출

url = "https://news.naver.com/section/105"
target = request.urlopen(url) # 접속정보 등록
soup = BeautifulSoup(target, "html.parser")

tag = "li.rl_item .rl_txt" # 뉴스 헤드라인
stock = soup.select(tag) # 포함한 모든 글자 추출
for t in stock:
    title = t.get_text()
    print('headline:',title)
