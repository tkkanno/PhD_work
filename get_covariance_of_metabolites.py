import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

print "This script will extract the covariance of the backscaled loadings plots of one opls comparison"
print """Make sure the csv file with the metabolite information you want to extract has header names "ppm" and "metabolite"""
#directory = raw_input('write directory ending with /' )
#datafile = raw_input('numpy backscaled loading data file: ')
#metabolite_list = raw_input('metabolites csv file: ')

directory = raw_input("Directory please: ")
datafile = raw_input("experiment labels: ")
metabolite_list = raw_input("metabolite list: ")

data = np.load(directory+datafile+'backscaled_loadings.npy')
labels = pd.read_csv(directory + metabolite_list)
ppmz = np.load(directory+datafile+'xaxis.npy')
d1 = np.mean(data[0], axis = 1)
if ppmz.shape[0] != d1.shape[0]:
  print "the ppm and backscale loadings don't corrispond, check their shapes"
#fig, ax  = plt.subplots()
#ax.plot(ppmz, d1)
#ax.invert_xaxis()
#print "showing covariance of data. If it looks right close the plot and script will continue"
#plt.show()

m_ppm = np.array(labels.ppm)
x=[]
print "ppm --- metabolite --- covariance"
for i in range(len(m_ppm)):
  if np.isnan(m_ppm[i]) == False:
    idx = np.argmin(np.abs(ppmz-m_ppm[i]))
    x.append(d1[idx])
    print m_ppm[i], labels.Metabolite[i], d1[idx]
  else:
    x.append(np.nan)
  
x = np.array(x)
print "Done. Saving Data"

labels['covariance'] = x
labels.to_csv(directory + 'metabolites_covariance')
print " data saved as metabolites_covariance in given directory"
