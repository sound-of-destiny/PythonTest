import kMeans
import numpy as np 
import matplotlib.pyplot as plt

dataMat = np.mat(kMeans.loadDataSet('kMeans/testSet2.txt'))
myCentroid, clustAssing = kMeans.kMeans(dataMat, 4)
#plt.plot(dataMat[:,0],dataMat[:,1], 'ro')
#plt.plot(myCentroid[:,0], myCentroid[:,1], 'gs')

dataMat2 = np.mat(kMeans.loadDataSet('kMeans/testSet2.txt'))
centList, myNewAssments = kMeans.biKMeans(dataMat2,3)
centList = np.mat(centList)
plt.plot(dataMat2[:,0],dataMat2[:,1], 'ro')
plt.plot(centList[:,0], centList[:,1], 'gs')

plt.show()