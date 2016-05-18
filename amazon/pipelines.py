# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import pymysql
import cgi

class AmazonPipeline(object):
    def process_item(self, item, spider):
        return item
class AmazonBooksFilePipeline(object):
    def __init__(self):
        self.filename='amazon_book.json'
        self.file = codecs.open(self.filename, 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))  
        if(spider.pipeline=='bookComment'):
            pass
        return item


class AmazonBooksDbPipeline(object):

    def booksType(self):
        sql="INSERT INTO books_type (type_name,type_num,type_link) VALUES (%s,%s,%s)"
        self.cur.execute(sql,(self.item['typeName'][0],self.item['typeNum'][0],self.item['typeLink'][0]))
        self.conn.commit()

    def booksList(self):
        sql="INSERT INTO book_info (book_name,book_author,book_time,book_price,book_star,book_link) VALUES (%s,%s,%s,%s,%s,%s)"
        bookAu=''
        try:
            bookAu=self.item['bookAuthor'][0]+self.item['bookAuthor2'][0]
            if bookAu=='':
                bookAu=self.item['bookAuthor'][0]
        except:
            pass
        self.cur.execute(sql,(self.item['bookName'][0],bookAu,self.item['bookTime'][0],self.item['bookPrice'][0],self.item['bookStar'][0],self.item['bookLink'][0]))
        self.conn.commit()

    def bookContent(self):
        sql="UPDATE book_info SET book_content=%s,book_comment_url=%s ,book_comment_num=%s WHERE book_name=%s"
        bookCo=''
        bookUr=''
        bookNu=''
        try:
            bookCo=cgi.escape(self.item['bookContent'][0])
            bookUr=self.item['bookCommentUrl'][0]
            bookNu=self.item['bookCommentNum']
        except:
            pass
        self.cur.execute(sql,(bookCo,bookUr,bookNu,self.item['bookName'][0]))
        self.conn.commit()

    def bookComment(self):
        sql="INSERT INTO book_comment (book_name,comment_star,comment_title,comment_time,comment_content) VALUES(%s,%s,%s,%s,%s)"
        name=''
        star=''
        title=''
        time=''
        content=''
        try:
            name=self.item['bookName'][0]
            star=self.item['bookCommentStar'][0]
            title=self.item['bookCommentTitle'][0]
            time=self.item['bookCommentTime'][0]
            content=cgi.escape(self.item['bookCommentContent'][0])
        except:
            pass
        self.cur.execute(sql,(name,star,title,time,content))
        self.conn.commit()

    funcDict={'booksType':booksType,'booksList':booksList,'bookContent':bookContent,'bookComment':bookComment}

    def __init__(self):
        self.db_init()

    def db_init(self):
        self.conn=pymysql.connect(host='input.your.mysql.host',user='your user name',passwd='your password',db='amazon',port=3306,charset='utf8')
        self.cur=self.conn.cursor()
        sql='TRUNCATE books_type'
        self.cur.execute(sql)
        sql='TRUNCATE book_info'
        self.cur.execute(sql)
        sql='TRUNCATE book_comment'
        self.cur.execute(sql)

    def process_item(self,item,spider):
        self.item=item
        self.func(spider.pipeline)
        return item

    def func(self,op):
        exe=self.funcDict.get(op)(self)






