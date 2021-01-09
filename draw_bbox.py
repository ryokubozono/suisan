import json
import glob
import os
import cv2

json_dir_name = 'train_annotations'
image_dir_name = 'train_images'
save_dir_name = 'draw_bbox'

train_dir = 'images/train'
val_dir = 'images/test'

json_files = glob.glob(json_dir_name + '/*')
json_files.sort()

for json_file in json_files:
    file_name = os.path.splitext(os.path.basename(json_file))[0]
    image_file_name = os.path.join(image_dir_name, file_name + '.jpg')
    image_save_name = os.path.join(save_dir_name, file_name + '.jpg')
    json_file_name = os.path.join(json_dir_name, file_name + '.json')
    json_open = open(json_file_name, 'r')
    json_load = json.load(json_open)
    flag = False
    for json_load_key in json_load['labels']:
        if json_load_key in ('Jumper School', 'Breezer School'):
            flag = True
            break

    if flag:
        img = cv2.imread(image_file_name)
        img_w = img.shape[1]
        img_h = img.shape[0]

        for json_load_key in json_load['labels']:
            if json_load_key == "Jumper School":
                jumper = json_load['labels']['Jumper School']
                for v in jumper:
                    print(v)
                    img = cv2.rectangle(img, (v[0], v[1]), (v[2], v[3]), (255, 0, 0))
                                        
            elif json_load_key == "Breezer School":
                breezer = json_load['labels']['Breezer School']
                for v in breezer:
                    print(v)
                    img = cv2.rectangle(img, (v[0], v[1]), (v[2], v[3]), (0, 255, 0))

            else:
                print("ignored key:", json_load_key)

            cv2.imwrite(image_save_name, img)
        