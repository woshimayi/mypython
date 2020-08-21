import logging

from bs4 import BeautifulSoup
import requests
import re
import os
import time
import sys

base_url = 'https://www.dgtle.com/'
url = 'https://m.dgtle.com/ins-detail/1644813'

logging.basicConfig(
    level=logging.ERROR,
    format='[%(funcName)s:%(lineno)d] - %(levelname)s: %(message)s')

class BeautifulPicture:
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            'authorization': ""}
    def __del__(self):
        logging.debug("del class")

    def mk_dir(self, path):
        self.path = path.strip()
        self.is_exit = os.path.exists(path)
        if not self.is_exit:
            logging.debug("创建 %s 文件夹" % path)
            os.makedirs(path)
            logging.debug('创建成功')
        else:
            logging.debug('文件夹已经存在 %s' % path)
        os.chdir(path)

    def save_img(self, url, name):
        img = requests.get(url)
        logging.debug('len %s' % len(img.content))
        if len(img.content) > 50000:
            f = open(name, 'wb')
            f.write(img.content)
            logging.error('%s 保存成功' % name)
            f.close()

    def get_pic(self, url):
        r = requests.get(url, headers=self.headers, stream=True, timeout=10)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "lxml")
        soup.prettify()
        logging.debug('%s' % soup)
        i = 0
        for jpg_url in soup.find_all('img'):
            i += 1
            # logging.debug(jpg_url['src'])
            time.sleep(0.5)
            if 'http' in jpg_url['src']:
                logging.error(str(time.strftime("%Y%m%d%H%M%S",
                                        time.localtime())) + str(i) + '.jpg')
                self.save_img(
                    jpg_url['src'], str(
                        time.strftime(
                            "%Y%m%d%H%M%S", time.localtime())) + str(i) + '.jpg')
        os.chdir('../')

    def get_next_url(self):

        for jpg_url in soup.find_all('a'):
            if 'http' in jpg_url['href']:
                logging.debug(jpg_url['href'])
                # logging.debug('成功')
            else:
                logging.debug(base_url + jpg_url['href'])


if __name__ == '__main__':
    # # if len(sys.argv) < 3:
    # #     logging.debug("argc less three")
    be = BeautifulPicture()
    path = r'./get_pic' + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    be.mk_dir(path)
    url = r'https://www.dgtle.com/inst-1646420-1.html'
    # index = url.split('/')[-1]
    # url = base_url+''+'inst-'+index+'-1.html'
    logging.debug(url)
    be.get_pic(url)
