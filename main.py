import json
import os
import ssl
from urllib.request import urlopen
import re

from bs4 import BeautifulSoup


def main():
    get_dir2()


def get_dir1():
    """
    获取markets
    :return:
    """
    # 初始url
    start_url = "https://www.taobao.com"
    # 下載器
    ssl._create_default_https_context = ssl._create_unverified_context
    html = urlopen(start_url).read().decode('utf-8')

    soup = BeautifulSoup(html)
    markets_urls = {}
    for market in soup.find_all("a", {"href": re.compile('https://www.taobao.com/markets/.+')}):
        # 若不存在文件夾 新建
        dir1 = market.text
        path1 = "images/{}".format(dir1)
        if not os.path.isdir(path1):
            os.mkdir(path1)
        markets_urls[dir1] = market.get('href')
    fo = open("markets_urls.txt", "w+")
    fo.writelines(json.dumps(markets_urls))
    fo.close()


def get_dir2():
    # 读取markets.txt
    fo = open("markets_urls.txt", "r")
    try:
        markets_urls = json.loads(fo.readlines()[0])
    except Warning as w:
        print(w)
        markets_urls = {}
    # markets_dict = {market: 0 for market in markets_list}
    markets_lists_urls = {}
    for market_name, market_url in markets_urls.items():
        ssl._create_default_https_context = ssl._create_unverified_context
        html = urlopen(market_url).read().decode('utf-8')
        soup = BeautifulSoup(html)
        one_market = {}
        for market in soup.find_all("a", {"href": re.compile('//s.taobao.com/list.+')}):
            # 若不存在文件夾 新建
            dir2 = market.text.spl
            path2 = "images/{}/{}".format(market_name, dir2)
            if not os.path.isdir(path2):
                os.mkdir(path2)
            one_market[dir2] = market.get('href')
        markets_lists_urls[market_name] = {
            "market_url": market_url,
            "list_url": one_market
        }
    fo = open("markets_lists_urls.txt", "w+")
    fo.writelines(json.dumps(markets_lists_urls))
    fo.close()


if __name__ == '__main__':
    main()
