# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReshenieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    

    #img
    images = scrapy.Field()
    image_urls= scrapy.Field()
class SpecsItem(scrapy.Item):
    specs = scrapy.Field()

