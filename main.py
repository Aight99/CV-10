import cv2
import os
import re


def merge_channels(input_dir, output_dir):
    imgs = []

    for i, file in enumerate(os.listdir(input_dir)):
        imgs.append(cv2.imread(os.path.join(input_dir, file)))

        if len(imgs) == 3:
            cvs = [cv2.split(img) for img in imgs]
            save_img = [img[i] for i, img in enumerate(cvs)]
            merged = cv2.merge(save_img)
            cv2.imwrite(os.path.join(output_dir, re.sub(r"_r", "", file)), merged)
            imgs = []


if __name__ == '__main__':
    merge_channels("python_split_image_by_ch/data", "python_split_image_by_ch/images")
