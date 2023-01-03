#在step1中会造成提取多个类xml文件都没有object这个属性，所以这里采取一种暴力法将不包含我要的类的annotation和image删掉
#后来我觉得这个步骤可以不用操作

import os

Dir = '/home/model_trainging/dataset/coco_DL/annotations/train2014'
ImageDir = '/home/model_trainging/dataset/coco_DL/images/train2014'
cnt = 0
for i, file_name in enumerate(os.listdir(Dir)):
    fsize = os.path.getsize(os.path.join(Dir,file_name))
if fsize == 410:
    print('removing {} of size{}'.format(file_name,fsize))
    os.remove(os.path.join(ImageDir, file_name[:-3]+'jpg'))
    os.remove(os.path.join(Dir, file_name))
    cnt += 1

print('remove {} files'.format(cnt))
