from scipy.stats import johnsonsu
import numpy as np
import matplotlib.pyplot as plt

color = ["b-", "g-", "r-"]
a     = [-2.,1.,3.]
b     = 2.
loc   = 1.1
scale = 1.5

i = 0

fig, ax = plt.subplots(1, 1)
for i in range(len(a)):
    x = np.linspace(johnsonsu.ppf(0.01, a[i], b, loc, scale), johnsonsu.ppf(0.99, a[i], b, loc, scale), 100)
    ax.plot(x, johnsonsu.pdf(x, a[i], b, loc, scale), color[i], lw=2, alpha=0.6, label='johnsonsu pdf')
    
fig.savefig("johnsonsu_sample_a.png", bbox_inches="tight", dpi=300, transparent=True)



color = ["b-", "g-", "r-"]
a     = 1
b     = [1,2,3]
loc   = 1.1
scale = 1.5

i = 0

fig, ax = plt.subplots(1, 1)
for i in range(len(b)):
    x = np.linspace(johnsonsu.ppf(0.01, a, b[i], loc, scale), johnsonsu.ppf(0.99, a, b[i], loc, scale), 100)
    ax.plot(x, johnsonsu.pdf(x, a, b[i], loc, scale), color[i], lw=2, alpha=0.6, label='johnsonsu pdf')
    
fig.savefig("johnsonsu_sample_b.png", bbox_inches="tight", dpi=300, transparent=True)