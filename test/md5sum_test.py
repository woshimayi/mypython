
import hashlib
import os

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def GetFileSha256(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.sha256()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


# filepath = raw_input(r'')

# 输出文件的md5值以及记录运行时间
print(GetFileMd5(r'EPON_MTK7G_0003_JINQIANMAO.HAINAN_EN604_CW_V2.2.1_R1B01D2ad1a4d8_934adc10.squashfs.upf'))
print(GetFileSha256(r'EPON_MTK7G_0003_JINQIANMAO.HAINAN_EN604_CW_V2.2.1_R1B01D2ad1a4d8_934adc10.squashfs.upf'))

# hash = hashlib.sha256()
# hash.update('admin'.encode('utf-8'))
# print(hash.hexdigest())



