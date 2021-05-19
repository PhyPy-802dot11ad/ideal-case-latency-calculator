import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('Multi-mpdu.csv', index_col=0)


x = np.arange((df.columns.values.size))
y = df.index.values + 1
z = np.copy(df.values)

fig = plt.figure(figsize=(20,12))
plt.subplots_adjust(left=0., top=0.95, right=0.95, bottom=0.05, wspace=0.1)

ax = fig.add_subplot(121, projection='3d')


Z = np.copy(z)
for m in range(z.shape[0]):
    Z[m,:] /= 10**6
X, Y = np.meshgrid(x, y)
ax.plot_surface( X, Y, Z, zorder=2, cmap=cm.coolwarm )

ax.set_xticks( x )
ax.set_xticklabels( df.columns.values )

ax.set_xlabel('MCS scheme', labelpad=10, fontsize=14)
ax.set_ylabel(r'Number of A-PPDUs', labelpad=10, fontsize=14)
ax.set_zlabel('Latency per A-PPDU transmission (ms)', labelpad=10, fontsize=14)

ax.set_title(f'Latency span: {round(Z.min(),3)}~{round(Z.max(),3)} ms', fontsize=20)


ax = fig.add_subplot(122, projection='3d')

for m in range(z.shape[0]):
    Z[m,:] = z[m,:] / y[m] / 10**6
X, Y = np.meshgrid(x, y)
ax.plot_surface( X, Y, Z, zorder=2, cmap=cm.coolwarm )

ax.set_xticks( x )
ax.set_xticklabels( df.columns.values )

ax.set_xlabel('MCS scheme', labelpad=10, fontsize=14)
ax.set_ylabel(r'Number of A-PPDUs', labelpad=10, fontsize=14)
ax.set_zlabel('Latency per additional A-PPDU (ms)', labelpad=10, fontsize=14)

ax.set_title(f'Latency span: {round(Z.min(),3)}~{round(Z.max(),3)} ms', fontsize=20)

plt.show()


fig = plt.figure(figsize=(10,6))
plt.subplots_adjust(left=0.1, top=0.98, right=0.98, bottom=0.1, wspace=0.35)

ax = fig.add_subplot(121)
ax.fill_between( y, z[:,0]/10**6, z[:,-1]/10**6, alpha=0.25, color='C0', zorder=2 )
ax.plot( y, z[:,0]/10**6, color='C0', lw=2, zorder=3 )
ax.plot( y, z[:,-1]/10**6, color='C0', lw=2, zorder=3 )
ax.set_xlabel(r'Number of A-PPDUs', labelpad=10, fontsize=14)
ax.set_ylabel('Latency per A-PPDU transmission (ms)', labelpad=10, fontsize=14)

ax = fig.add_subplot(122)
ax.fill_between( y, Z[:,0], Z[:,-1], alpha=0.25, color='C0', zorder=2 )
ax.plot( y, Z[:,0], color='C0', lw=2, zorder=3 )
ax.plot( y, Z[:,-1], color='C0', lw=2, zorder=3 )
ax.set_xlabel(r'Number of A-PPDUs', labelpad=10, fontsize=14)
ax.set_ylabel('Latency per additional A-PPDU (ms)', labelpad=10, fontsize=14)

plt.show()