import scrapy


class AosFatosSpider(scrapy.Spider):
    name = 'Aos_fatos'

    start_url = ['https://aosfatos.org/']

    def parse(self, response):
        links = response.xpath(
            '//nav//ul//li/a[re:test(@href, "checamos")]').getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_category
            )

    def parse_category(self, response):
        # import ipdb; ipdb.set_trace()
        news = response.css('.card::attr(href)').getall()
        for new_url in news:
            yield scrapy.Request(
                response.urljoin(new_url),
                callback=self.parse_new
            )
        pages_url = response.css('.pagination a::atr(href)').getall()
        for page in pages_url:
            yield scrapy.Request(
                response.urljoin(page),
                callback=self.parse_category
            )

    def parse_new(self, response):
        title = response.css('article h1::text').get()
        date = ' '.join(response.css('p.publish_date::text').get().split())
        quotes = response.css('article blockquote p')
        for quote in quotes:
            quote_text = quote.css('::text').get()
            status = quotes[1].xpath(
                './parent::blockquote/preceding-sibling::figure//figcaption/text()').get()

            yield{
                'title': title,
                'date': date,
                'quote_text': quote_text,
                'status': status,
                'url': response.url
            }
