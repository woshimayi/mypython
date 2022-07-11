import os
import re
import shutil

dir = r'V:/'


def file_operation(root, filepath, filter):
    suffix = os.path.splitext(filepath)[1]
    if suffix in filter:
        print('\t\t\t\tfile', os.path.join(root, filepath))
        L = str(filepath).split(']')
        if suffix == '.torrent':
            print('del torrent', os.path.join(root, filepath), end='')
            os.remove(os.path.join(root, filepath))
            pass
        elif len(L) >= 2:
            # print('rename', end='')
            os.rename(os.path.join(root, filepath), os.path.join(root, L[1].strip('[. ]')))
        elif '阳光电影www.ygdy8.com' in filepath:
            # print('222', filepath, str(filepath).split('com')[1].strip('. '))
            os.rename(os.path.join(root, filepath), os.path.join(root, str(filepath).split('com')[1].strip('. ')))
        elif suffix == '.exe':
            # os.remove(os.path.join(root, filepath), os.path.join(root, "EXE"))
            print('move dir', end='')
            # shutil.move(os.path.join(root, filepath).replace('\\', '/'), str(root + '\\EXE\\').replace('/', '\\') )


def function(dir, filter):
    print("==========os.walk================")
    index = 1
    print(filter)

    for root, dirs, files in os.walk(dir):
        print("第",index,"层")
        index += 1

        for dir in dirs:
            try:
                # print("R:%s W:%s" % (os.access(dir, os.R_OK), os.access(dir, os.W_OK)))
                print('\t\t\t\tdir', os.path.join(root, dir), len(os.listdir(os.path.join(root, dir))))
                subdir = os.path.join(root, dir)
                files = os.listdir(os.path.join(root, dir))

            except Exception as e:
                print(e)

        # '''
        for filepath in files:
            # print("1111", str(filepath).split(']') , os.path.splitext(filepath)[0], os.path.splitext(filepath)[1])
            file_operation(root, filepath, filter)
            # suffix = os.path.splitext(filepath)[1]
            # if suffix in filter:
            #     # print('file', os.path.join(root, filepath))
            #     L = str(filepath).split(']')
            #     if suffix  == '.torrent':
            #         # os.remove(os.path.join(root, filepath))
            #         # print(os.path.join(root, filepath))
            #         pass
            #     elif len(L) >= 2:
            #         # print(L[1].strip('[. ]'))
            #         print(os.path.join(root, filepath))
            #         print(os.path.join(root, L[1].strip('[. ]')))
            #         os.rename(os.path.join(root, filepath), os.path.join(root, L[1].strip('[. ]')))
            #     elif '阳光电影www.ygdy8.com' in filepath:
            #         print('222', filepath, str(filepath).split('com')[1].strip('. '))
            #         os.rename(os.path.join(root, filepath), os.path.join(root, str(filepath).split('com')[1].strip('. ')) )


# '''


if __name__ == "__main__":
    video = ['.mp4', '.avi', '.flv', '.mpg', '.mkv', '.wmv', '.m2ts', '.webm', '.asf', '.mov', '.m4v', '.rm', '.vob', '.ogv', '.gif']
    function(dir, video)
