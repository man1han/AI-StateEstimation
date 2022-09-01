from os.path import exists
from filtering import filtering
import numpy as np
import re

def main():
    file = input("Please enter a ground truth file name: ")
    state_space = input("Please enter a state_space.npy file: ")
    value_space = input("Please enter a value_space.npy file: ")

    state = np.load(state_space)
    value = np.load(value_space)

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

    f = filtering(state, value, moves, sensor, path_coords) 
    f.filter()





if __name__ == "__main__":
    main()