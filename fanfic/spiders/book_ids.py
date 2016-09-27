

from scrapy import Spider, Request


class BookIdsSpider(Spider):

    name = 'book_ids'

    start_urls = [
        'https://www.fanfiction.net/book/Harry-Potter/?r=10&len=60',
    ]

    def parse(self, response):

        """
        Collect book ids, continue to the next page.
        """

        for href in response.xpath('//a[@class="stitle"]/@href').extract():

            book_id = href.split('/')[2]

            # TODO: Yield BookId item.
            print(book_id)

        next_href = (
            response
            .xpath('//a[text()="Next »"]/@href')
            .extract_first()
        )

        next_url = response.urljoin(next_href)

        yield Request(next_url, callback=self.parse)
