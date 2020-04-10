# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    def start_requests(self):
        urls_list = []
        for i in range(2,6):
            urls_list.append('http://books.toscrape.com/catalogue/page-' + str(i) + '.html')
        urls = []
        urls.append('http://books.toscrape.com/')
        for i in range (0, len(urls_list)):
            urls.append(urls_list[i])
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//article[@class="product_pod"]/h3/a/text()').extract()
        with open('books_title.txt', 'a+') as f:
            for i in range(0, len(title)):
                f.write(str(i) + ': ' + title[i] + '\n')
        f.close()
        yield {
            'title': title
        }
