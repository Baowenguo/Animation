# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:25:10 2018

@author: Administrator
"""

import random
import operator
import matplotlib.pyplot
import matplotlib.animation 


num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#IO. Read in the environment
f = open("in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    environment.append(data_line)
print(environment)
f.close()


#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,299),random.randint(0,299)])

def update(frame_number):
    
    fig.clear()   
#environment
    matplotlib.pyplot.imshow(environment)

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 299 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 299
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 299 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 299 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

matplotlib.pyplot.show()