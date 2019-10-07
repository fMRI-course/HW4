""" Four dimensions exercise
"""

#: Our usual imports
import numpy as np  # the Python array package
import matplotlib.pyplot as plt  # the Python plotting package

#- Load image object using nibabel
import nibabel as nib
img=nib.load('ds107_sub012_t1r2.nii', mmap=False)
data=img.get_data()
print(data.shape)
#- Turn off nibabel memory mapping.

#- Get image array data from image object

#- Get the 10th volume and show shape
vol10=data[...,9] #it should be 9.
print(vol10.shape)
#- Standard deviation across all voxels for 10th volume
print('The varianc of vol 10 is', np.var(vol10))
#print('The varianc of vol 10 is', np.var(vol10.ravel()))
#- Get standard deviation for each volume; then plot the values

vol_std=[]
for i in range(data.shape[-1]):
    vol=data[...,i]
    vol_std.append(np.std(vol))
print(type(vol_std))
#print(len(vol_std))

# print(vol_std)
plt.figure()
plt.plot(vol_std)
# plt.show()
#- Read global signal values calculated by SPM, and plot
global_sig=open('global_signals.txt','rt')
content=global_sig.read()
print(type(content))
# print(content)
# plt.plot(content)
# plt.show()

#- Apply algorithm for SPM global calculation to first volume
vol0=data[...,0]
M=np.mean(vol0.ravel())
vol0_thresh=vol0 > M/8
W=vol0[vol0_thresh]
M_thresh=np.mean(W.ravel())
print(M_thresh)
print(type(M_thresh))
# plt.plot(float(M_thresh))
# axes=plt.gca()
# axes.set_ylim([0,10])
# plt.show()
#- Make an `spm_global` function that accepts a 3D array as input,
#- and returns the global mean for the volume according to the SPM
#- algorithm
def spm_global(vol):
    M=np.mean(vol.ravel())
    vol_thresh=vol > M/8
    W=vol[vol_thresh]
    M_thresh=np.mean(W.ravel())
    print(M_thresh)
    return M_thresh

#- Write a function `get_spm_globals` that returns the global values
#- for each volume
spm_glob=[]
for i in range(data.shape[-1]):
    vol=data[...,i]
    spm_glob.append(spm_global(vol))
print(spm_glob)
plt.figure()
plt.plot(spm_glob)
plt.show()
