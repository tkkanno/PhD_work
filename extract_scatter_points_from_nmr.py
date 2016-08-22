import numpy as np
import matplotlib.pyplot as plt#
import pandas as pd
import seaborn as sns
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
      
def mean_center(data):
  data = data - np.mean(data,0)
  data = np.nan_to_num(data)
  return data
  
def scale_pareto(data):
    data = mean_center(data) / np.sqrt(np.std(data,0))
    data = np.nan_to_num(data)
    return data
print "This script will take the pls input data and find the peak of a given assigned metabolites spreadsheet"
spread = 0.003
print "It will search within a range of %.3f ppm. If you want to change this, go into the script"%(spread)
print "this script may require iterations to refine the search space for peaks"
directory = raw_input("Directory please: ")
metabolite_list = raw_input("metabolites ppm list: ")
datafile = raw_input("pls input: ")


metdata = pd.read_csv(directory+metabolite_list)
mets= metdata['Metabolite']
data = np.loadtxt(directory+datafile)
clss = data[:,0]
data = data[:,1:]
clss = clss[1:]


ppm = data[0]
data = data[1:]
norm_dat = scalepqn(data)
scale_dat = scale_pareto(data)

x,y,z =[],[],[]
new_ppms = []
datlist = metdata['ppm']
mean_spect = np.mean(norm_dat, 0)


#find major peak within range of metabolite list and then write that slice to new arrays

if datlist[0] ==0:
  datlist = datlist[1:]

for i in datlist:
  print i
  #checks if the values given are really the peaks, if not, re-assigns to new peak
  idx = np.argmin(np.abs(ppm-i))
  idxmin =np.argmin(np.abs(ppm-(i-spread)))
  idxmax = np.argmin(np.abs(ppm-(i+spread)))
  sppm= ppm[idxmax:idxmin]
  slice_to_take = mean_spect[idxmax:idxmin].max()
  b = np.where(mean_spect == slice_to_take)
  #take slices of data where peak is highest
  if len(b)==1:
    b = b[0][0]
    idx = b
    new_ppms.append(ppm[idx])
    x.append(data[:,idx])
    y.append(norm_dat[:,idx])
    z.append(scale_dat[:,idx])
  else:
    print "too many equal values to this"
    break
    
new_ppms = np.vstack(new_ppms)

x = np.vstack(x)
y = np.vstack(y)
z = np.vstack(z)

n= clss.shape[0]
clss = np.reshape(clss, (n,1))
x, y, z = x.T, y.T, z.T
x = np.hstack((clss,x))
y = np.hstack((clss,y))
z = np.hstack((clss,z))

x = x[x[:,0].argsort()]
y = y[y[:,0].argsort()]
z = z[z[:,0].argsort()]
x = pd.DataFrame(x)
y = pd.DataFrame(y)
z = pd.DataFrame(z)
x.columns = mets
z.columns = mets
y.columns = mets

#z.boxplot(by = 'class')
#plt.show()
y.to_csv(directory + "raw_dataframe")
y.to_csv(directory +"normalised_dataframe")
z.to_csv(directory + "Scaled_dataframe")

new_ppms_to_save = np.vstack((0,new_ppms))
new_ppms_to_save = pd.DataFrame(new_ppms_to_save)
file_out = [mets,datlist,new_ppms_to_save]
file_out = pd.concat(file_out, axis = 1)
file_out.columns = ['Metabolite', 'old_ppm', 'new_ppm']
file_out.to_csv(directory+"new_ppm_values")
print "data saved to directory. Take the new ppm values to extract covariance \n data"


####generating 50 boxplots if you so desire from this data. is impossible to read but ok
#can simply do that with dp.df.boxplot(column = '', by = 'class')
data = (data/data.max()) *1000
fig,ax = plt.subplots()
for i in range(len(data)):
  ax.plot(ppm, data[i])


datlist= np.array(datlist)  
mets = np.array(mets[1:])
for i in range(len(datlist)):
  idx = np.argmin(np.abs(ppm-new_ppms[i]))
  print i, mets[i], datlist[i], new_ppms[i], idx
  ax.annotate(("%s, %.4f")%(mets[i], ppm[idx]), \
		xy = (new_ppms[i], data[:,idx].max()), \
		xycoords = 'data', \
		xytext =(datlist[i], data[:,idx].max() + (data[:,idx].max()) ),\
		arrowprops = dict(arrowstyle = "->"),\
		rotation = 60)
ax.invert_xaxis()
plt.show()
