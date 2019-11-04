import scrapy
from reshenie.items import ReshenieItem,SpecsItem

class FirstSpider(scrapy.Spider):
    name = "reshenie"
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    

    def start_requests(self):
        urls =[
            'https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012',
            #'https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=1&priceValue=',
            #'https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=2&priceValue=',
            ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        item = ReshenieItem()
        uncleaned_title_list=response.xpath('//div[@class="title"]/a[@class="name"]/text()').extract()
        cleaned_title = [x.replace("\n","") for x in uncleaned_title_list]
        cleaned_title = [x.replace("\t","") for x in cleaned_title]

        item['title']=cleaned_title
        price = response.xpath('//div[@class="price"]/text()').extract()
        price = [x.replace(" лв.","") for x in price]
        price = [x.replace(",",".") for x in price]
        item['price']=price
        link = response.xpath('//div[@class="image"]/a/@href').extract()
        item['image_urls'] = response.xpath('.//div[@class="image"]/a/img/@src').extract()
        for x in link:
            description_url=r"https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/"+x
            yield scrapy.Request(url=description_url,callback=self.get_specs)
        yield item
            
    def get_specs(self,response):
        item = SpecsItem()
        specs =response.xpath('//div[@class="product-classifications"]/table[@class="table"]').extract()
        availability = response.xpath('//div[@class="store-navigation"]/ul/li/text()')
        item['specs']=specs
        item['availability']=availability 
        yield item


