import requests
from lxml import etree
url = 'http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_main.daum?person_id=778542'
respose = requests.get(url)
html = etree.HTML(respose.text)

url2 = 'http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_rechist.daum?person_id=778542'
respose = requests.get(url2)
html2 = etree.HTML(respose.text)

season_data = {}
total_data = {}
profile = {}

# 단순 17 이라 고 해서 반복으로 추출 하기 보다는 그냥 0,1,2 ~ 16 해도 상관 없음
# 이 데이터들을 DB 적재 하기 좋은 방법을 생각 해보기

#a = html2.xpath('//*[@id="mArticle"]/div/div[3]/div/table/thead/tr/th[3]')


#프로필
for x in range(5):
    profile_label = html.xpath('//*[@id="mArticle"]/div/div[2]/div[3]/dl[{}]/dt'.format(x))
    profile_value = html.xpath('//*[@id="mArticle"]/div/div[2]/div[3]/dl[{}]/dd'.format(x))

    if profile_label:
        profile[profile_label[0].text.strip(" :")] = profile_value[0].text.strip()
        # print(profile_label[0].text.strip(" :"))
        # print(profile_value[0].text.strip())

#시즌 기록
for x in range(17):
    # python string format 방법 확인 하기
    # https://docs.python.org/3.5/library/stdtypes.html#str.format
    titles = html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/thead/tr/th[{}]'.format(x))
    values = html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/tbody/tr/td[{}]'.format(x))

    if titles:
        season_data[titles[0].text] = values[0].text.strip()

#통산기록
for x in range(3, 19):
    title = html2.xpath('//*[@id="mArticle"]/div/div[3]/div/table/thead/tr/th[{}]'.format(x))
    value = html2.xpath('//*[@id="mArticle"]/div/div[3]/div/table/tfoot/tr/td[{}]'.format(x))

    total_data[title[0].text] = value[0].text.strip()


print(season_data)
print(profile)
print(total_data)