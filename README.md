# State-Estimation-AI

This repository contains code for a state estimation Algorithm that predicts an agent's location given its recoded transitions and observations.

## Introduction
Before the algorithm is run, 100 x 50 state space grids are generated with each cell receiving a label from [B, H, T, N]. Given the grid layout, an agent is placed randomly and performs 100 random moves, observing the cell it is standing on after each move.

The transition model for the agent passes 90% of the time (the agent moves) and fails 10% of the time (the agent says it moves but doesn't). The observation model for the agent passes 90% of the time (records the current cell correctly) and fails 10% of the time with a 5% chance it records one of the other two possible cells. 

After the agent takes 100 random actions, the 100 observations, 100 actions, and 100 true location coordinates are saved to a file. The whole process of dropping an agent in randomly and having it perform 100 actions is done 10 times per map, with 10 maps in total. 

## Example
Now it's time to use the State Estimation. By taking a map and a file recording of an agent's 100 actions and observations in that map, I can create a heatmap of the probability of the agent being in each cell at a specific timestamp without knowing where the agent originally started. 

We can look through how the algorithm handles the first saved actions of the agent in the first state map. 

After the agent performs 100 random movements on the state space, the following file is saved [action_file](https://github.com/JDunich/State-Estimation-AI/blob/main/src/data/map1/grid1.txt)

We can then feed the state estimation algorithm this action_file along with the original state space and we are left with the following statistics. 

### Heatmap Of Probability 
The darker the green, the larger the probability the agent is at that location for each iteration. As more observations and actions are seen, the algorithm can widdle down to a single point.  
 
 <p align="center"><img src="https://github.com/JDunich/State-Estimation-AI/blob/main/src/data/map1/images/heatmap1.gif" width="600" height="450"/></p>

### Barplot of Probability 
The barplot below shows the highest probability at each iteration. 

<p align="center"><img src="https://github.com/JDunich/State-Estimation-AI/blob/main/src/data/map1/images/probability1.png" width="600" height="450"/></p>

### Barplot of Error
The barplot below shows the distance from the highest probability point in the heatmap, to the true location of the agent. 

<p align="center"><img src="https://github.com/JDunich/State-Estimation-AI/blob/main/src/data/map1/images/error1.png" width="600" height="450"/></p>
