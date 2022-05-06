import pickle
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import glob
import gc

t = 0
c = 1
N = 100

filename = f"data/compiled/t{t}-c{c}.p"

paths = glob.glob(f'data/compiled/t*-c{c}.p')
print(paths)
#raise KeyboardInterrupt()

with open(filename,'rb') as f:
    arr = pickle.load(f).reshape(-1,int(1e6))
    is_updated = arr == 0
    del arr
"""
arrays = []
for p in tqdm(paths):
    with open(p,'rb') as f:
        arr = pickle.load(f).reshape(-1,int(1e6))
        is_updated = arr == 0
        del arr
        gc.collect()
        arrays.append(is_updated)

    d = np.vstack(arrays)

del arrays
gc.collect()
"""

#print(d.shape)
    
#is_updated = d != 0

flat = is_updated

# Generate N splits
slices = np.linspace(0,d.shape[0],N+1).astype(int)

heatmaps_over_time = []
for i in tqdm(range(len((slices)) - 1)):
    subset = flat[slices[i]:slices[i+1]]
    heatmaps_over_time.append(subset.sum(axis=0))

vals = np.array(heatmaps_over_time)

np.savetxt(f"data/compiled/slices/sliced_updates_t{t}-c{c}_N{N}.csv", vals, delimiter=',', fmt='%.0f')
#plt.matshow(vals[4].reshape(1000,1000))
