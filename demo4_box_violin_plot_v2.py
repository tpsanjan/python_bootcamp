import numpy as np
import matplotlib.pyplot as plt

# Fix random state for reproducibility
np.random.seed(0)       

# Generate dummy data using np.random.normal(mean, stdev, size):
data = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))

# Note: size(data) = 100 rows x 3 cols
print(type(data), 'Size = ', data.shape)
print('Mean(vals in row-0) = ',np.mean(data[:,0]))
print('Mean(vals in row-1) = ',np.mean(data[:,1]))
print('Mean(vals in row-2) = ',np.mean(data[:,2]))

# Generate box/ violin plot:
'''
plt.boxplot(data)
plt.title('Box plot')
''
plt.violinplot(data)
plt.title('Violin plot')
''
plt.xlabel('Three separate samples')
plt.ylabel('Observed values')
'''
# To set plot aesthetics
plt.style.use('_mpl-gallery')

# Additional options: notch = True, vert = False
plt.boxplot(data, positions = [2, 4, 6], widths = 1.5, patch_artist = True,
                showmeans = False, showfliers = False,
                notch = True, vert = False,
                medianprops = {"color": "white", "linewidth": 0.5},
                boxprops = {"facecolor": "C0", "edgecolor": "white",
                          "linewidth": 0.5},
                whiskerprops = {"color": "C0", "linewidth": 1.5},
                capprops = {"color": "C0", "linewidth": 1.5})

plt.xlim(0,8)
plt.ylim(0,8)

plt.yticks(np.arange(1,8))
''
plt.tight_layout()
plt.show()
