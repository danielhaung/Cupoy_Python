import scrapy


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.html']

    
    #當你對一個url進行請求後，你需要對返回的response進行操作，而parse這個function就是這隻爬蟲默認進行處理response的function，
    #若你沒有特別指定處理response的function，則由parse這個function進行處理
    def parse(self, response):
        title = response.xpath('//title').get()
        content = response.xpath('//p').get()
        print("---------------------------------------------------------------")
        print(title)
        print(content)
        print("---------------------------------------------------------------")
