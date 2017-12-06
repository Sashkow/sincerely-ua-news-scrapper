# get 

from pyquery import PyQuery as pq
from lxml import etree

from dateutil.rrule import rrule, DAILY

from datetime import date
import time


f = open('out.tsv','w')
f2 = open('all.tsv','w')



# print(dir(lst[0]))
    # print("-".join([str(item.day)   ,str(item.month), str(item.year)]))


# print("here")





def print_page(h3s):
    for h3 in h3s:
        # h3 = q('h3')[1]
        href_elem = h3.getparent().getparent().getparent().getchildren()[0]
        if 'href' in href_elem.attrib:
            full_href = "".join(['https://www.segodnya.ua', href_elem.attrib['href']])
        else:
            print ("improper h3:", h3.text)
            continue
        date = h3.getnext()
        if date:
            date = date.getchildren()[0].text
        else:
            print("no date for h3:", h3.text)
        keywords = ['Ляшк', 'Мосийчук', 'Лозово', 'Радикальная партия', 'радикалы']
        f2.write('\t'.join([h3.text, full_href, date])+'\n')
        if any(word in h3.text for word in keywords):
            print('\t'.join([h3.text, full_href, date]))
            f.write('\t'.join([h3.text, full_href, date])+'\n')

def print_day(day="02-11-2017"):
    i = 1
    while(True):
        q = pq("https://www.segodnya.ua/allnews/archive/"+day+"/p"+str(i)+".html")
        # time.sleep(1)
        h3s = q('h3')
        print(len(h3s))
        if len(h3s)<2:
            break
        print("page:", i)
        print_page(h3s)
        i+=1


dates = [month_datetime.strftime("%d-%m-%Y") for month_datetime in rrule(DAILY, dtstart=date(2017,2,1), until=date(2017,9,1))]

for date in dates:
    print(date)
    print_day(str(date))







# print(h3.text, href.attrib['href'])
# # print(etree.tounicode(parentparent, pretty_print=True))
# # print(q('h3').parent().parent())
# # elements = q('h3')[1].getparent().getparent().getchildren()
# for element in parentparent:
#   print("Element:")
#   print(etree.tounicode(element, pretty_print=True))
#   # print(type(element))
    # print(element.tag, element.text)
