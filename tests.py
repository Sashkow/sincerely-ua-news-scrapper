
import json
import unittest
# import newspaper
import papers_please
from main import Site
from main import recall_site
from datetime import date

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
    # def test_getlinks(self):
    #     site = Site('test_inputs/input1')
    #     site.getlinks()




    def test_articles(self):
        site = recall_site()
        site.getarticles()




    # def test_get_articles_urls(self):
    #     site = Site('test_inputs/input1')
    #     urls = site.get_articles_urls('https://www.segodnya.ua/allnews/archive/02-11-2017/p1.html')
    #     print(urls)


    # def test_continue(self):
    #     site = recall_site()
    #     site.getlinks()
    #     print(site.start_date)
    #


    # def test_get_article(self):
    #     site = recall_site()
    #     site.getarticle("https://www.segodnya.ua/lifestyle/psychology/v-avstralii-kenguru-pereprygnul-cherez-velosipedista-v-dvizhenii-793135.html")

    # def test_get_article(self):
    #     site = recall_site()
    #     site.getarticle(
    #             "https://www.segodnya.ua/opinion/faradgalahcolumn/perenos-posolstva-ukrainy-v-ierusalim-lishit-ee-partnerov-s-yuga-793803.html"
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















if __name__ == '__main__':
    unittest.main()
