# -*- coding: utf-8 -*-
import logging
import os
import re
import shutil
import sys

# logging.debug(os.name)
# logging.debug(os.environ)
# logging.debug(os.environ.get('PATH'))
# logging.debug(os.path.abspath('.'))

# curron_dir = os.path.abspath('.')
# mkdir = os.path.join(curron_dir, 'test_dir')

# logging.debug(os.path.split(mkdir))
# logging.debug(os.path.splitext(mkdir))

# if id('test_dir') == id(os.path.split(mkdir)):
# 	logging.debug("cunzai")
# else:
# 	os.mkdir(mkdir)
# 	logging.debug("sd")
# os.rmdir(mkdir)

# os.rename('test_123', 'test_dir')


# for x in os.listdir('.'):
# 	if os.path.isdir(x):
# 		logging.debug(x)

# logging.debug('C:\\Windows\\System32')


dir = r'V:/'
# 打开搜索到的所有程序
# for x in os.listdir(dir):
# 	# logging.debug('dir:\t\t', x)
# 	if os.path.isdir(dir):
# 		logging.debug('dir:\t\t\t\t', x)
# 	if os.path.splitext(x)[1]=='.exe':
# 		y = os.path.join(dir, x)
# 		logging.debug(y)


# 循环打开程序
# for z in range(10):
# 	logging.debug(z)
# 	os.startfile('calc')


i = 0;
k = 0;

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(funcName)s:line:%(lineno)d] - %(levelname)s: %(message)s')


def gci(dir):
    global i
    global k

    for x in os.listdir(dir):
        if os.path.isdir(x):
            logging.debug(x)
            k = k + 1
            logging.debug(k, end='')

            y = os.path.join(dir, x)
            logging.debug(':', y)
            logging.debug(os.listdir(y))

        elif os.path.isfile(x):
            y = os.path.join(dir, x)
            # i = i + 1
            # logging.debug(i, end='')
            logging.debug('::' + y)


# logging.debug(dir)
# gci(dir)
# logging.debug(i)

# 遍历目录 找出具体某些类型的文件


