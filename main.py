import os
from urllib.request import urlopen
import re

from bs4 import BeautifulSoup


def main():
    # 初始url
    start_url = "https://www.taobao.com/"
    # 下載器
    html = urlopen(start_url).read().decode('utf-8')
    soup = BeautifulSoup(html)
    for market in soup.find_all("a", {"href": re.compile('https://www.taobao.com/markets/.+')}):
        # 若不存在文件夾 新建
        dir1 = market.text
        path1 = "images/{}".format(dir1)
        if not os.path.isdir(path1):
            os.mkdir(path1)




if __name__ == '__main__':
    main()
