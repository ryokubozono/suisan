import glob
import os

train_dir = 'images/train'
val_dir = 'images/test'

train_list_file_name = '_train.txt'
val_list_file_name = '_test.txt'

f = open(train_list_file_name, 'w')

train_files_list = glob.glob(train_dir + '/*.jpg')
train_files_list.sort()

for train_file in train_files_list:
    print(train_file)
    f.write(train_file)
    f.write('\n')

f.close()

f = open(val_list_file_name, 'w')

val_files_list = glob.glob(val_dir + '/*.jpg')
val_files_list.sort()

for val_file in val_files_list:
    print(val_file)
    f.write(val_file)
    f.write('\n')

f.close()
