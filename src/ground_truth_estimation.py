from itertools import count
from os.path import exists
from filtering import filtering
import numpy as np
import re

np.set_printoptions(threshold=np.inf)

def get_numpy(folder):
    state = np.load(folder + "/state_space.npy")
    value = np.load(folder + "/value_space.npy")
    return state, value

def main():
    
    for fld in range(10):
        folder = 'data/map' + str(fld+1)
        state_space, value_space = get_numpy(folder)

        for counter in range(10):
            file = folder + '/grid' + str(counter+1) + '.txt'

            if exists(file):
                with open(file) as f:
                    file_data = [data.split(':')[1] for data in f.readlines()]
                    res = re.compile(r'[0-9]+')
                    start_coords = [int(x) for x in res.findall(file_data[0])]
                    path_data = file_data[1].split()
                    path_coords = [[int(x[0]), int(x[1])] for x in [res.findall(y) for y in path_data]]
                    moves = [x for x in file_data[2].strip()]
                    sensor = [x for x in file_data[3].strip()]
            else:
                print("File can not be found")
                return 

            #value_space = np.full(shape=(50,100), fill_value=0)
            #value_space[start_coords[1], start_coords[0]] = 1
            f = filtering(state_space, value_space, moves, sensor, path_coords, counter+1, folder)
            arr = f.filter()



    

if __name__ == "__main__":
    main()

