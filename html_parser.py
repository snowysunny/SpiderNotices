# coding: utf-8

from SpiderNotices import html_downloader
from bs4 import BeautifulSoup as bs
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')


class HtmlParser(object):
    def parse(self, html_cont):
        if html_cont is None:
            return
        soup = bs(html_cont, 'html.parser', from_encoding="utf-8")
        try:
            # <div class="detail-body" style="padding: 20px 50px;">
            return soup.find('div', class_='detail-body').find('div').get_text()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    url = "http://data.eastmoney.com/notices/detail/AER/AN201805031136865330,QWVyQ2FwK0hvbGRpbmdzK05W.html"
    html_data = html_downloader.HtmlDownloader().download(url)

    res = HtmlParser().parse(html_data)
    print(res)
    print(type(res))

    # soup = bs(html_data, 'html.parser')
    # detail_body = soup.find('div', class_='detail-body').find('div').get_text()
    # print(detail_body)
