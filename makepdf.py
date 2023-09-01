
from PIL import Image
import os


images = []
label_id = []

labels = r'C:\Users\Umar Shafiq\Downloads\15 Days\Practice Challenge\DS60\p50' # selecting the folder
image_path = os.listdir(labels)

res = [sub[2:-4] for sub in image_path]  # after 2 letters and till 4 letters from back, e.g. af1.jpg then -> 1 
res
len(res)


for i in range(1, len(res)+1):
    for j in range(1,len(res)+1):
        i = str(i)
        if int(i) == j:
            print(j)
            
            img = Image.open(labels + '/' + 'af' + i + '.jpg')
            
            im = img.convert('RGB')
            
            images.append(im)
    
bsm = Image.open(r'C:\Users\Umar Shafiq\Downloads\15 Days\Practice Challenge\DS60' + '/' + 'bsm.jpg')    
im = bsm.convert('RGB')    
      
im.save(labels + '.pdf', save_all=True, append_images=images)


