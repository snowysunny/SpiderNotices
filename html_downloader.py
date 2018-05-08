# coding: utf-8

from urllib import request
import socket
import json
# http://data.eastmoney.com/notices/getdata.ashx?StockCode=&FirstNodeType=0&CodeType=1&PageIndex=9&PageSize=50&jsObj=tTVWnYKP&SecNodeType=0&Time=2018-05-03

class HtmlDownloader(object):


    def download(self, url):
        socket.setdefaulttimeout(200)
        if url is None:
            return None

        headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        # }

        req = request.Request(url, headers=headers)
        response = request.urlopen(req)

        # headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
        # data1 = request.Request(url, headers=headers)
        # response = request.urlopen(data1)
        # response = request.urlopen(url)

        if response.getcode() != 200:
            return None
        try:
            html_data = response.read().decode('GB18030')  # .decode('gbk')
            return html_data.encode('utf-8')
        except request.URLError as e:
            print("What")
            if hasattr(e, 'code'):
                print(e.code())
            if hasattr(e, 'reason'):
                print(e.reason())


if __name__ == "__main__":
    # url = 'http://data.eastmoney.com/notices/getdata.ashx?StockCode=&FirstNodeType=0&CodeType=1&PageIndex=1&PageSize=50&SecNodeType=0&Time=&rt=50844815'
    url = "http://data.eastmoney.com/notices/getdata.ashx?StockCode=&FirstNodeType=0&CodeType=1&PageIndex=1&PageSize=50&SecNodeType=0&Time=2018-05-03"
    res = HtmlDownloader().download(url)

    print(res)
    res = res[6:][:-1]
    print(res)
    res_dict = json.loads(res)
    print(res_dict)
    print(res_dict['data'])
    if not len(res_dict['data']):
        print("NULL")
    else:
        for i in range(10):
            first_data = res_dict['data'][i]
            print("date: ", first_data['NOTICEDATE'][:10])
            print("code: ", first_data['CDSY_SECUCODES'][0]['SECURITYCODE'])
            print("name: ", first_data['CDSY_SECUCODES'][0]['SECURITYFULLNAME'])
            print('title: ', first_data['NOTICETITLE'])
            print("type: ", first_data['ANN_RELCOLUMNS'][0]['COLUMNNAME'])
            print('url: ', first_data['Url'])

