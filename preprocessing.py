import h5py
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2hed

D=h5py.File('breast.h5', 'r')
#X:images
#Y:Cell counts
#P:Patient IDs
X,Y,P = D['images'], np.array(D['counts']),np.array(D['id'])

# X_hed = []
# for i in range(7404):
#     X_hedImage = rgb2hed(X[i])
#     X_hed.append(X_hedImage)
#     if i%100 == 0:
#         print((i/7404)*100, "%")
print("ok")
X_hed_brown = rgb2hed(X[:3000])[:,:,:,2]
print(X_hed_brown.shape)

# from numpy import save
# from numpy import load
# X_hed_array = np.array(X_hed)
# save("X_hed_array.npy", X_hed_array)
# X_hed_array = np.load("X_hed_array.npy")
# print(X_hed_array.shape)
# plt.imshow(X_hed_array[0])