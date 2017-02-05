import pymysql
connection = pymysql.connect(host='', user='', password='', db='test', charset='utf8')
curs = connection.cursor()
sql = """
INSERT INTO test.person (name) VALUES (%(name)s)
"""
curs.execute(query=sql, args={'name':'김석영'})
connection.commit()

curs.close()
connection.close()