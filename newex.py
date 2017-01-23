import requests
from lxml import etree
url = 'http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_main.daum?person_id=778542'
respose = requests.get(url)
html = etree.HTML(respose.text)

for x in range(17):
    elements = html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/thead/tr/th[%d]' % x)
    if elements:
        print(elements[0].text)
    elements = html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/tbody/tr/td[%d]' % x)
    if elements:
        print(elements[0].text)
