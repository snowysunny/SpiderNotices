#coding: utf-8

from SpiderNotices import html_downloader, html_parser, html_outputer
import time
import json
from datetime import datetime
from datetime import timedelta

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def singlePageCraw(self, url):
        notices_info = []
        html_data = self.downloader.download(url)
        html_data = html_data[6:][:-1]
        print(html_data)
        html_data_json = json.loads(html_data)
        # print(html_data_json)
        if not html_data_json['data']:
            print("no data")
            return 0
        for i in range(len(html_data_json['data'])):
            each_notice_data = html_data_json['data'][i]
            each_notice_info = []
            each_notice_info.append(each_notice_data['CDSY_SECUCODES'][0]['SECURITYCODE'])
            each_notice_info.append(each_notice_data['CDSY_SECUCODES'][0]['SECURITYFULLNAME'])
            each_notice_info.append(each_notice_data['NOTICETITLE'])
            each_notice_info.append(each_notice_data['ANN_RELCOLUMNS'][0]['COLUMNNAME'])
            each_notice_info.append(each_notice_data['NOTICEDATE'][:10])
            each_notice_info.append(each_notice_data['Url'])
            content_url = each_notice_data['Url']
            content_html_data = self.downloader.download(content_url)
            content_data = self.parser.parse(content_html_data)
            each_notice_info.append(content_data)
            notices_info.append(each_notice_info)
            # print("date: ", each_notice_data['NOTICEDATE'][:10])
            # print("code: ", each_notice_data['CDSY_SECUCODES'][0]['SECURITYCODE'])
            # print("name: ", each_notice_data['CDSY_SECUCODES'][0]['SECURITYFULLNAME'])
            # print('title: ', each_notice_data['NOTICETITLE'])
            # print("type: ", each_notice_data['ANN_RELCOLUMNS'][0]['COLUMNNAME'])
            # print('url: ', each_notice_data['Url'])
        print(notices_info)
        for i in range(len(notices_info)):
            db = self.outputer.dbconnect()
            res = self.outputer.insertdb(db, notices_info[i])

        if not res:
            return 2
        return 1
        # print(notices_info)
        # print(len(notices_info))
        # print(len(html_data_json['data']))

    def urlManage(self, pageIndex, codeType=2, setTime="", firstNodeType=0, secNodeType=0, pageSize=50):
        url = "http://data.eastmoney.com/notices/getdata.ashx?StockCode=&FirstNodeType=%s&CodeType=%s&PageIndex=%s&PageSize=%s&SecNodeType=%s&Time=%s"
        obj_url = url %(firstNodeType, codeType, pageIndex, pageSize, secNodeType, setTime)
        return obj_url

    def Crawl_new(self):
        for time_range in range(111, 127):
            date_time = datetime.today() - timedelta(time_range)
            date_time = date_time.strftime('%Y-%m-%d')
            code_type_range = 1
            Start = time.time()
            for page_index_range in range(1, 100):
                try:
                    startTime = time.time()
                    url = self.urlManage(page_index_range, code_type_range, date_time)
                    print(url)
                    res = self.singlePageCraw(url)
                    if res == 0:
                        break
                    endTime = time.time()
                    time.sleep(15)
                    print("one page spendTime: ", endTime - startTime)
                except:
                    print("Error show, coninue")

            print("All Time: ", time.time() - Start)


    def Crawl(self):
        for time_range in range(0, 30):
            date_time = datetime.today() - timedelta(time_range)
            date_time = date_time.strftime('%Y-%m-%d')
            for code_type_range in range(1, 11):
                for page_index_range in range(1, 100):
                    try:
                        startTime = time.time()
                        url = self.urlManage(page_index_range, code_type_range, date_time)
                        print(url)
                        res = self.singlePageCraw(url)
                        if res == 0:
                            break
                        endTime = time.time()
                        time.sleep(15)
                        print("one page spendTime: ", endTime - startTime)
                    except:
                        print("Error show, coninue")

    def Crawl_NoDate(self):
        start = time.time()
        for code_type_range in range(12, 13):
            print('**************************************************** code_type_range:  ', code_type_range)
            for page_index_range in range(1, 140):
                startTime = time.time()
                url = self.urlManage(page_index_range, code_type_range)
                print(url)
                res = self.singlePageCraw(url)
                if res == 0:
                    break
                endTime = time.time()
                time.sleep(15)
                print("one page spendTime: " , endTime - startTime)
        print("Finsh, total spendTime: ", time.time() - start)


    # def Crawl(self):


if __name__ == "__main__":
    print("----------------------------Start----------------------------------------")
    SpiderMain().Crawl_new()
    # url = 'http://data.eastmoney.com/notices/getdata.ashx?StockCode=&FirstNodeType=0&CodeType=2&PageIndex=3&PageSize=50&SecNodeType=0&Time='
    # pageIndex = 80
    # #
    # url = SpiderMain().urlManage(pageIndex)
    # print(url)
    # SpiderMain().singlePageCraw(url)
    # print("Finish")


    # for time_range in range(-1, 365):
    #     time = datetime.today() - timedelta(time_range)
    #     time = time.strftime('%Y-%m-%d')
    # print(time)
    # print(type(time))