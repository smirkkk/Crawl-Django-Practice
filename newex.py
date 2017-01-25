import requests
from lxml import etree
url = 'http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_main.daum?person_id=778542'
respose = requests.get(url)
html = etree.HTML(respose.text)


# 단순 17 이라 고 해서 반복으로 추출 하기 보다는 그냥 0,1,2 ~ 16 해도 상관 없음
# 이 데이터들을 DB 적재 하기 좋은 방법을 생각 해보기
for x in range(17):
    # python string format 방법 확인 하기
    # https://docs.python.org/3.5/library/stdtypes.html#str.format
    titles = html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/thead/tr/th[{}]'.format(x))
    values = html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/tbody/tr/td[{}]'.format(x))
    if titles:
        print(x, titles[0].text, values[0].text.strip())