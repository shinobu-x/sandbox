import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import torch
import torch.nn.functional as F

def softmax_with_temperature(x, temperature: float):
    return F.softmax(x / temperature,dim=1)
num_classes=40
left=np.linspace(0,num_classes-1,num_classes)
input=torch.from_numpy(np.array([[norm.pdf(x=i, loc=20, scale=8) \
                                  for i in range(num_classes)]],
                                dtype=np.float32))
fig=plt.figure(figsize=(10.0,5.0))
temperatures=[0.01,0.03,0.05,0.1,0.2,0.5,0.75,1.0]
outputs=[]
labels=[r'$\tau$t='+str(i) for i in temperatures]
colors=['blue','green','red','cyan','magenta','orange','purple','salmon']
for i,temperature in enumerate(temperatures):
    output=softmax_with_temperature(input,temperature)
    ax=fig.add_subplot(2,4,i+1)
    ax.bar(left,output.data.flatten(),color=colors[i],label=labels[i])
    plt.legend()
fig.tight_layout()
plt.savefig('softmax_with_temperature.png')
plt.show()
