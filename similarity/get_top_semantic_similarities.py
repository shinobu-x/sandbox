import os
import numpy as np
from PIL import Image
import torch
from CLIP import clip

device = 'cuda:1' if torch.cuda.is_available() else 'cpu'
mean = torch.tensor([0.48145466, 0.4578275, 0.40821073]).to(device)
std = torch.tensor([0.26862954, 0.26130258, 0.27577711]).to(device)
text = 'abstract landscape painting'
model,preprocess = clip.load("ViT-B/32")
model = model.to(device)
text_tokens = clip.tokenize(text).to(device)
with torch.no_grad():
    text_features = model.encode_text(text_tokens).float()
    text_features /= text_features.norm(dim=-1,keepdim=True)
images = []
exts = ['.jpg','.gif','png']
for f in os.listdir('./samples'):
    ext = os.path.splitext(f)[1]
    if ext.lower() in exts:
        images.append(Image.open(os.path.join('./samples',f)))
images = [preprocess(image) for image in images]
images = torch.tensor(np.stack(images)).to(device)
images -= mean[:,None,None]
images /= std[:,None,None]
image_features = torch.empty((0,512))
with torch.no_grad():
    image_features_batch = model.encode_image(images).float()
    image_features = torch.cat([image_features, image_features_batch.cpu()],dim=0)
image_features /= image_features.norm(dim=-1,keepdim=True)
similarities = text_features.cpu().numpy()@image_features.cpu().numpy().T
results = zip(range(len(similarities[0])),similarities[0])
results = sorted(results, key=lambda x:x[1],reverse=True)
top_scores = []
top_images = []
indices = []
for i,score in results[:10]:
    top_scores.append(score)
    top_images.append(images[i])
    indices.append(i)
print(top_scores)
