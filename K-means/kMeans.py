import numpy as np

def loadDataSet(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float,curLine))
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA,vecB):
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))

def randCent(dataSet, k):
    n = dataSet.shape[1]
    centroids = np.mat(np.zeros((k, n)))
    for j in range(n):
        minJ = np.min(dataSet[:,j])
        maxJ = np.max(dataSet[:,j])
        rangeJ = float(maxJ - minJ)
        centroids[:,j] = minJ + rangeJ * np.random.rand(k,1)
    return centroids

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = dataSet.shape[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                dist = distMeas(dataSet[i,:],centroids[j,:])
                if dist < minDist:
                    minDist = dist
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2

        for c in range(k):
            index = dataSet[np.nonzero(clusterAssment[:,0] == c)[0]]
            centroids[c,:] = np.mean(index, axis=0)
            
        #print(centroids)
        
    return centroids,clusterAssment

def biKMeans(dataMat, k, distMeas=distEclud):
    m = dataMat.shape[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroid0 = np.mean(dataMat, axis=0).tolist()[0]
    centList = [centroid0]
    for i in range(m):
        clusterAssment[i,1] = distMeas(dataMat[1,:],centroid0)**2

    while len(centList) < k:
        lowestSSE = np.inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataMat[np.nonzero(clusterAssment[:,0] == i)[0],:] #在簇i中，不为0的x轴坐标
            centroids, splitClustAss = kMeans(ptsInCurrCluster, 2)
            sseSplit = np.sum(splitClustAss[:,1],axis=0)
            sseNotSplit = np.sum(clusterAssment[np.nonzero(clusterAssment[:,0] != i)[0],1],axis = 0)
            print(sseSplit, sseNotSplit, sseSplit+sseNotSplit)

            if(sseSplit + sseNotSplit) < lowestSSE:
                baseCentTosplit = i
                baseCentroid = centroids
                bestClusterAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        
        bestClusterAss[np.nonzero(bestClusterAss[:,0] == 1)[0],0] = len(centList)
        bestClusterAss[np.nonzero(bestClusterAss[:,0] == 0)[0],0] = baseCentTosplit
        centList[baseCentTosplit] = baseCentroid[0,:].tolist()[0]
        centList.append(baseCentroid[1,:].tolist()[0])
        clusterAssment[np.nonzero(clusterAssment[:,0] == baseCentTosplit)[0],:] = bestClusterAss
    return centList,clusterAssment
