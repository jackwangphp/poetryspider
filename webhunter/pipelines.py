# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.exceptions import DropItem


class MysqlWriterPipeline(object):
    def __init__(self):
        db_conf = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'jackwong',
            'db': 'poetry',
            'charset': 'utf8'
        }
        self.db = pymysql.connect(host=db_conf['host'], port=db_conf['port'], user=db_conf['user'],
                                  passwd=db_conf['password'], db=db_conf['db'], charset=db_conf['charset'])

    def process_item(self, item, spider):
        cursor = self.db.cursor()
        sql = "INSERT INTO poetry ( title, dynasty, poet, content ) VALUES ( '%s', '%s', '%s', '%s');" % (
        item['title'][0], item['dynasty'][0], item['poet'][0], item['content'][0])
        try:
            cursor.execute(sql)
            self.db.commit()
            return item
        except:
            self.db.rollback()
            raise DropItem("Mysql inset error%s" % sql)

    def close_spider(self, spider):
        self.db.close()
