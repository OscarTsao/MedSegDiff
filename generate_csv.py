import os
import pandas as pd

img_dir  = './data/ISIC/ISBI2016_ISIC_Part1_Training_Data'
mask_dir = './data/ISIC/ISBI2016_ISIC_Part1_Training_GroundTruth'

imgs  = sorted([f for f in os.listdir(img_dir)  if f.endswith('.jpg')])
# 直接對應成有空格＋大寫的檔名
masks = [f.replace('.jpg', ' Segmentation.png') for f in imgs]

df = pd.DataFrame({
    'image': imgs,
    'mask' : masks
})
df.to_csv('./data/ISIC/ISBI2016_ISIC_Part1_Training_GroundTruth.csv', index=False)
print('✅ CSV 建立完成，共', len(df), '筆')
