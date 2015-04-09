import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import dateutil
import matplotlib.mlab as mlab
import matplotlib

r = mlab.csv2rec('tele_index_W_temp_and_precip.csv')

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.set_title("phdi",fontsize=14)
ax.set_xlabel("NAO",fontsize=12)
ax.set_ylabel("SOI",fontsize=12)
ax.grid(True,linestyle='-',color='0.75')

#x = np.random.random(30)
#y = np.random.random(30)
#z = np.random.random(30)

x = r.nao #first column
y = r.soi #second column
z = r.phdi #third column

# http://stackoverflow.com/questions/5211174/normalizing-colors-in-matplotlib
# Make the norm
norm = matplotlib.colors.Normalize(vmin = np.min(z), vmax = np.max(z), clip = False)

# http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter
# scatter with colormap mapping to z value
surf = ax.scatter(x,y,s=20,c=z, marker = 'o', norm = norm, cmap = cm.jet );

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()