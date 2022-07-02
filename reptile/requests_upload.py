import os
import sys

import requests
from requests_toolbelt.multipart import encoder

getUpgrade = 'http://192.168.1.1/getUpgradeStatus'


def upload_file(url, filepath):
    print('uploading ...')
    files = {'file': open(filepath, 'rb')}
    requests.post(url, files=files)
    r = requests.get(getUpgrade)
    print(r.text)


def my_callback(monitor):
    # Your callback function
    pass

def upload_progress(url, file):
    try:
        file_stat = os.stat(file)
        print(f"file size :{file_stat.st_size}")
        e = encoder.MultipartEncoder(
            fields={'fieldKey': ('filename', open(file, 'rb'), 'text/plain')}
        )

        m = encoder.MultipartEncoderMonitor(e, my_callback)
        r = requests.post(url, data=m, headers={'Content-Type': m.content_type}, timeout=200)
        print(r.text)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    if 1 == len(sys.argv):
        print('input filepath')
    else:
        filepath = sys.argv[1]

    # upload_file(r'http://192.168.1.1/upgradeImage',  r'Z:\tmp_B560\trunk\images\bcm968782GWV_nand_fs_image_128_puresqubi_V2946.w')

    for i in range(5):
        print("i=", i)
        upload_progress(r'http://192.168.1.1/upgradeImage',
                        r'Z:\tmp_B560\trunk\images\bcm968782GWV_nand_fs_image_128_puresqubi_V2946.w')
