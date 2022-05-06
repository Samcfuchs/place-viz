import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import gc

# Load pickle with 3D array of pixel values.

t = 2
c = 2
name = "100"

with open(f'data/compiled/t{t}-c{c}.p','rb') as f:
    arr = pickle.load(f)

# Compute changes
left = arr[:-1]
right = arr[1:]
diff = left-right

print(diff.shape)

del arr
gc.collect()

# Grab a subset of the data if you want
# sample = diff[ :, 497:528, 175:244] #canada
sample = diff[188:3010, (1733-1000):(1947-1000), 540:714] #Dutch 
print(sample.shape)

# This is the part that takes the longest
changes = sample != 0

# Sum changes through all time-steps
n_updates = changes.sum(axis=0)
print(n_updates.shape)

# Normalize the distribution of pixel values so it looks more legible
def normalizer(n, k=1):
    return np.log(n+k)

norm_updates = normalizer(n_updates, k=5)

# Save these values to CSV files
# np.savetxt(f"data/compiled/dutch_n_updates_t{t}-c{c}.csv", n_updates.astype(int), delimiter=',', fmt='%.0f')
# np.savetxt(f"data/compiled/dutch_norm_updates_t{t}-c{c}.csv", norm_updates, delimiter=',', fmt='%.4f')
np.savetxt(f"data/compiled/dutch_n_updates_" + name + ".csv", n_updates.astype(int), delimiter=',', fmt='%.0f')
np.savetxt(f"data/compiled/dutch_norm_updates_" + name + ".csv", norm_updates, delimiter=',', fmt='%.4f')