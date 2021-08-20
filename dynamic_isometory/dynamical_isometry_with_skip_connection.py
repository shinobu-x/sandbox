import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.nn import init

def f(L, N, skip = False):
    x = torch.zeros(224, 224)
    #init.normal_(x, 0.0, 1.0)
    #init.normal_(x, 0.0, 1.0 / (len(L) * 200))
    init.uniform_(x, 0.0, 1.0)
    #init.constant_(x, 1.0)
    #init.xavier_normal_(x)
    #init.kaiming_normal_(x)

    var = x.var().to('cpu').detach().numpy().copy() #0.045 #** 2
    num_layers = len(L) - 1
    scaling = (num_layers * N) ** -1
    qs = []
    for l in range(len(L)):
        if skip:
            if l == 0:
                q = var * scaling
                qs.append(np.sqrt(q))
            elif l == 1:
                q = q + (var * scaling * q)
                qs.append(np.sqrt(q))
            else:
                num_qs = len(qs)
                q = \
                    qs[num_qs - 1] + \
                    (var * scaling * qs[num_qs - 1]) + \
                    (2 * var * scaling * np.sqrt(qs[num_qs - 1]) * sum(qs))
                qs.append(np.sqrt(q))
        else:
            q = var / num_layers
            qs.append(q)
    return qs
L = np.linspace(0, 400, 401)
Y = f(L, 200, skip = True)
fig, ax = plt.subplots(2, 1, figsize = (8, 6))
ax[0].plot(L, Y, 'b', label = 'Range of y: 0 ~ 1.1')
ax[0].legend()
ax[0].set_yscale('log')
ax[0].set_xlabel('# of Layers')
ax[0].set_ylabel('Value of q')
ax[0].set_xlim(min(L), max(L))
ax[0].set_ylim(min(Y), max(Y))
ax[1].plot(L, Y, 'g', label = 'Range of y: 0.998 ~ 1.02')
ax[1].legend()
#ax[1].set_yscale('log')
ax[1].set_xlabel('# of Layers')
ax[1].set_ylabel('# of Layers')
ax[1].set_xlim(10, max(L))
ax[1].set_ylim(0.998, 1.02)
fig.savefig('./dynamic_isometry.png')
plt.show()
