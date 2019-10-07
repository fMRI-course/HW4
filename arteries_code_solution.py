""" Find the arteries exercise
"""

#: Our usual imports
import numpy as np  # Python array library
import matplotlib.pyplot as plt  # Python plotting library

#: Import nibabel
import nibabel as nib

#- Use nibabel to load the image ds107_sub001_highres.nii

img=nib.load('ds107_sub001_highres.nii', mmap=False)
#- img = ?
#- data = ?
data=img.get_data()
#- Plotting some slices over the third dimension
print(data.shape)
plane96=data[:,:,96]
# plt.imshow(plane96)
# plt.show()
#- Here you might try plt.hist or something else to find a threshold
data_1d=data.ravel()
# plt.figure()
# plt.hist(data_1d)
# plt.show()
# #- Maybe display some slices from the data binarized with a threshold
# plt.figure()
# plt.imshow(plane96 > 240)
# plt.show()
#- Create a smaller 3D subvolume from the image data that still
#- contains the arteries
data_small=data[90:-90, 90:-90,10:130]
# plt.figure()
# plt.imshow(data_small[:,:,96])
# plt.show()
#- Try a few plots of binarized slices and other stuff to find a good
#- threshold
pct_99 = np.percentile(data_small, 99)
binarized_data = data_small > pct_99
#: Uncomment the next line after installing scikit-image
from skimage import measure


#: This function uses matplotlib 3D plotting and sckit-image for
# rendering
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def binarized_surface(binary_array):
    """ Do a 3D plot of the surfaces in a binarized image

    The function does the plotting with scikit-image and some fancy
    commands that we don't need to worry about at the moment.
    """
    # Here we use the scikit-image "measure" function
    verts, faces = measure.marching_cubes_classic(binary_array, 0)
    fig = plt.figure(figsize=(10, 12))
    ax = fig.add_subplot(111, projection='3d')
    # Fancy indexing: `verts[faces]` to generate a collection of triangles\
    print('Peiwu')
    mesh = Poly3DCollection(verts[faces], linewidths=0, alpha=0.5)
    ax.add_collection3d(mesh)
    ax.set_xlim(0, binary_array.shape[0])
    ax.set_ylim(0, binary_array.shape[1])
    ax.set_zlim(0, binary_array.shape[2])
    print('Peiwu')
    plt.show()
binarized_surface(binarized_data)
