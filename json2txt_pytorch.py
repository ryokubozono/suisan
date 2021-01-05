import json
import glob
import os
import random

f1 = open('train.txt', 'w', encoding='utf-8')
f2 = open('val.txt', 'w', encoding='utf-8')

json_dir_name = 'train_annotations'
image_dir_name = 'train_images'

json_files = glob.glob(json_dir_name + '/*')
json_files.sort()

for json_file in json_files:
    if random.random() > 0.3:
        f = f1
    else:
        f = f2

    file_name = os.path.splitext(os.path.basename(json_file))[0]
    image_file_name = os.path.join(image_dir_name, file_name + '.jpg')
    json_file_name = os.path.join(json_dir_name, file_name + '.json')
    print(image_file_name)

    json_open = open(json_file_name, 'r')
    json_load = json.load(json_open)

    flag = False
    for json_load_key in json_load['labels']:
        print(json_load_key)
        if json_load_key in ('Jumper School', 'Breezer School'):
            f.write(image_file_name + ' ')
            flag = True
            break

    for json_load_key in json_load['labels']:
        print(json_load_key)
        if json_load_key == "Jumper School":
            jumper = json_load['labels']['Jumper School']
            for v in jumper:
                print(v)
                f.write(",".join(map(str, v)))
                f.write(',0 ')
        elif json_load_key == "Breezer School":
            breezer = json_load['labels']['Breezer School']
            for v in breezer:
                print(v)
                f.write(",".join(map(str, v)))
                f.write(',1 ')
        else:
            print("ignored key:", json_load_key)

    if flag:
        f.write('\n')
