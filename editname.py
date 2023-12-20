import os


def cmp(element):
    num = os.path.splitext(element)[0]
    num = int(num)
    return num


path = r'/home/ling/yolov5/My_data/images-face/train/out/'
outpath = r'/home/ling/yolov5/My_data/images-face/train/output/labels/'
filelist = os.listdir(path)
filelist.sort(key=cmp)
count = 1308
for file in filelist:
    Olddir = os.path.join(path, file)
    fp = open(Olddir, 'rb')
    content = fp.read()
    fp.close()
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    rename = str(count).zfill(5)
    Newdir = os.path.join(path, str(count).zfill(5) + filetype)  # zfill(6):表示命名为6位数
    f = open(os.path.join(outpath, str(count).zfill(5) + filetype), 'wb')
    f.write(content)
    f.close()
    count += 1
