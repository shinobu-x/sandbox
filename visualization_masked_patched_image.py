import random
import numpy as np
import matplotlib.pyplot as plt
import PIL
from einops import rearrange
import torch
import torchvision
from torch import nn
img = PIL.Image.open('art.png')
#plt.imshow(img)
#plt.show()
b = 1
patch_size = 16
numpy_img = np.asarray(img)
img = torchvision.transforms.ToTensor()(np.array(img))
c,h,w=img.shape
dim_w,dim_h = w/patch_size, h/patch_size
img = img.view(b, c, h//patch_size, patch_size, w//patch_size, patch_size)
img = img.permute(0,2,4,1,3,5).reshape(b,-1,c*patch_size**2)
img = img.squeeze(0).numpy()
fig = plt.figure(figsize=(8,8))
fig.suptitle("Ah......", fontsize=24)
fig.add_axes()
ratio = 0.3
count = 0
for i in range(0, img.shape[0]):
    x = i % int(dim_w)
    y = i // int(dim_h)
    patch = numpy_img[y*patch_size:(y+1)*patch_size, x*patch_size:(x+1)*patch_size].copy()
    r = random.uniform(0,10)
    if r > 5 and count < dim_w*dim_h/ratio:
        count += 1
        patch *= 0
    ax = fig.add_subplot(dim_w, dim_h, i+1)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.imshow(patch)
plt.savefig('ah.png')
