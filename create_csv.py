from glob import glob
import os
import pandas as pd

root_dir = "mix1/val/"
# os.chdir(root_dir)

img_path_list = []
label_list = []
possible_img_extension = ['.jpg', '.jpeg', '.JPG', '.bmp', '.png']  # 이미지 확장자들
for (root, dirs, files) in os.walk(root_dir):
    for file_name in files:
        if os.path.splitext(file_name)[1] in possible_img_extension:
            image_path = root_dir + file_name
            label = file_name.split('_')
            label = label[0]
            img_path_list.append(image_path)
            label_list.append(label)

dict = {'image': img_path_list, 'label': label_list}
df = pd.DataFrame(dict)
df.to_csv('validation.csv', encoding='utf-8-sig', index=False, header=True)

