'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: xml_to_web.py
@time: 2025/11/11 16:38
@desc: 通过 xml 文件生成html 元素
'''

from bs4 import BeautifulSoup


class GenWeb(object):
    """docstring for GenWeb"""

    def __init__(self):
        super(GenWeb, self).__init__()
        self.fw = open("index.txt", 'w')

    def close(self):
        self.fw.close()

    def gen_val(self, name, zhname):
        self.fw.write('''
                    <div class="row">
						<div class="content_input_title">
							<span>%s</span>
						</div>
						<div class="content_input">
							<input type="text" class="col-3 col-sm-8 paraDisable" id="ipsec%s" hgs_key="%s"><span class="rowComments"></span>
						</div>
					</div>
                      ''' % (zhname, name, name))

    def gen_int(self, name, zhname, min, max):
        self.fw.write('''
                    <div class="row">
						<div class="content_input_title">
							<span>%s</span>
						</div>
						<div class="content_input">
							<input type="text" class="col-3 col-sm-2 paraDisable" id="ipsec%s" hgs_key="%s"><span class="rowComments">有效范围%s-%s</span>
						</div>
					</div>
                      ''' % (zhname, name, name, min, max))

    def gen_bool(self, name, zhname):
        self.fw.write(
            '''
					<div class="row">
						<div class="content_input_title">
							<span>%s</span>
						</div>
						<div class="content_input">
							<input type="checkbox" class="paraDisable" id="ipsec%s" hgs_key="%s">
						</div>
					</div>
            ''' % (zhname, name, name))

    def gen_select(self, name, zhname, sel):
        self.fw.write(
            '''
					<div class="row">
						<div class="content_input_title">
							<span>%s</span>
						</div>
						<div class="content_input">
							<select class="col-6 wanCfgChange paraDisable" id="ipsec%s" hgs_key="%s">
            ''' % (zhname, name, name))

        for i in sel.split(','):
            self.fw.write(
                '''
								<option value="%s">%s</option>
                ''' % (i, i))

        self.fw.write(
            '''
							</select>
						</div>
					</div>
            ''')


if __name__ == '__main__':

    xml_file = r"E:\mypython_new\file_IO\cms-dm-hg-cmcc-tr98-obj-Traffic-web.xml"  # 替换为你的 XML 文件路径

    with open(xml_file, 'r', encoding='utf-8') as fr:
        L = fr.readlines()
        # print(L)
        shortObjectName = ''
        mulNodeFlag = False

        # prmt file begain
        name = ''
        j = 0
        objDict = []
        print(L)
        G = GenWeb()
        for line in L:
            # print("----------", line)
            if 'object' in line:
                soup = BeautifulSoup(line.strip(), "lxml")
                soup.prettify()
            elif 'parameter' in line:
                soup = BeautifulSoup(line.strip(), "lxml")
                soup.prettify()
                for jpg_url in soup.find_all('parameter'):
                    for key, val in jpg_url.attrs.items():
                        print("{}:{}".format(key, val))
                        if key == "webtype":
                            print("======: ", jpg_url['name'])
                            if val == "bool":
                                G.gen_bool(jpg_url['name'], jpg_url['zhname'])
                                pass
                            elif val == "value":
                                G.gen_val(jpg_url['name'], jpg_url['zhname'])
                                pass
                            elif val == "select":
                                G.gen_select(jpg_url['name'], jpg_url['zhname'], jpg_url['selval'])
                                pass
                            elif val == "int":
                                G.gen_int(jpg_url['name'], jpg_url['zhname'], jpg_url['minvalue'], jpg_url['maxvalue'])
                                pass

                print("")

    print('Hello world')
