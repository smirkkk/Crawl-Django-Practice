import urllib.request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = urllib.request.Request("http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_main.daum?person_id=778542")
    data = urllib.request.urlopen(URL).read()

    soup = BeautifulSoup(data, 'html.parser')

    #print(soup.findAll(id='mArticle'))

    th = soup.findAll('table')

    for x in th:
        string = x.get('class')
        print(string)
        if string[1] == "tbl_season":
            print(x)
        else:
            break
   # // *[ @ id = "mArticle"] / div / div[3] / div / table