from bs4 import BeautifulSoup
import requests
import re
import os
import time
import xlwt
import xlrd
import xlutils.copy


class game:
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            'authorization': ""}
        self.data = xlrd.open_workbook(r'./game-config.xls')
        if self.data:
            print("read success")
            self.workbook = xlutils.copy.copy(self.data)
            self.sheet = self.workbook.get_sheet(0)
        else:
            print('read fail, and create new file')
            self.workbook = xlwt.Workbook(
                encoding='utf-8', style_compression=0)
            self.sheet = self.workbook.add_sheet(
                'game_config', cell_overwrite_ok=True)
            self.workbook.save(r'./game-config.xls')

        table1 = self.data.sheets()[0]
        self.j = table1.nrows # 在之前的行数下面添加

    def get_config(self, url):
        i = 0
        r = requests.get(url, headers=self.headers)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "lxml")
        soup.prettify()

        title = soup.find_all(
            'h2', 'zt_center_con_body_left_yxinfo_title_center')
        # print(title)
        print(title[1].get_text())  # Get game name
        self.sheet.write(self.j, i, title[1].get_text())
        i += 1

        cfg = soup.find_all('div', 'zt_center_con_body_left_yxset_con')
        # print(cfg[1].find_all('p')) # get config information

        for config in cfg[1].find_all('p'):
            print(config.get_text().split('：')[1])
            self.sheet.write(self.j, i, config.get_text().split('：')[1])
            i += 1
        self.workbook.save(r'./game-config.xls')

        self.j += 1

    def get_all_url(self, url):
        r = requests.get(url, headers=self.headers)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "lxml")
        soup.prettify()

        url_all = soup.find_all('a')
        print(url_all)
        for url in url_all:
            if 'http' in url['href']:
                print(url)




if __name__ == "__main__":
    G = game()
    url = 'https://www.ali213.net/zt/nfs19/'
    G.get_config(url)
    # G.get_all_url('https://www.ali213.net/zhuanti/nfs/')

