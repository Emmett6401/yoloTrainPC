from glob import glob
import yaml

train_img_list = glob('./pothole/train/images/*.jpg')
test_img_list = glob('./pothole/test/images/*.jpg')
valid_img_list = glob('./pothole/valid/images/*.jpg')
print(len(train_img_list), len(test_img_list), len(valid_img_list))

with open('./pothole/train.txt','w') as f:
    f.write('\n'.join(train_img_list) + '\n')
with open('./pothole/test.txt','w') as f:
    f.write('\n'.join(test_img_list) + '\n')
with open('./pothole/val.txt','w') as f:
    f.write('\n'.join(valid_img_list) + '\n')