class GetDirAllFileInfo(object):
    """docstring for GetDirAllFileInfo"""

    def __init__(self, dir):
        super(GetDirAllFileInfo, self).__init__()
        self.dir = dir

    def win2unixformat(self, path):
        """
        windwos 路径反斜杠转换为linux斜杠
        :param path:
        :return:
        """
        result = path
        result = result.replace('\\', '/')
        return result

    def allfiles(self):
        """
        显示所有文件
        """
        logging.debug("==========os.walk================")
        index = 1
        os.chdir(self.dir)
        L = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                # logging.debug("%s %s" % (os.path.splitext(file)[0], os.path.splitext(file)[1]))
                L.append(os.path.splitext(file)[1])
                # pattern = re.compile(r'(^(\[(.*)]))(.*)')
                # pattern = re.compile(r'(^(阳光(.*)com))(.*)')
                pattern = re.compile(r'((迅雷之家(.*)com))(.*)')
                if pattern.search(file):
                    logging.debug('8\t\t\t\t %s |\t\t\t %s ' % (file, pattern.search(file).groups()[-1].strip(' .')))
                    dstfile = pattern.search(file).groups()[-3].strip(' .')
                    logging.debug('%s' % (file.split(dstfile)[0].strip('.') + file.split(dstfile)[-1]))
                    dstfile = file.split(dstfile)[0].strip('.') + file.split(dstfile)[-1]

                    srcfile = self.win2unixformat(os.path.join(root, file))
                    dstfilepath = self.win2unixformat(os.path.join(root, dstfile))
                    logging.debug("%s %s" % (srcfile, dstfilepath))
                    os.rename(srcfile, dstfilepath)

                index += 1
        return L

    def allfilesfilterrename(self, filters):
        """
        过滤后缀列表重命名
        :param filters: 过滤后缀列表
        """
        logging.debug("==========os.walk================")
        index = 0
        logging.debug(filters)
        os.chdir(self.dir)

        for root, dirs, files in os.walk(dir):
            for file in files:
                suffix = os.path.splitext(file)[1]
                # logging.debug(suffix)
                # if suffix in filters:
                if suffix in filters:
                    # logging.debug(file)
                    index += 1
                    pattern = re.compile(r'(^(\[(.*)]))(.*)')
                    # pattern = re.compile(r'(.*).mp4$')
                    if pattern.search(file):
                        logging.debug(file)
                        logging.debug('9\t\t\t\t %s' % pattern.search(file).groups()[-1].strip(' .'))
                        dstfile = pattern.search(file).groups()[-1].strip(' .')

                        try:
                            srcfile = self.win2unixformat(os.path.join(root, file))
                            dstfilepath = self.win2unixformat(os.path.join(root, dstfile))
                            # dstfilepath = self.win2unixformat(os.path.join(root, file)) + '.mp4'
                            logging.debug("%s %s" % (srcfile, dstfilepath))
                            os.rename(srcfile, dstfilepath)

                        except Exception as e:
                            logging.debug(e)
                else:
                    srcfile = self.win2unixformat(os.path.join(root, file))
                    # logging.debug(srcfile)
                    # shutil.move(srcfile, dstdir)

        logging.debug('total num: %s' % index)

    def filesfiltermove(self, filters, dstdir, index=1):
        """

        :param filters:  过滤后缀列表
        :param dstdir:   目标文件夹
        """
        logging.debug("==========os.walk================")
        logging.debug(filters)
        os.chdir(self.dir)

        if os.path.exists(dstdir):
            pass
        else:
            os.mkdir(dstdir)

        i = 0
        for root, dirs, files in os.walk(dir, topdown=True):
            logging.debug("第", i, "层")
            if index == i:
                break

            for file in files:
                # logging.debug('file list %s %s' % (os.path.splitext(file)[0], os.path.splitext(file)[1]))
                suffix = os.path.splitext(file)[1]

                if suffix in filters:
                    try:
                        srcfile = self.win2unixformat(os.path.join(root, file))
                        logging.debug(srcfile)
                        # shutil.move(srcfile, dstdir)
                    except Exception as e:
                        logging.debug(e)
                    index += 1
            i += 1
        logging.debug('\ntotal num: ', index)

    def filesfilterdel(self, filters):
        """
        过滤指定后缀文件进行删除
        :param filters:
        """
        logging.debug("==========os.walk================")
        index = 0
        logging.debug(filters)
        os.chdir(self.dir)

        for root, dirs, files in os.walk(dir):
            for file in files:
                # logging.debug('file list %s %s' % (os.path.splitext(file)[0], os.path.splitext(file)[1]))
                suffix = os.path.splitext(file)[1]

                if suffix in filters:
                    try:
                        logging.debug(file)
                        srcfile = self.win2unixformat(os.path.join(root, file))
                        os.remove(srcfile)
                    except Exception as e:
                        logging.debug(e)
                    index += 1
        logging.debug('\ntotal num: %s' % index)

    def dirfilesmove2root(self, index):
        """
        移动文件夹中单文件到根目录  删除空目录
        :param index:
        """
        logging.debug("==========os.walk================")
        i = 0
        os.chdir(self.dir)
        for root, dirs, files in os.walk(dir):
            if index == i:
                break

            for sub in dirs:
                # logging.debug('\t\tdir: %s' % os.path.join(root, sub))
                subnum = len(os.listdir(sub))
                if os.path.isdir(sub) and (1 == subnum):
                    # logging.debug(os.listdir(sub), len(os.listdir(sub)))
                    for j in range(subnum):
                        try:
                            # logging.debug('move:', os.path.join(root, sub, os.listdir(sub)[j]))
                            result = self.win2unixformat(os.path.join(root, sub, os.listdir(sub)[j]))
                            logging.debug('move %s' % result)
                            shutil.move(result, self.dir)
                        except Exception as e:
                            logging.debug(e)
                elif 0 == subnum:
                    try:
                        result = self.win2unixformat(os.path.join(root, sub))
                        logging.debug('del', result)
                        os.rmdir(result)
                    except Exception as e:
                        logging.debug(e)
            i += 1

    def alldirs(self, index):
        """
        显示所有目录
        :param index:
        """
        logging.debug("==========os.walk================")
        i = 0
        os.chdir(self.dir)
        for root, dirs, files in os.walk(dir):
            if index == i:
                break
            for sub in dirs:
                logging.debug('\t\tdir:', os.path.join(root, sub))
                if os.path.isdir(sub):
                    logging.debug(len(os.listdir(sub)))
            i += 1

    def allroots(self):
        """
        # 所有目录
        """
        logging.debug("==========os.walk================")
        index = 1
        # logging.debug(filters)
        os.chdir(self.dir)
        for root, dirs, files in os.walk(dir):
            # logging.debug("第",index,"层\t\t")
            logging.debug(root, len(os.listdir(root)))

            index += 1


