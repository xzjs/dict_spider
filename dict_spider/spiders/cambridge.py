import scrapy

from dict_spider.items import DictSpiderItem


class Cambridge(scrapy.Spider):
    name = 'cambridge'
    url_base = 'https://dictionary.cambridge.org/dictionary/english/'
    start_urls = []

    with open("dict.txt", 'r') as f:
        param = []
        for line in f.readlines():
            index = line.find("/")
            if index > 0:
                word = line[:index].strip()
                start_urls.append(url_base + word)

    def parse(self, response):
        item = DictSpiderItem()
        item['word'] = response.url.split("/")[-1]
        soudmark = []
        for sel in response.css(".pron"):
            ss = sel.xpath('.//text()').extract()
            result = ''
            for s in ss:
                s = s.encode('utf-8')
                result = result + s.replace('.', '')
            soudmark.append(result)
        item['uk']=soudmark[0]
        item['us']=soudmark[1]
        yield item
