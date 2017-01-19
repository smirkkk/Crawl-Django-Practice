import requests
from lxml import etree
url = 'http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_main.daum?person_id=778542'
respose = requests.get(url)
html = etree.HTML(respose.text)
elements = html.xpath('//*[@id="mArticle"]/div/div[2]/div[2]/strong')
if elements:
    print (elements[0].text)
