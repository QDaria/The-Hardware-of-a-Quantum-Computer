#!/usr/bin/env python
# coding: utf-8

# # kreyCat

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# 

# In[2]:


def cat(α, θ, q, p):
    return 1/(2*π)*1/(1 + np.cos(θ)*np.exp(-2*α**2))*(
        np.exp(-p**2 - (q + np.sqrt(2)*α)**2) + 
        np.exp(-p**2 - (q - np.sqrt(2)*α)**2) +
        2*np.cos(θ - 2*np.sqrt(2)*α*p)*np.exp(-q**2 - p**2))
π = np.pi
rq = 3
rp = 3
t = 0.003
fonts = 20

q = np.linspace(-rq, rq, 100)
p = np.linspace(-rp, rp, 100)
q, p = np.meshgrid(q, p)

for θ in [0, π]:
    for α in np.arange(0.5, 3, 0.5):
        plot = plt.figure(figsize=(8, 8))
        ax = plt.axes(projection='3d')
        ax.plot_surface(
            q, p, cat(α, θ, q, p),
            rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set_xlabel('q')
        ax.set_ylabel('p')
        ax.set_zlabel('W')
        ax.set_xlim(-rq, rq)
        ax.set_ylim(-rp, rp)
        ax.set_zlim(-1/π, 1/π)
        ax.set_xticks(np.arange(-rq, rq+1))
        ax.set_yticks(np.arange(-rp, rp+1))
        ax.set_zticks(np.arange(-1, 1+1, 1/4)/π)
        ax.view_init(elev=30, azim=-60)
        ax.set_title(f'$\\alpha={α}$, $\\theta={θ}$')
        plt.show()
        plt.close()

plt.savefig('Krey_cat.png', dpi=300)

plt.show()


# In[ ]:




