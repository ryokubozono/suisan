import json
import glob
import os
import cv2

yolo_dir_name = 'images/train'
image_dir_name = 'images/train'
save_dir_name = 'draw_bbox_yolo'

train_dir = 'images/train'
val_dir = 'images/test'

yolo_files = glob.glob(yolo_dir_name + '/*.txt')
yolo_files.sort()

for yolo_file in yolo_files:
    file_name = os.path.splitext(os.path.basename(yolo_file))[0]
    image_file_name = os.path.join(image_dir_name, file_name + '.jpg')
    image_save_name = os.path.join(save_dir_name, file_name + '.jpg')
    yolo_file_name = os.path.join(yolo_dir_name, file_name + '.txt')
    yolo_open = open(yolo_file_name, 'r')
    yolo_load = yolo_open.readlines()

    img = cv2.imread(image_file_name)
    img_w = img.shape[1]
    img_h = img.shape[0]

    for bbox in yolo_load:
        bbox_raw = bbox.split()
        bbox_value = bbox_raw[1].split(",")
        bbox_value = [float(s) for s in bbox_value]
        v = [0, 0, 0, 0]
        v[0] = round((bbox_value[0] - bbox_value[2] / 2) * img_w)
        v[1] = round((bbox_value[1] - bbox_value[3] / 2) * img_h)
        v[2] = round((bbox_value[0] + bbox_value[2] / 2) * img_w)
        v[3] = round((bbox_value[1] + bbox_value[3] / 2) * img_h)
        print(v)
        print(bbox_value)
        # bbox = [float(s) for s in bbox]
        if bbox_raw[0] == "0":
            img = cv2.rectangle(img, (v[0], v[1]), (v[2], v[3]), (255, 0, 0))
                                    
        elif bbox_raw[0] == "1":
            img = cv2.rectangle(img, (v[0], v[1]), (v[2], v[3]), (0, 255, 0))

        else:
            print("ignored key")

        cv2.imwrite(image_save_name, img)
        