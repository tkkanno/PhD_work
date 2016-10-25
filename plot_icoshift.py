#!/usr/bin/python
from pylab import *
import numpy as np
from matplotlib.colors import LogNorm

directory = raw_input("write directory. Makes sure to add '/' at the end: ")
filein = raw_input("write original spectra file_name: ")
shifted = raw_input("write aligned spectra file name: ")

print "Loading Files..."

first = directory + filein
second = directory + shifted


orig = np.loadtxt(first)
icoshift = np.loadtxt(second)

ppm = orig[0]
orig = orig[1:,:]

ppm_bin = icoshift[0]
icoshift = icoshift[1:,:]
#check if the first row is  ppm, if so delete it
if np.array_equal(ppm, icoshift[0]) == True:
  print 'ppm in shifted data file'
  icoshift = np.delete(icoshift,0,0)
  
if np.array_equal(ppm, orig[0])==True:
  print 'ppm in original datafile'
  orig = np.delete(orig,0,0)

print "Done."

if orig.min() < 0 or icoshift.min() <0 :
  orig = orig  - orig.min()
  icoshift = icoshift -icoshift.min()
  

levels = range(-10, 20)
ax1 = subplot(221)
title('Original data')
plot(orig.T)

subplot(222,sharex=ax1)
title('Original data')
contourf(orig, levels=levels)

subplot(223,sharex=ax1, sharey=ax1)
title('Aligned with Icoshift')
plot(icoshift.T)

subplot(224,sharex=ax1)
title('Aligned with Icoshift')
contourf(icoshift, levels=levels)
print "Plotting Files:"
show()

