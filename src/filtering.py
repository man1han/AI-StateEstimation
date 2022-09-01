import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mpl
import matplotlib.animation as animation

class filtering:

    def __init__(self, state_space, value_space, moves, sensor, path_coords, counter=None, map=None, iterations = 100):
        self.state_space = state_space
        self.value_space = value_space
        self.moves = moves 
        self.sensor = sensor
        self.path_coords = path_coords
        self.counter = counter
        self.map = map
        self.iterations = iterations
        
        self.y = state_space.shape[0]
        self.x = state_space.shape[1]
        self.blocked_list = self.is_blocked()

        self.error = []
        self.probability = []


        self.fig = plt.figure()
        self.ims = []
        im = plt.imshow(self.value_space, cmap='Greens', interpolation='nearest')
        self.ims.append([im])
        
    
    def filter(self, iteration = 0):
        if iteration == self.iterations:
            # ani = animation.ArtistAnimation(self.fig, self.ims, interval=len(self.ims), blit=True,
            # repeat_delay=1000)
            # plt.title("Heatmap for Robot Location")
            # plt.xlabel("x coordinate")
            # plt.ylabel("y coordinate")
            #ani.save(self.map + '/images' + '/heatmap' + str(self.counter) + '.gif', writer="imagemagick")
            #plt.clf()

            plt.bar(range(len(self.error)), self.error)
            plt.title("Barplot of Error at each step")
            plt.xlabel("Step")
            plt.ylabel("Distance from Actual Location")
            #plt.savefig(self.map + '/images' + '/error' + str(self.counter))
            plt.show()
            plt.clf()

            plt.bar(range(len(self.probability)), self.probability)
            plt.title("Barplot of Probability at each step")
            plt.xlabel("Step")
            plt.ylabel("Probability")
            plt.show()
            #plt.savefig(self.map + '/images' + '/probability' + str(self.counter))
            plt.clf()

            return self.value_space

        arr = np.full(shape=(self.y,self.x), fill_value=0.0)
        for x in range(0,self.x):
            for y in range(0,self.y):
                if [y, x] not in self.blocked_list:
                    r, c, m, n, arr1, arr2 = self.find_r_j(y, x, self.moves[iteration])
                    BLOCKED = True
                    for i in arr1: 
                                for j in arr2: 
                                    if 0 <= r + i < m and 0 <= c + j < n and i != j and [r+i, c+j] not in self.blocked_list:
                                        BLOCKED = False
                                        arr[r+i, c+j] += self.value_space[y, x] * 0.9
                                    elif i == 0 and j == 0:
                                        if BLOCKED:
                                            arr[r+i, c+j] += self.value_space[y, x] * 1
                                        else: 
                                            arr[r+i, c+j] += self.value_space[y, x] * 0.1
    

        for x in range(0,self.x):
            for y in range(0,self.y):           
                if self.state_space[y, x] == self.sensor[iteration]:
                    arr[y, x] *= 0.9
                else:
                    arr[y, x] *= 0.05
        
        arr *= 1/arr.sum()
        self.value_space = arr

        if iteration == 0 or iteration == 9 or iteration == 49 or iteration == 99: 
            norm = mpl.Normalize(vmin=0, vmax=0)
            norm.autoscale(arr)
            plt.title("Heatmap for Robot Location")
            plt.xlabel("x coordinate")
            plt.ylabel("y coordinate")
            im = plt.imshow(arr, cmap='Greens', interpolation='nearest', norm=norm)
            plt.show()
            #self.ims.append([im])
 
        self.probability.append(np.amax(arr))
        result = np.where(arr == np.amax(arr))
        listOfCordinates = list(zip(result[0], result[1]))
        max_prob = listOfCordinates[random.randint(0, len(listOfCordinates)-1)]
        self.error.append(math.sqrt((self.path_coords[iteration][0] - max_prob[1])**2 + (self.path_coords[iteration][1] - max_prob[0])**2))

        return self.filter(iteration+1)

    def is_blocked(self):
        blocked_list = []
        for x in range(0, self.x):
            for y in range(0, self.y):
                blocked_list.append([y, x]) if self.state_space[y,x] == 'B' else None
        return blocked_list

    
    def arr_from_evidence(self, move):
        if move == 'U':
            return [-1, 0], [0]

        if move == 'D':
            return [1, 0], [0]

        if move == 'L':
            return [0], [-1, 0]

        if move == 'R':
            return [0], [1, 0]

    def find_r_j(self, i, j, move):
        x = np.zeros(shape=(self.y,self.x))
        x[i, j] = 1 
        r, c = np.where(x)
        r = r[0]
        c = c[0]
        m, n = x.shape
        arr1, arr2 = self.arr_from_evidence(move)
        BLOCKED = True
        return r, c, m, n, arr1, arr2


