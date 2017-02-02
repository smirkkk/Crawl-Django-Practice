import requests
from lxml import etree
import pymysql

tmp = pymysql.connect(host='localhost', user='root', password='', db='sports', charset='utf8')
curs = tmp.cursor()

url = 'http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_main.daum?person_id=778542'
respose = requests.get(url)
html = etree.HTML(respose.text)

url2 = 'http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_rechist.daum?person_id=778542'
respose = requests.get(url2)
html2 = etree.HTML(respose.text)

url3 = 'http://www.koreabaseball.com/Record/Player/HitterDetail/Situation.aspx?playerId=62947'
respose = requests.get(url3)
html3 = etree.HTML(respose.text)


season_data = {}
total_data = {}
daily_data = {}
profile = {}


# 프로필
def crawl_profile():
    for x in range(5):
        profile_label = html.xpath('//*[@id="mArticle"]/div/div[2]/div[3]/dl[{}]/dt'.format(x))
        profile_value = html.xpath('//*[@id="mArticle"]/div/div[2]/div[3]/dl[{}]/dd'.format(x))

        if profile_label:
            profile[profile_label[0].text.strip(" :")] = profile_value[0].text.strip()


# 시즌 기록
def crawl_season():
    for x in range(17):
        titles = html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/thead/tr/th[{}]'.format(x))
        values = html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/tbody/tr/td[{}]'.format(x))

        if titles:
            season_data[titles[0].text] = values[0].text.strip()


# 통산기록
def crawl_total():
    for x in range(3, 19):
        title = html2.xpath('//*[@id="mArticle"]/div/div[3]/div/table/thead/tr/th[{}]'.format(x))
        value = html2.xpath('//*[@id="mArticle"]/div/div[3]/div/table/tfoot/tr/td[{}]'.format(x))

        total_data[title[0].text] = value[0].text.strip()


# 일일 기록
def crawl_daily():
    for x in range(20):
        titles = html.xpath('//*[@id="mArticle"]/div/div[3]/div/div[1]/table/thead/tr/th[{}]'.format(x))
        values = html.xpath('//*[@id="mArticle"]/div/div[3]/div/div[1]/table/tbody/tr[1]/td[{}]'.format(x))

        if titles:
            daily_data[titles[0].text] = values[0].text.strip()


# 시즌 기록 DB 삽입
def db_season():
    sql = 'TRUNCATE `season_record`'
    curs.execute(sql)

    sql = "INSERT INTO `sports`.`season_record` (`경기`, `타석`, `타수`, `안타`, `2루타`, `3루타`, `홈런`, `타점`, `득점`, `도루`, `사사구`, `삼진`, `타율`, `출루율`, `장타율`, `OPS`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(season_data['경기'], season_data['타석'], season_data['타수'], season_data['안타'], season_data['2타'], season_data['3타'], season_data['홈런'], season_data['타점'], season_data['득점'], season_data['도루'], season_data['사사구'], season_data['삼진'], season_data['타율'], season_data['출루율'], season_data['장타율'], season_data['OPS'])
    curs.execute(sql)
    tmp.commit()


# 프로필 DB 삽입
def db_profile():
    sql = 'TRUNCATE `profile`'
    curs.execute(sql)

    sql = "INSERT INTO `sports`.`profile` (`데뷔`, `출생`, `포지션`, `신체`) VALUES ('{}', '{}', '{}', '{}')".format(profile['데뷔'], profile['출생'], profile['포지션'], profile['신체'])
    curs.execute(sql)
    tmp.commit()


# 통산 기록 DB 삽입
def db_total():
    sql = 'TRUNCATE `total_record`'
    curs.execute(sql)

    sql = "INSERT INTO `sports`.`total_record` (`경기`, `타석`, `타수`, `안타`, `2루타`, `3루타`, `홈런`, `타점`, `득점`, `도루`, `사사구`, `삼진`, `타율`, `출루율`, `장타율`, `OPS`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(total_data['경기'], total_data['타석'], total_data['타수'], total_data['안타'], total_data['2타'], total_data['3타'], total_data['홈런'], total_data['타점'], total_data['득점'], total_data['도루'], total_data['사사구'], total_data['삼진'], total_data['타율'], total_data['출루율'], total_data['장타율'], total_data['OPS'])
    curs.execute(sql)
    tmp.commit()


# 일일 기록 DB 삽입
def db_daily():
    sql = 'select * from `sports`.`{}`'.format('daily_record')
    curs.execute(sql)
    rows = curs.fetchall()
    if len(rows) == 0:
        sql = "INSERT INTO `sports`.`daily_record` (`날짜`, `상대`, `타석`, `타수`, `안타`, `2루타`, `3루타`, `홈런`, `타점`, `득점`, `도루`, `사사구`, `삼진`, `타율`, `출루율`, `장타율`, `OPS`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            daily_data['날짜'], daily_data['상대'], daily_data['타석'], daily_data['타수'], daily_data['안타'], daily_data['2타'],
            daily_data['3타'], daily_data['홈런'], daily_data['타점'], daily_data['득점'], daily_data['도루'], daily_data['사사구'],
            daily_data['삼진'], daily_data['타율'], daily_data['출루율'], daily_data['장타율'], daily_data['OPS'])
        curs.execute(sql)
        tmp.commit()

    elif str(rows[len(rows)-1][0]) == daily_data['날짜']:
        return
    else:
        sql = "INSERT INTO `sports`.`daily_record` (`날짜`, `상대`, `타석`, `타수`, `안타`, `2루타`, `3루타`, `홈런`, `타점`, `득점`, `도루`, `사사구`, `삼진`, `타율`, `출루율`, `장타율`, `OPS`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(daily_data['날짜'],daily_data['상대'], daily_data['타석'], daily_data['타수'], daily_data['안타'], daily_data['2타'], daily_data['3타'], daily_data['홈런'], daily_data['타점'], daily_data['득점'], daily_data['도루'], daily_data['사사구'], daily_data['삼진'], daily_data['타율'], daily_data['출루율'], daily_data['장타율'], daily_data['OPS'])
        curs.execute(sql)
        tmp.commit()


def abcd():
    a = html3.xpath('//*[@id="_chartWrap"]/ul/li[1]/div/div[4]/span')
    print(a)


if __name__ == '__main__':
    abcd()

    crawl_profile()
    crawl_season()
    crawl_total()
    crawl_daily()

    db_season()
    db_profile()
    db_total()
    db_daily()

    print(season_data)
    print(profile)
    print(total_data)
    print(daily_data)
