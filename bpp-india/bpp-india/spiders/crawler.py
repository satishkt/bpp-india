__author__ = 'mandeepak'

import scrapy
from bs4 import BeautifulSoup
from scrapy import Selector
import time
from items import PriceupItem

class PriceSpider(scrapy.Spider):
    name = "pricedekho"
    allowed_domains = ["pricedekho.com"]
    crawledURL=[]
    detailedCrawled=[]
    brand=""
    category=""
    baseURL=""

    def __init__(self, category=None,brand=None, *args, **kwargs):
        super(PriceSpider, self).__init__(*args, **kwargs)
        self.brand=brand.lower()
        self.category=category.lower()
        self.baseURL='http://www.%s.com/%s/' %(self.name,self.category)
        print(self.baseURL)
        categoryURL=self.baseURL+'%s+%s-price-list.html' %(self.brand,self.category)
        print(categoryURL)
        self.start_urls = [categoryURL]
        self.crawledURL.append('/%s-price-list.html'%(self.category))

    def parse(self, response):
        #baseURL='http://www.%s.com/%s/' %(self.name,self.product)
        print("Base URL:"+self.baseURL)
        for url in response.xpath('//li[@class="page"]/a/@href').extract():
            if url.split("/")[2] not in self.crawledURL:
                yield scrapy.Request(self.baseURL+url.split("/")[2], callback=self.search)
                self.crawledURL.append(url)

    def search(self, response):
        for url in response.xpath('//li[@class="list_view"]//a/@href').extract():
            if url not in self.detailedCrawled:
                 yield scrapy.Request(url, callback=self.detail)
                 self.crawledURL.append(url)

    def detail(self, response):
        print("URL for detail page is "+response.url)
        productTitle=response.url.split('/')[-1].split(".")[0]
        soup = BeautifulSoup(response.body)
        prices=soup.find_all("li", attrs={"class": "activelist"})
        priceList=[]
        for price in prices:
            markup=str(price)
            price_tag=str(BeautifulSoup(markup).find("span", attrs={"class": "price"}).contents).split(" ")[2].strip()
            # print("Price:"+price_tag)
            priceList.append(price_tag)

        titles=soup.find_all("div", attrs={"class": "storeimage"})
        sellerList=[]
        for title in titles:
            markup=str(title)
            seller=str(BeautifulSoup(markup).find("img")).split("=")[1].split(" ")[-2].split('"')[0]
            # print("Title:"+title)
            sellerList.append(seller)
        # myfile=open(self.category+".csv", "a")

        for price,seller in zip(priceList,sellerList):
            #myfile.write(productTitle+","+seller+","+'"'+price+'"'+"\n")
            item = PriceupItem()
            # item['link']=response.url
            item['date']=time.strftime("%d/%m/%Y")
            item['category']=self.category
            item['description']=productTitle
            item['vendor']=seller
            item['price']=price.replace(",","")
            yield item


        # date = Field()
        # product = Field()
        # category = Field()
        # description = Field()
        # vendor = Field()
        # price = Field()



        # myfile.close()


if __name__ == '__main__':
	obj=PriceSpider()
