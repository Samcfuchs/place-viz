import numpy as np
import pickle
import os

# Opening pickle
filename = 'images.p'

infile = open(filename,'rb')
mat_dict = pickle.load(infile)
infile.close()

keyed_dict = dict()

for mat in mat_dict:
    
    old_key = mat
    new_key = mat[mat.rindex("-")+1:]  + "," + mat[mat.rindex("-")-1: mat.rindex("-")]
    keyed_dict[new_key] = mat_dict[old_key]

sorted_dict = dict(sorted(keyed_dict.items()))

key_list = list(sorted_dict.keys())

zero_list = list()
one_list = list()
two_list = list()
three_list = list()


def populate_matrix(i, amt):
    zero_1000 = np.zeros((1000, 1000), dtype=np.int64 )
    if amt == 1:
        zero_list.append(sorted_dict[key_list[i]])
        one_list.append(zero_1000)
        two_list.append(zero_1000)
        three_list.append(zero_1000)

    elif amt == 2:
        zero_list.append(sorted_dict[key_list[i]])
        one_list.append(sorted_dict[key_list[i+1]])
        two_list.append(zero_1000)
        three_list.append(zero_1000)

    elif amt == 4:
        zero_list.append(sorted_dict[key_list[i]])
        one_list.append(sorted_dict[key_list[i+1]])
        two_list.append(sorted_dict[key_list[i+2]])
        three_list.append(sorted_dict[key_list[i+3]])

i = 0
while i < len(key_list):
    key = key_list[i]
    if key[:key.index(",")-1] == key_list[i+3][:key_list[i].index(",")-1]:
        populate_matrix(i, 4)
        i = i+4
    elif key[:key.index(",")-1] == key_list[i+1][:key_list[i].index(",")-1]:
        populate_matrix(i, 2)
        i = i+2
    else:
        populate_matrix(i, 1)
        i = i+1

zero_matrix = np.dstack(zero_list)
one_matrix = np.dstack(one_list)
two_matrix = np.dstack(two_list)
three_matrix = np.dstack(three_list)


final_matrix = np.vstack([np.hstack([zero_matrix, one_matrix]), np.hstack([two_matrix, three_matrix])])

print(final_matrix.shape)

# matrix_reshaped = final_matrix.reshape(final_matrix.shape[0], -1)

# np.savetxt("test.csv", matrix_reshaped, delimiter =",")