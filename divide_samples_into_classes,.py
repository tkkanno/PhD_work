import numpy as np
direct = raw_input('directory names here: ')
data = raw_input('file name: ')
c = raw_input('class file name ')

data = np.loadtxt(direct+ data)
c = np.loadtxt(direct+c)
ppm = data[0]
data = data[1:,:]



#with open('/home/louic/Desktop/mouse_pellets/all_cpmg/sample_labels', 'rb') as f:
  #reader = csv.reader(f)
  #for row in reader:
    #labels.append(row)
    
#temp_labels = [item for sublist in labels for item in sublist] #flattens list
#labels = temp_labels
#classes = set(t) #makes set to find unique items
##turn set back into list
#classes = list(classes)
#direct = '/home/louic/Desktop/mouse_pellets/all_pls_comparisons/'


#loop through to make numpy arrays of all comparisons
def divide_data(direct, data,cls):
  classes = np.unique(cls)
  for first_group in range(len(classes)):
    for second_group in range(first_group+1,len(classes)):
      temp_list = []
      cls_array  = []

      for i in range(len(data)):
	if cls[i] == classes[first_group]:
	  cls_array.append(0)
	elif cls[i] == classes[second_group]:
	  cls_array.append(1)
      cls_array = np.vstack(cls_array)
      cls_array = np.vstack((0,cls_array))
      
      temp_list = [data[row] for row in range(len(data)) if (cls[row] == classes[first_group] or \
						      cls[row] == classes[second_group])]

      temp_array = np.vstack(temp_list)
      temp_array = np.vstack((ppm,temp_array))
      temp_array = np.hstack((cls_array, temp_array))
      print first_group, second_group
      np.savetxt(direct+"pls_input_%s_vs_%s"%(classes[first_group], classes[second_group]), \
		  temp_array)
divide_data(direct, data, c)
#def create_pls_inputdat(direct, data, ppm, cls):
  #p = np.unique(cls)
  #for i in range(len(p)):
    #dat = [data[j] for j in range(len(cls)) if cls[j] ==0 or cls[j] ==i]
    #dat = np.vstack(dat)
    #datcls = [cls[k] for k in range(len(cls)) if cls[k] ==0 or cls[k] == i]
    #datcls = np.vstack(datcls)
    #clspls = np.vstack((0,datcls))
    #pls = np.vstack((ppm, dat))
    #plsinput = np.hstack((clspls, pls))
    #print i
    #np.savetxt(direct+'ctrl_vs_%i_plsinput'%(i), plsinput)
