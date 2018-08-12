
import json
import unittest
# import newspaper
import papers_please
from main import Site
from main import recall_site
from datetime import date

from elasticsearch import Elasticsearch
# es = Elasticsearch(['https://elastic:oESru8NqPaZePrEZNQyb@localhost:443'])

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


# from wordforms import generate_wordforms, generate_phraseforms



# class TestPapersPlease(unittest.TestCase):
#     def test_inherits_newspaper_source(self):
#         url = 'https://www.segodnya.ua/'
#         p = papers_please.PapersPlease(url, language='ru', memoize_articles=False)
#         self.assertEqual(p.url, url)
#         self.assertTrue(isinstance(p,newspaper.Source))
#
#     def test_segodnya_alternative_urls(self):
#         url = 'https://www.segodnya.ua/'
#         p = papers_please.PapersPlease(url, memorize_articles=False)
#         p.add_segodnya_urls()
#         p.build()
#         p.print_summary()

class TestSite(unittest.TestCase):
    # # def test_getlinks(self):
    # #     site = Site('test_inputs/segodnya')
    # #     site.getlinks()
    #
    # # def test_getlinks(self):
    # #     site = Site('test_inputs/tsn')
    # #     site.getlinks()
    #
    # # def test_getlinks(self):
    # #     site = Site('test_inputs/kor')
    # #     site.getlinks()
    # #
    # def test_getlinks(self):
    #     site = Site('test_inputs/112')
    #     site.getlinks()

    # def test_getlinks(self):
    #     site = Site('test_inputs/censor_net')
    #     site.getlinks()

    # def test_getlinks(self):
    #     site = Site('test_inputs/strana')
    #     site.getlinks()
    #
    #


    def test_articles(self):
        site = recall_site()
        site.getarticles(overwrite=False)



    # def test_get_articles_urls(self):
    #     site = Site('test_inputs/input1')
    #     urls = site.get_articles_urls('https://www.segodnya.ua/allnews/archive/02-11-2017/p1.html')
    #     print(urls)


    # def test_continue(self):
    #     site = recall_site()
    #     site.getlinks()
    #     print(site.start_date)
    #

    #

    # def test_get_article(self):
    #     site = recall_site()
    #     site.getarticle("https://112.ua/video/novosti-112-vypusk-ot-1100-01012017-222733.html")



    # def test_get_article(self):
    #     site = recall_site()
    #     article = site.getarticle("https://www.segodnya.ua/opinion/faradgalahcolumn/perenos-posolstva-ukrainy-v-ierusalim-lishit-ee-partnerov-s-yuga-793803.html")
    #     # es.index(index='news', doc_type='article', body=article)
    #     es.search(index="news3", body={"query": {"term": {"title.raw": "Трех инfgостранцев будут судить за похищение и убийство в Одессе"}}})['hits']['total']
    #     es.update(index='test', doc_type='article', body={'doc':article, 'doc_as_upsert': True})
# )
    # def test_get_article(self):
    #     site = recall_site()
    #     site.getarticle("https://www.segodnya.ua/lifestyle/food/postnoe-menyu-na-den-top-5-receptov-1116719.html")

    # def test_to_memory(self):






# class TestWordForms(unittest.TestCase):
#     def test_generate_wordforms(self):
#         word = 'республіканська'
#         generate_wordforms(word)
#
#     def test_generate_phaseforms(self):
#         phrase = 'Блок Геннадія Чекіти "За справедливість"'
#         generate_phraseforms(phrase)

# from elasticsearch import Elasticsearch
# import elasticsearch.helpers
# # es = Elasticsearch(['https://elastic:oESru8NqPaZePrEZNQyb@localhost:443'])
#
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# пes,'news5','news5')



# class TestES(unittest.TestCase):
#     def test_es_search(self):
#         res = es.search(index="news", body={"query": {"term": {"title": "1"}}})
#         res = es.search(index="news", body={"query": {"term": {"title": "1"}}})
#         for item in res["hits"]:
#             print(item,res["hits"][item])
#

























if __name__ == '__main__':
    unittest.main()
