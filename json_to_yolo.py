import json
import os
import jsonpath
import cv2

path_img = r'/home/ling/BigWrok/final/imgs/'
path_json = r'/home/ling/BigWrok/final/outlabel/'
path_out = r'/home/ling/BigWrok/final/label_txt/'
filelist_json = os.listdir(path_json)
filelist_json.sort()
for file in filelist_json:
    filename = os.path.splitext(file)[0]
    frame=cv2.imread(os.path.join(path_img,str(filename)+'.jpg'))
    # cv2.imshow('dd',frame)
    # cv2.waitKey(0)
    size=frame.shape
    w=size[1]
    h=size[0]
    obj = json.load(open(os.path.join(path_json, file), 'r', encoding='utf-8'))
    classname = jsonpath.jsonpath(obj, '$..label')
    points = jsonpath.jsonpath(obj, '$..points')
    #print(classname)
    #print(points)
    for i in range(0,len(points)):
        for j in range(0,4):
            points[i][j][0]=round(float(points[i][j][0])/w,6)
            points[i][j][1] = round(float(points[i][j][1]) / h, 6)
    data = []
    fp = open(os.path.join(path_out,str(filename)+'.txt'), 'w')
    for i in range(0, len(classname)):
        data.append([classname[i], points[i][0], points[i][1], points[i][2], points[i][3]])
        fp.write(data[i][0])
        for j in range(0, 4):
            fp.write(' ' + str(points[i][j][0]))
            fp.write(' ' + str(points[i][j][1]))
        fp.write('\n')
    fp.close()
# 拉出图片
# for file in filelist_json:
#     filename = os.path.splitext(file)[0]
#     fin=open(os.path.join('/home/ling/BigWrok/final/imgs/', str(filename) + '.jpg'), 'rb')
#     fout = open(os.path.join('/home/ling/BigWrok/Output/images/', str(filename) + '.jpg'), 'wb')
#     content=fin.read()
#     fout.write(content)
#     fin.close()
#     fout.close()