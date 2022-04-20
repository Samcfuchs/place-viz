import sys
import numpy as np
import matplotlib.pyplot as plt

def gen_color_map():
    # This is an arbitrary file, but don't change it--our colormap needs to be consistent
    #file = "data/img_2022/images_single/0-1648901427.png"
    # I think they added new colors at some point in the experiment? There are
    # 32 colors at the end (that's 5 bits)
    file = "data/img_2022/images_quadro/0/0-1649071837.png"

    im = plt.imread(file)
    colors = np.unique(im.reshape(-1,4), axis=0)

    # I don't know how this sort function works but it should make this function
    # invariant to which particular file we use
    #colors.sort(axis=0)

    return colors

def parse_image(fn, colors=gen_color_map()):
    im = plt.imread(fn)

    false_colors, false_ind = np.unique(im.reshape(-1,4), axis=0, return_inverse=True)
    assert (false_colors == colors).all()

    #false_color_dict = {k:i for i,k in enumerate(colors)}
    #print(false_color_dict)

    #view_color_map(false_colors)

    #ind = np.vectorize(color_dict.__getitem__)(im)
    #colors_int = (colors * 255).astype(int)
    #im_int = (im * 255).astype(int)
    #print(colors_int)
    #ind = colors_int[im_int]
    
    return false_ind.reshape((im.shape[0],im.shape[1]))

def view_color_map(cmap):
    print("Unique Colors:", len(cmap))
    print((cmap*255).astype(int))
    plt.imshow(cmap.reshape((4,8,4)))
    plt.show()

colors = gen_color_map()

view_color_map(colors)

file = "data/img_2022/images_quadro/1/1-1649059774.png"
ind = parse_image(file, colors)
print(ind)

