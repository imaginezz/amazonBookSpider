# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class AmazonBooksTypeItem(scrapy.Item):
    typeName=scrapy.Field()
    typeNum=scrapy.Field()
    typeLink=scrapy.Field()
class AmazonBooksListItem(scrapy.Item):
    bookName=scrapy.Field()
    bookAuthor=scrapy.Field()
    bookAuthor2=scrapy.Field()
    bookTime=scrapy.Field()
    bookPrice=scrapy.Field()
    bookStar=scrapy.Field()
    bookLink=scrapy.Field()
class AmazonBookContentItem(scrapy.Item):
    bookName=scrapy.Field()
    bookContent=scrapy.Field()
    bookCommentUrl=scrapy.Field()
    bookCommentNum=scrapy.Field()
class AmazonBookCommentItem(scrapy.Item):
    bookName=scrapy.Field()
    bookCommentStar=scrapy.Field()
    bookCommentTitle=scrapy.Field()
    bookCommentTime=scrapy.Field()
    bookCommentContent=scrapy.Field()
