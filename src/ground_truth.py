import random
import numpy as np
from grid_maker import grid 


def main():

    y = 50
    x = 100
    moves = ['U', 'D', 'L', 'R']

    for i in range(10):

        g = grid(grid_dim=[y, x])
        state_space, value_space = g.grid_gen()

        for j in range(10):

            _y = random.randint(0, y-1)
            _x = random.randint(0, x-1)
            while state_space[_y, _x] == 'B':
                _y = random.randint(0, y-1)
                _x = random.randint(0, x-1) 
            
            grid_start = [_y,_x]
            
            current = grid_start
            move_track = ''
            sense_track = ''
            current_track = []
            for c in range(100):
                
                m = moves[random.randint(0,3)]

                do_move = True
                if random.random() < 0.1:
                    do_move = False

                if do_move:
                    if m == 'U' and current[0] != 0:
                        current = [current[0]-1, current[1]] if state_space[current[0]-1, current[1]] != 'B' else current
                    elif m == 'D' and current[0] != y-1:
                        current = [current[0]+1, current[1]] if state_space[current[0]+1, current[1]] != 'B' else current
                    elif m == 'L' and current[1] != 0:
                        current = [current[0], current[1]-1] if state_space[current[0], current[1]-1] != 'B' else current
                    elif m == 'R'and current[1] != x-1:
                        current = [current[0], current[1]+1] if state_space[current[0], current[1]+1] != 'B' else current

                correct_sense = True
                if random.random() < 0.1:
                    print("here")
                    correct_sense = False
                
                s = state_space[current[0], current[1]]
                if not correct_sense:
                    senses = ['N', 'H', 'T']
                    senses.remove(s)
                    s = senses[random.randint(0,1)]

                move_track += m
                sense_track += s
                current_track.append(current)

            file = "map" + str(i+1) + "/grid" + str(j+1) + ".txt"
            with open(file, "w") as f:
                f.write("x0y0: [" + str(grid_start[1]) + "," + str(grid_start[0]) + "]\n")
                f.write("xiyi: [" + str(current_track[0][1]) + "," + str(current_track[0][0]) + "]")
                for cord in current_track[1:]:
                    f.write(", [" + str(cord[1]) + "," + str(cord[0]) + "]")
                f.write("\nalpha: " + move_track + "\n")
                f.write("e: " + sense_track)
        np.save('map' + str(i+1) + "/state_space", state_space)
        np.save('map' + str(i+1) + "/value_space", value_space)


if __name__ == "__main__":
    main()