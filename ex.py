import urllib.request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = urllib.request.Request("http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_main.daum?person_id=778542")
    data = urllib.request.urlopen(URL).read()

    soup = BeautifulSoup(data, 'html.parser')
