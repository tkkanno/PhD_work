#plot average spectra and normalised spectra
#!/usr/bin/python
from pylab import *
from matplotlib.colors import LogNorm
import numpy as np

directory = raw_input("write directory. Makes sure to add '/' at the end: ")
print "data needs to have ppm in the first line!!"
filein = raw_input("write spectra file_name: ")

classes = raw_input("write class file name: ")
print "Loading Files..."
first = directory + filein
class_file = directory + classes

data = np.loadtxt(first)
cls = np.loadtxt(class_file)
print "Done."

ppm = np.array(data[0,])
data = np.delete(data, 0,0)

#define normlisation techniques, have to learn how to use self stuff!
def scaletointegral(ydata):
        integral = ydata.sum(1) / 100
        newydata = np.transpose(ydata.T / integral)
        return np.array(newydata)
        
def scalepqn(ydata):
      # 1: scale to integral
      newydata = scaletointegral(ydata)
      # 2: reference spectrum is median of all samples
      yref = np.median(ydata, 0)
      # 3: quotient of test spectra with ref spectra
      yquot = newydata / yref
      # 4: median of those quotients
      ymed = np.median(yquot, 0)
      # 5: divide by this median
      newydata = newydata / ymed
      return np.array(newydata)
      
#normlaise data
datapqn = scalepqn(data)

#separate data into classes
#get the number of classes from the user
#and create a dict with a list for each class
print "there are %s samples" %len(cls)
condition = int(raw_input('how many classses are there? '))

dct = {}
means = {}
stdevs = {}
labels = []

color_list = ['b', 'r', 'g', 'y', 'c', 'm', 'k']

for i in range(condition):
  labels.append('con_%s' %i)
  
  dct['con_%s' % i] = []

#split the spectra into lists of each class
for i in range(len(cls)):
  for m in range(condition):
    if m == cls[i]:
      dct['con_%s' %m].append(datapqn[i,])
    else:
      pass
#vstack the lists turning them into numpy arrays
for i in range(condition):
  dct['con_%s' %i] = np.vstack(dct['con_%s' %i])


#create mean and standard deviation of data
#create second dictionary of mean and std of each class
for i in range(condition):
  means['con_%s' %i] = np.mean(dct['con_%s'%i], axis = 0) 
  stdevs['con_%s' %i] = np.std(dct['con_%s'%i ], axis = 0) 


#plot spectra colored by class
fig, ax = plt.subplots(1)

for i in range(condition):
  ax.plot(ppm, means['con_%s' %i ], label = labels[i] , color = color_list[i]) 
  ax.fill_between(ppm,  means['con_%s' %i ] + stdevs['con_%s' %i ], \
			  means['con_%s'%i ] - stdevs['con_%s' %i ],\
		    facecolor = color_list[i], alpha = 0.2) 

ax.set_title('Mean PQN normalised spectra with Standard Deviation')
ax.legend(loc = 'upper left')
ax.set_xlabel('PPM/Bucket')
ax.set_ylabel('Peak Intensity (Arbitrary Units)')
ax.invert_xaxis()
ax.grid()
plt.show()