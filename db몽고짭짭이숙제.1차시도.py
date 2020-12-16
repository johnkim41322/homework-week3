from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

#지니뮤직의 1~50위 곡의 정보를 스크래핑 (30분 예상)

#순위 /#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#곡 제목  #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#가수를 #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis


# 아래 빈 칸('')을 채워보세요
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
print(trs)

# 아래 빈 칸('')을 채워보세요
for tr in trs:
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    #print(title)
    rank = tr.select_one('td.number').text[0:2].strip()
    #***랭크부분에서 순위가 제대로 출력이 안됨!!!! ***
    #print(rank.text[0:2].strip())
#      td.info > a.title.ellipsis
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    #print(artist)
    #print(rank, title, artist)
    #여기까지 달달이 맛

    # 인서트할때, doc 먼터는 언제 어떻게 만드나 ???
    doc = {
        'rank':rank,
        'title':title,
        'artist':artist
    }

    db.genie.insert_one(doc)

   ## db몽고 데이터 인서트 반드시 혼자 해 볼것



