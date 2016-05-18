# -*- coding: utf-8 -*-
import scrapy
import string
import time
from scrapy.selector import Selector 
from scrapy.spiders import Spider
from scrapy.http import Request
from amazon.items import AmazonBooksTypeItem
from amazon.items import AmazonBooksListItem
from amazon.items import AmazonBookContentItem
from amazon.items import AmazonBookCommentItem


class BooksSpider(scrapy.Spider):
    name = "books_spider"
    pipeline="default"
    allowed_domains = ["amazon.cn"]
    start_urls = (
            'https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=topnav_storetab_b?ie=UTF8&node=658390051',
    )

    def parse(self, response):
        if response.status!=200:
            time.sleep(60)
            yield Request(response.url,meta=response.meta,callback=self.parse,dont_filter=True)
        self.pipeline="booksType"
        sel=Selector(response)
        lists=sel.xpath('.//div[@class="categoryRefinementsSection"]/ul[1]/li/a[1]')
        for l in lists:
            item=AmazonBooksTypeItem()
            name=l.xpath('span[1]/text()').extract()
            num=l.xpath('span[2]/text()').extract()
            link=l.xpath('@href[1]').extract()

            item['typeName']=[n.encode('utf-8') for n in name ]
            item['typeNum']=[n.encode('utf-8') for n in num ]
            item['typeLink']=[n.encode('utf-8') for n in link ]
            yield AmazonBooksTypeItem(item)
            for i in range(1,75):
                req=link[0]+'&page='+str(i)
                yield Request(req,callback=self.booksListParse,dont_filter=True)
        return

    def booksListParse(self,response):
        if response.status!=200:
            time.sleep(60)
            yield Request(response.url,meta=response.meta,callback=self.booksListParse,dont_filter=True)
        self.pipeline="booksList"
        sel=Selector(response)
        lists=sel.xpath('.//div[@id="mainResults"]/ul/li/div/div/div/div[2]')
        for l in lists:
            item=AmazonBooksListItem()
            name=l.xpath('div[2]/a/@title').extract()
            link=l.xpath('div[2]/a/@href').extract()
            author=l.xpath('div[2]/div/span[2]/text()').extract()
            author2=l.xpath('div[2]/div/span[3]/text()').extract()
            time=l.xpath('div[2]/span[3]/text()').extract()
            price=l.xpath('div[3]/div[1]/div[2]/a/span/text()').extract()
            star=l.xpath('div[3]/div[2]/div/span/span/a/i[1]/span/text()').extract()

            item['bookName']=[n.encode('utf-8') for n in name ]
            item['bookAuthor']=[n.encode('utf-8') for n in author ]
            item['bookAuthor2']=[n.encode('utf-8') for n in author2 ]
            item['bookTime']=[n.encode('utf-8') for n in time ]
            item['bookPrice']=[n.encode('utf-8') for n in price ]
            item['bookStar']=[n.encode('utf-8') for n in star ]
            item['bookLink']=[n.encode('utf-8') for n in link ]
            yield AmazonBooksListItem(item)
            req=link[0]
            yield Request(req,meta={'bookName':name},callback=self.bookContentParse,dont_filter=True)
        return

    def bookContentParse(self,response):
        if response.status!=200:
            time.sleep(60)
            yield Request(response.url,meta=response.meta,callback=self.bookContentParse,dont_filter=True)
        self.pipeline="bookContent"
        bookName=response.meta['bookName']
        sel=Selector(response)
        item=AmazonBookContentItem()
        content=sel.xpath('.//*[@id="iframeContent"]').extract()
        if len(content)<1:
            content=sel.xpath('.//*[@id="bookDescription_feature_div"]/noscript/div').extract()
        commenturl=sel.xpath('.//div[@id="revSum"]/div[2]/div/div[1]/a/@href').extract()
        commentnum=sel.xpath('.//div[@id="revF"]/div/a/text()').extract()
        print commentnum
        commentNum=''
        for i in range(len(commentnum[0])):
            if '0'<=commentnum[0][i]<='9':
                commentNum+=commentnum[0][i]
        item['bookName']=bookName
        item['bookContent']=[n.encode('utf-8') for n in content ] 
        item['bookCommentUrl']=[n.encode('utf-8') for n in commenturl ] 
        item['bookCommentNum']=commentNum
        yield AmazonBookContentItem(item)
        try:
            pageNum=(int(commentNum)/10)+1
            for i in range(1,pageNum):
                req=commenturl[0]+'?pageNumber='+str(i)
                yield Request(req,meta={'bookName':bookName},callback=self.bookCommentParse,dont_filter=True)
        except:
            pass
        return
    
    def bookCommentParse(self,response):
        if response.status!=200:
            time.sleep(60)
            yield Request(response.url,meta=response.meta,callback=self.bookCommentParse,dont_filter=True)
        self.pipeline="bookComment" 
        sel=Selector(response)
        bookcontent=AmazonBookCommentItem()
        lists=sel.xpath('.//div[@id="cm_cr-review_list"]/div')
        for l in lists:
            item=AmazonBookCommentItem()
            star=l.xpath('div[1]/a[1]/i/span/text()').extract()
            title=l.xpath('div[1]/a[2]/text()').extract()
            time=l.xpath('div[2]/span[4]/text()').extract()
            content=l.xpath('div[4]/span/text()').extract()
            item['bookName']=response.meta['bookName']
            item['bookCommentStar']=[n.encode('utf-8') for n in star ]
            item['bookCommentTitle']=[n.encode('utf-8') for n in title ] 
            item['bookCommentTime']=[n.encode('utf-8') for n in time ] 
            item['bookCommentContent']=[n.encode('utf-8') for n in content ] 
            yield AmazonBookCommentItem(item)


    
        

