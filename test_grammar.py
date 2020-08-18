import numpy as np

pos_idx = np.random.permutation(5)
print(pos_idx)
pos_idx = np.concatenate([pos_idx, np.random.permutation(5)])
print(pos_idx)