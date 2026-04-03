from urllib import request
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+%EC%84%9C%EC%9A%B8&oquery=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+%EC%84%9C%EC%9A%B8&tqi=jN8KvsqXKZwsskOzQhR-283947&ackey=8d5z38ta"
target = request.urlopen(url) # 접속정보 등록
soup = BeautifulSoup(target, "html.parser")

tag = "div.detail_info.lv3 > dl" # 미세먼지 오전
temp = soup.select_one(tag).get_text() # 포함한 모든 글자 추출
temp = ' '.join(temp.split())
print('Dust:',temp)

tag = "div.detail_info.lv2 > dl" # 미세먼지 오후 
temp = soup.select_one(tag).get_text() # 포함한 모든 글자 추출
temp = ' '.join(temp.split())
print('Dust:',temp)
# temp = soup.select('dd.lvl') #여러개
# print(list(temp))