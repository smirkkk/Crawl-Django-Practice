import requests
from lxml import etree
import pymysql

tmp = pymysql.connect(host='localhost', user='root', password='', db='sports', charset='utf8')
curs = tmp.cursor()

season_data = {}
total_data = {}
daily_data = {}
profile = {}


class basic():

    na = ['http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_main.daum?person_id=778542',
          'http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_rechist.daum?person_id=778542']

    park = ['http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_main.daum?person_id=778528',
            'http://score.sports.media.daum.net/record/baseball/kbo/plrinf_bat_rechist.daum?person_id=778528']

    url = na[0]
    respose = requests.get(url)
    html = etree.HTML(respose.text)

    url2 = na[1]
    respose = requests.get(url2)
    html2 = etree.HTML(respose.text)

    name = html.xpath('//*[@id="mArticle"]/div/div[2]/div[2]/strong')
    name = name[0].text
    print(name)

    # 프로필
    def crawl_profile(self):
        profile['이름'] = self.name
        for x in range(5):
            profile_label = self.html.xpath('//*[@id="mArticle"]/div/div[2]/div[3]/dl[{}]/dt'.format(x))
            profile_value = self.html.xpath('//*[@id="mArticle"]/div/div[2]/div[3]/dl[{}]/dd'.format(x))

            if profile_label:
                profile[profile_label[0].text.strip(" :")] = profile_value[0].text.strip()

    # 프로필 DB 삽입
    def db_profile(self):
        sql = 'select * from `sports`.`profile`'
        curs.execute(sql)
        rows = curs.fetchall()

        if len(rows) == 0:
            print('빔')
            sql = """
                    INSERT INTO `sports`.`profile` (`이름`, `데뷔`, `출생`, `포지션`, `신체`) VALUES (%(이름)s, %(데뷔)s, %(출생)s, %(포지션)s, %(신체)s)
                    """

            curs.execute(query=sql,
                         args={'이름': profile['이름'], '데뷔': profile['데뷔'], '출생': profile['출생'], '포지션': profile['포지션'],
                               '신체': profile['신체']})
            tmp.commit()
        elif str(rows[len(rows) - 1][1]) == self.name:
            print('이미있음')
            return
        else:
            print('추가')
            sql = """
            INSERT INTO `sports`.`profile` (`이름`, `데뷔`, `출생`, `포지션`, `신체`) VALUES (%(이름)s, %(데뷔)s, %(출생)s, %(포지션)s, %(신체)s)
            """

            curs.execute(query=sql,
                         args={'이름': profile['이름'], '데뷔': profile['데뷔'], '출생': profile['출생'], '포지션': profile['포지션'],
                               '신체': profile['신체']})
            tmp.commit()

    # 시즌 기록
    def crawl_season(self):
        for x in range(17):
            titles = self.html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/thead/tr/th[{}]'.format(x))
            values = self.html.xpath('//*[@id="mArticle"]/div/div[3]/div/table/tbody/tr/td[{}]'.format(x))

            if titles:
                season_data[titles[0].text] = values[0].text.strip()

    # 시즌 기록 DB 삽입
    def db_season(self):
        sql = 'TRUNCATE `season_record`'
        curs.execute(sql)

        sql = """
        INSERT INTO `sports`.`season_record` (`경기`, `타석`, `타수`, `안타`, `2루타`, `3루타`, `홈런`, `타점`, `득점`, `도루`, `사사구`, `삼진`, `타율`, `출루율`, `장타율`, `OPS` ) VALUES (%(경기)s, %(타석)s, %(타수)s, %(안타)s, %(2루타)s, %(3루타)s, %(홈런)s, %(타점)s, %(득점)s, %(도루)s, %(사사구)s, %(삼진)s, %(타율)s, %(출루율)s, %(장타율)s, %(OPS)s)
        """

        curs.execute(query=sql,
                     args={'경기': season_data['경기'], '타석': season_data['타석'], '타수': season_data['타수'], '안타': season_data['안타'], '2루타': season_data['2타'], '3루타': season_data['3타'], '홈런': season_data['홈런'], '타점': season_data['타점'], '득점': season_data['득점'], '도루': season_data['도루'], '사사구': season_data['사사구'], '삼진': season_data['삼진'], '타율': season_data['타율'], '출루율': season_data['출루율'], '장타율': season_data['장타율'], 'OPS': season_data['OPS']})

        tmp.commit()

    # 일일 기록
    def crawl_daily(self):
        for x in range(20):
            titles = self.html.xpath('//*[@id="mArticle"]/div/div[3]/div/div[1]/table/thead/tr/th[{}]'.format(x))
            values = self.html.xpath('//*[@id="mArticle"]/div/div[3]/div/div[1]/table/tbody/tr[1]/td[{}]'.format(x))

            if titles:
                daily_data[titles[0].text] = values[0].text.strip()

    # 일일 기록 DB 삽입
    def db_daily(self):
        sql = 'select * from `sports`.`daily_record`'
        curs.execute(sql)
        rows = curs.fetchall()
        if len(rows) == 0:
            sql = """
            INSERT INTO `sports`.`daily_record` (`날짜`, `상대`, `타석`, `타수`, `안타`, `2루타`, `3루타`, `홈런`, `타점`, `득점`, `도루`, `사사구`, `삼진`, `타율`, `출루율`, `장타율`, `OPS` ) VALUES (%(날짜)s, %(상대)s, %(타석)s, %(타수)s, %(안타)s, %(2루타)s, %(3루타)s, %(홈런)s, %(타점)s, %(득점)s, %(도루)s, %(사사구)s, %(삼진)s, %(타율)s, %(출루율)s, %(장타율)s, %(OPS)s)
            """

            curs.execute(query=sql,
                         args={'날짜': daily_data['날짜'], '상대': daily_data['상대'], '타석': daily_data['타석'], '타수': daily_data['타수'],
                               '안타': daily_data['안타'], '2루타': daily_data['2타'], '3루타': daily_data['3타'],
                               '홈런': daily_data['홈런'], '타점': daily_data['타점'], '득점': daily_data['득점'],
                               '도루': daily_data['도루'], '사사구': daily_data['사사구'], '삼진': daily_data['삼진'],
                               '타율': daily_data['타율'], '출루율': daily_data['출루율'], '장타율': daily_data['장타율'],
                               'OPS': daily_data['OPS']})

            tmp.commit()

        elif str(rows[len(rows)-1][0]) == daily_data['날짜']:
            return
        else:
            sql = """
            INSERT INTO `sports`.`daily_record` (`날짜`, `상대`, `타석`, `타수`, `안타`, `2루타`, `3루타`, `홈런`, `타점`, `득점`, `도루`, `사사구`, `삼진`, `타율`, `출루율`, `장타율`, `OPS` ) VALUES (%(날짜)s, %(상대)s, %(타석)s, %(타수)s, %(안타)s, %(2루타)s, %(3루타)s, %(홈런)s, %(타점)s, %(득점)s, %(도루)s, %(사사구)s, %(삼진)s, %(타율)s, %(출루율)s, %(장타율)s, %(OPS)s)
            """

            curs.execute(query=sql,
                         args={'날짜': daily_data['날짜'], '상대': daily_data['상대'], '타석': daily_data['타석'], '타수': daily_data['타수'],
                               '안타': daily_data['안타'], '2루타': daily_data['2타'], '3루타': daily_data['3타'],
                               '홈런': daily_data['홈런'], '타점': daily_data['타점'], '득점': daily_data['득점'],
                               '도루': daily_data['도루'], '사사구': daily_data['사사구'], '삼진': daily_data['삼진'],
                               '타율': daily_data['타율'], '출루율': daily_data['출루율'], '장타율': daily_data['장타율'],
                               'OPS': daily_data['OPS']})
            tmp.commit()

    # 통산기록
    def crawl_total(self):
        for x in range(3, 19):
            title = self.html2.xpath('//*[@id="mArticle"]/div/div[3]/div/table/thead/tr/th[{}]'.format(x))
            value = self.html2.xpath('//*[@id="mArticle"]/div/div[3]/div/table/tfoot/tr/td[{}]'.format(x))

            total_data[title[0].text] = value[0].text.strip()

    # 통산 기록 DB 삽입
    def db_total(self):
        sql = 'TRUNCATE `total_record`'
        curs.execute(sql)


        sql = """
        INSERT INTO `sports`.`total_record` (`경기`, `타석`, `타수`, `안타`, `2루타`, `3루타`, `홈런`, `타점`, `득점`, `도루`, `사사구`, `삼진`, `타율`, `출루율`, `장타율`, `OPS` ) VALUES (%(경기)s, %(타석)s, %(타수)s, %(안타)s, %(2루타)s, %(3루타)s, %(홈런)s, %(타점)s, %(득점)s, %(도루)s, %(사사구)s, %(삼진)s, %(타율)s, %(출루율)s, %(장타율)s, %(OPS)s)
        """

        curs.execute(query=sql,
                     args={'경기': total_data['경기'], '타석': total_data['타석'], '타수': total_data['타수'], '안타': total_data['안타'], '2루타': total_data['2타'], '3루타': total_data['3타'], '홈런': total_data['홈런'], '타점': total_data['타점'], '득점': total_data['득점'], '도루': total_data['도루'], '사사구': total_data['사사구'], '삼진': total_data['삼진'], '타율': total_data['타율'], '출루율': total_data['출루율'], '장타율': total_data['장타율'], 'OPS': total_data['OPS']})

        tmp.commit()

if __name__ == '__main__':
    a = basic()

    a.crawl_profile()
    a.crawl_daily()
    a.crawl_season()
    a.crawl_total()

    a.db_profile()
    a.db_daily()
    a.db_season()
    a.db_total()

    print(season_data)
    print(profile)
    print(total_data)
    print(daily_data)