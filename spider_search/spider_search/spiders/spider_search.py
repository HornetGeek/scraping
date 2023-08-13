import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor




class spiderSearch(CrawlSpider):
    
    def __init__(self, filename=None,*a, **kw):
        super(spiderSearch, self).__init__(*a, **kw)
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.readlines()
                
                self.allowed_domains = f.readlines()
    
    name = "links"
    custom_settings = {
        'DEPTH_LIMIT': 2
    }

    global count_word
    count_word = {}

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    
    global li
    global di
    di = {}
    flage = False
    def vlaue(self):
        self.flage = False
        for li in self.start_urls:
            print(str(li).replace('\n','')[:-1])

            di[str(li).replace('\n','')[:-1]] = []

        


    def parse_item(self, response):
        try:
            if not self.flage:
                self.vlaue()
                self.flage = True

            x = response.url.split('/')
            print("url")
            print(x)
            url = '/'.join(x[:3])

            print("parse")

            print(url)
            print(di)
            di[url].append(int(float(response.xpath("count(//*[contains(text(), 'design')])").get())))
            count_word[url] = sum(di[url])

            with open('output2.txt', 'w') as f:
                f.write(str(count_word))
            
            yield {
                "url": response.url,
                "word":response.xpath("count(//*[contains(text(), 'design')])").get()
            }
        except Exception as e:
            print(e)
            with open('error.txt', 'a') as f:
                f.write(str(e))