import json
import glob
import os
import random
import cv2
import shutil

json_dir_name = 'train_annotations'
image_dir_name = 'train_images'

train_dir = 'images/train'
val_dir = 'images/test'

json_files = glob.glob(json_dir_name + '/*')
json_files.sort()

for json_file in json_files:
    file_name = os.path.splitext(os.path.basename(json_file))[0]
    image_file_name = os.path.join(image_dir_name, file_name + '.jpg')
    json_file_name = os.path.join(json_dir_name, file_name + '.json')
    json_open = open(json_file_name, 'r')
    json_load = json.load(json_open)
    flag = False
    for json_load_key in json_load['labels']:
        if json_load_key in ('Jumper School', 'Breezer School'):
            flag = True
            break

    if flag:
        if random.random() > 0.3:
            mode = 'train'
            f = open(os.path.join(train_dir, file_name + '.txt'), 'w', encoding='utf-8')
            shutil.copyfile(image_file_name, os.path.join(train_dir, file_name + '.jpg'))
        else:
            mode = 'test'
            f = open(os.path.join(val_dir, file_name + '.txt'), 'w', encoding='utf-8')
            shutil.copyfile(image_file_name, os.path.join(val_dir, file_name + '.jpg'))

        img = cv2.imread(image_file_name)
        img_w = img.shape[1]
        img_h = img.shape[0]

        for json_load_key in json_load['labels']:
            if json_load_key == "Jumper School":
                jumper = json_load['labels']['Jumper School']
                for v in jumper:
                    
                    v_yolo = [0, 0, 0, 0]
                    v_yolo[0] = round((v[2] + v[0])/2/img_w, 6)
                    v_yolo[1] = round((v[3] + v[1])/2/img_h, 6)
                    v_yolo[2] = round((v[2] - v[0])/img_w, 6)
                    v_yolo[3] = round((v[3] - v[1])/img_h, 6)

                    f.write('0 ')
                    f.write(" ".join(map(str, v_yolo)))
                    f.write('\n')
            elif json_load_key == "Breezer School":
                breezer = json_load['labels']['Breezer School']
                for v in breezer:

                    v_yolo = [0, 0, 0, 0]
                    v_yolo[0] = round((v[2] + v[0])/img_w, 6)
                    v_yolo[1] = round((v[3] + v[1])/img_h, 6)
                    v_yolo[2] = round((v[2] - v[0])/img_w, 6)
                    v_yolo[3] = round((v[3] - v[1])/img_h, 6)

                    f.write('1 ')
                    f.write(" ".join(map(str, v_yolo)))
                    f.write('\n')
            else:
                print("ignored key:", json_load_key)

        f.close()
