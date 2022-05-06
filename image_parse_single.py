import sys
import numpy as np
import matplotlib.pyplot as plt
import glob
from tqdm import tqdm
import pickle
from matplotlib.colors import rgb2hex
from datetime import datetime as dt
import gc

def rgba_to_hex_mat(mat):
    flat = mat.reshape(-1,4)
    flat_hex = np.array([rgb2hex(flat[i,:]) for i in range(flat.shape[0])])
    return flat_hex.reshape(mat.shape[0],mat.shape[1])

def tohex(array):
    array = np.asarray(array*255, dtype='uint32')
    return ((array[:, :, 0]<<16) + (array[:, :, 1]<<8) + array[:, :, 2])

def rgbtoint(color):
    color = (color*255).astype(int)
    return (color[0]<<16) + (color[1]<<8) + color[2]


def gen_color_map():
    """
    Uses an arbitrary image to construct a map from unique color values to
    integer indices in the range [0-31]. By passing this map to the image
    parser, we can ensure that those indices are used consistently across
    different images.

    Returns a dictionary mapping {integer representation of hex code -> integer
    index}
    """

    # This is an arbitrary file, but don't change it--our colormap needs to be consistent
    file = "data/img_2022/images_quadro/0/0-1649071837.png"

    im = plt.imread(file)
    colors = np.unique(im.reshape(-1,4), axis=0)
    #colors_hex = list(map(rgb2hex, colors))
    colors_hex = list(map(rgbtoint, colors))

    color_map = {color:index for index,color in enumerate(colors_hex)}

    return color_map


""" This is the function that needs to be optimized """
def parse_image(filename, colors=gen_color_map()):

    im = plt.imread(filename)

    #im_hex = rgba_to_hex_mat(im)
    im_hex = tohex(im)

    indices = np.vectorize(colors.__getitem__)(im_hex)

    return indices.reshape((im.shape[0],im.shape[1]))


def view_color_map(cmap):
    print("Unique Colors:", len(cmap))
    print((cmap*255).astype(int))
    plt.imshow(cmap.reshape((4,8,4)))
    plt.show()


def parse_in_folder(folder_path, colors=gen_color_map()):

    paths = glob.glob(folder_path)
    N = len(paths)
    print("Images found:", N)
    
    mat = np.zeros(shape=(len(paths),1000,1000), dtype=np.int8)

    for i in tqdm(range(N)):
        mat[i] = parse_image(paths[i], colors)

        # Clear out the memory leaks
        if i % 100 == 0:
            gc.collect()
    
    return mat

if __name__ == "__main__":
    color_map = gen_color_map()

    # Get the time to parse one image
    file = "data/img_2022/images_quadro/1/1-1649059774.png"
    start = dt.now()
    ind = parse_image(file, color_map)
    print(ind)
    print("Time (s):", dt.now() - start)

    #sys.exit()

    # Parse all the images from 
    # mats = parse_in_folder("data/img_2022/images_*/*.png")
    t = 0
    mats = parse_in_folder(f"data/img_2022/images_single/*.png")
    with open(f"t{t}-c0.p", 'wb') as f:
        pickle.dump(mats, f)
