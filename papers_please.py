import newspaper

from newspaper import Source

from dateutil.rrule import rrule, DAILY
from datetime import date

class Category(object):
    def __init__(self, url):
        self.url = url
        self.html = None
        self.doc = None


class PapersPlease(Source):
    def add_segodnya_urls(self):

        dates = [month_datetime.strftime("%d-%m-%Y")
                 for month_datetime
                 in rrule(DAILY, dtstart=date(2017,2,1), until=date(2017,9,1))]
        urls = ["https://www.segodnya.ua/allnews/archive/"+str(day)+"/p"+str(i)+".html"
               for day in dates for i in range(20)]
        urls = urls[:10]
        self.categories = [Category(url=url) for url in urls]

    def build(self):
        """Encapsulates download and basic parsing with lxml. May be a
        good idea to split this into download() and parse() methods.
        """
        print("building")
        # self.download()
        # self.parse()
        #
        # # self.set_categories()
        # self.download_categories()  # mthread
        # self.parse_categories()
        #
        # self.set_feeds()
        # self.download_feeds()  # mthread
        # # self.parse_feeds()

        self.download()
        self.parse()
        # self.set_categories()
        self.download_categories()
        self.parse_categories()
        self.set_feeds()
        self.download_feeds()
        self.generate_articles()



# cnn_paper.download_categories()
# print("hrere")
# cnn_paper.parse_categories()
# cnn_paper.set_feeds()
# cnn_paper.download_feeds()
# cnn_paper.generate_articles()
# cnn_paper.print_summary()
# print(len(cnn_paper.articles))
#
# for article in paper24.articles:
	# print(article.url)

# u'http://www.cnn.com/2013/11/27/justice/tucson-arizona-captive-girls/'
# u'http://www.cnn.com/2013/12/11/us/texas-teen-dwi-wreck/index.html'
# ...

# >>> for category in cnn_paper.category_urls():
# >>>     print(category)

# u'http://lifestyle.cnn.com'
# u'http://cnn.com/world'
# u'http://tech.cnn.com'
# ...
# >>> article = cnn_paper.articles[0]
# >>> article.download()

# >>> article.html
# u'<!DOCTYPE HTML><html itemscope itemtype="http://...'
# >>> article.parse()

# >>> article.authors
# [u'Leigh Ann Caldwell', 'John Honway']

# >>> article.text
# u'Washington (CNN) -- Not everyone subscribes to a New Year's resolution...'

# >>> article.top_image
# u'http://someCDN.com/blah/blah/blah/file.png'

# >>> article.movies
# [u'http://youtube.com/path/to/link.com', ...]
# >>> article.nlp()

# >>> article.keywords
# ['New Years', 'resolution', ...]

# >>> article.summary
# u'The study shows that 93% of people ...'
# Newspaper has seamless language extraction and detection. If no language is specified, Newspaper will attempt to auto detect a language.

# >>> from newspaper import Article
# >>> url = 'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml'

# >>> a = Article(url, language='zh') # Chinese

# >>> a.download()
# >>> a.parse()

# >>> print(a.text[:150])
# 香港行政长官梁振英在各方压力下就其大宅的违章建
# 筑（僭建）问题到立法会接受质询，并向香港民众道歉。
# 梁振英在星期二（12月10日）的答问大会开始之际在其
# 演说中道歉，但强调他在违章建筑问题上没有隐瞒的意
# 图和动机。 一些亲北京阵营议员欢迎梁振英道歉，
# 且认为应能获得香港民众接受，但这些议员也质问梁振英有

# >>> print(a.title)
# 港特首梁振英就住宅违建事件道歉
# If you are certain that an entire news source is in one language, go ahead and use the same api :)

# >>> import newspaper
# >>> sina_paper = newspaper.build('http://www.sina.com.cn/', language='zh')

# >>> for category in sina_paper.category_urls():
# >>>     print(category)
# u'http://health.sina.com.cn'
# u'http://eladies.sina.com.cn'
# u'http://english.sina.com'
# ...

# >>> article = sina_paper.articles[0]
# >>> article.download()
# >>> article.parse()

# >>> print(article.text)
# 新浪武汉汽车综合 随着汽车市场的日趋成熟，传统的“集
# 全家之力抱得爱车归”的全额购车模式已然过时，另一种轻
# 松的新兴 车模式――金融购车正逐步成为时下消费者购买
# 爱车最为时尚的消费理 念，他们认为，这种新颖的购车模
# 式既能在短期内
# ...

# >>> print(article.title)