if __name__ == "__main__":
    video = ['.mp4', '.avi', '.flv', '.mpg', '.mkv', '.wmv', '.m2ts', '.webm', '.asf', '.m4v', '.rmvb', '.vob',
             '.ogv', '.gif']

    exe = ['.exe', '.msi']

    delfile = ['.torrent', '.nfo', '.jpg', '.png']

    picture = ['.jpg', '.png', '.ebp', '.mp', '.cx', '.if', '.if', '.peg', '.ga', '.xif', '.px', '.vg', '.sd', '.dr',
               '.cd', '.xf', '.fo', '.ps', '.i', '.ng', '.dri', '.aw', '.mf', '.lic', '.mf', '.co', '.vif', '.pn']

    compression = ['.0', '.000', '.001', '.7z', '.ace', '.ain', '.alz', '.apz', '.ar', '.arc', '.ari', '.arj', '.axx',
                   '.bh', '.bhx', '.boo', '.bz', '.bza', '.bz2', '.c00', '.c01', '.c02', '.cab', '.car', '.cbr', '.cbz',
                   '.cp9', '.cpgz', '.cpt', '.dar', '.dd', '.dgc', '.efw', '.f', '.gca', '.gz', '.ha', '.hbc', '.hbc2',
                   '.hbe', '.hki', '.hki1', '.hki2', '.hki3', '.hpk', '.hyp', '.ice', '.imp', '.ipk', '.ish', '.jar',
                   '.jgz', '.jic', '.kgb', 'kz', '.lbr', '.lha', '.lnx', '.lqr', '.lz4', '.lzh', '.lzm', '.lzma',
                   '.lzo', '.lzx', '.md', '.mint', '.mou', '.mpkg', '.mzp', '.nz', '.p7m', '.package', '.pae', '.pak',
                   '.paq6', '.paq7', '.paq8', '.par', '.par2', '.pbi', '.pcv', '.pea', '.pf', '.pim', '.pit', '.piz',
                   '.puz', '.pwa', '.qda', '.r00', '.r01', '.r02', '.r03', '.rar', '.rk', '.rnc', '.rpm', '.rte', '.rz',
                   '.rzs', '.s00', '.s01', '.s02', '.s7z', '.sar', '.sdn', '.sea', '.sfs', '.sfx', '.sh', '.shar',
                   '.shk', '.shr', '.sit', '.sitx', '.spt', '.sqx', '.sqz', '.tar', '.taz', '.tbz', '.tbz2', '.tgz',
                   '.tlz', '.tlz4', '.txz', '.uc2', '.uha', '.uue', '.wot', '.xef', '.xx', '.xxe', 'xz', '.y', '.yz',
                   '.yz1', '.z', '.zap', '.zip', '.zipx', '.zix', '.zoo', '.zz', 'exe']

    music = ['.mp3', '.ogg', '.wav', '.aac', '.flac', '.mov']
    logging.debug('start run ....')

    dirs = [r'N:/', r'V:/']
    # dir = r'C:/Users/zs-mobile/Pictures'
    # dir = r'E:/相册'

    for dir in dirs:
        F = GetDirAllFileInfo(dir)
        F.filesfilterdel(delfile)
        F.dirfilesmove2root(1)
        F.allfilesfilterrename(video)
        # F.filesfiltermove(music, r'V:/MUSIC')
        # F.filesfiltermove(exe, r'V:/EXE')
        # F.filesfiltermove(video, r'V:/EXE')
        # F.allroots()
        L = F.allfiles()
        logging.debug(list(set(L)))
