#!/usr/bin/env python
# coding: utf-8

# # Matplotlib
# Read the tutorials: "Basic Usage" and "Pyplot Tutorial" in the link: https://matplotlib.org/stable/tutorials/index.html before solving the exercises below. The "Pyplot Tutorial" you do not read in detail but it is good to know about since the fact that there are two approaches to plotting can be confusing if you are not aware of both of the approaches.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.


# ### Plotting in Matplotlib can be done in either of two ways, which ones? Which way is the recommended approach?

# The procedural approach uses the Matplotlib module PyPlot (matplotlib.pyplot). Modules in Python packages are a way of organizing functions, into related or conceptual groupings. You can think of modules as subdirectories within the package’s main folder. This means that matplotlib.pyplot contains a variety of functions, which have names like matplotlib.pyplot.plot()
# 
# In contrast, the object-oriented approach involves starting by creating an instance of a Matplotlib Figure object and assigning it to a variable name (by convention, fig). Matplotlib allows a figure to contain more than one subplot; the set of subplots in a figure are called axes (each of the axes has an x-axis and a y-axis). Thus in creating a Figure object we need to assign it to a variable for the figure, and a list of the axes objects in the figure. Then we use methods on the individual axes to plot and modify the contents of each subplot
# 
# Den objektorienterade är att föredra.

# ### Explain shortly what a figure, axes, axis and an artist is in Matplotlib.

# Figure: är den ytan/objekt vi jobbar med som innehåller allt
# Axes: ytan du ska visualisera din data på.
# Axis: Y och X axel, sätter var det är för skala, mätvärder etc.
# 
# 
# 
# Artist:Allt som syns i din graf, inklysive serier, axis etc

# ### When plotting in Matplotlib, what is the expected input data type?

# arrays med data

# ### Create a plot of the function y = x^2 [from -4 to 4, hint use the np.linspace function] both in the object-oriented approach and the pyplot approach. Your plot should have a title and axis-labels.

# In[5]:


#fig, ax2 = plt.subplots()  # Create a figure containing a single axes.
#ax2.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

import matplotlib.pyplot as plt
N = 100
#y = np.zeros(N)
x = np.linspace(-4, 4, N, endpoint=True)

plt.figure(figsize=(4, 4), layout='constrained')
plt.plot(x, x**2, label='quadratic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("y=xt")
plt.legend()


# In[8]:


#N = 100
#x = np.linspace(-4, 4, N, endpoint=True)

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
ax.plot(x, x**2, label='quadratic') 
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.


# ### Create a figure containing 2  subplots where the first is a scatter plot and the second is a bar plot. You have the data below. 

# In[10]:


# Data for scatter plot
np.random.seed(15)
random_data_x = np.random.randn(1000)
random_data_y = np.random.randn(1000)
x = np.linspace(-2, 2, 10) #ändrade från 100 till 10 för utseendets skull
y = x**2

# Data for bar plot
fruit_data = {'grapes': 22, 'apple': 8, 'orange': 15, 'lemon': 20, 'lime': 25}
names = list(fruit_data.keys())
values = list(fruit_data.values())


# 

# In[11]:


fig, axs = plt.subplots(1, 2, figsize=(9, 3), sharey=True)
axs[1].scatter(x, y)
axs[0].bar(names, values)
#axs[2].plot(names, values)
fig.suptitle('2 subplots')

