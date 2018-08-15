import numpy as np
import pymysql
import copy
import os
import pandas as pd
import math

#K-means算法
def distEcludn(vecA,vecB):
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))

def distEclud1(vecA,vecB):
    return np.abs(vecA - vecB)

def randCent(dataSet, k):
    n = 1
    centroids = np.mat(np.zeros((k, n)))
    for j in range(n):
        minJ = np.min(dataSet)
        maxJ = np.max(dataSet)
        rangeJ = float(maxJ - minJ)
        centroids[:,j] = minJ + rangeJ * np.random.rand(k,1)
    return centroids 

def kMeans(dataSet, k, distMeas=distEclud1, createCent=randCent):
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
                dist = distMeas(dataSet[i],centroids[j,:])
                if dist < minDist:
                    minDist = dist
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2

        for c in range(k):
            dataK = dataSet[np.nonzero(clusterAssment[:,0] == c)[0]]
            centroids[c,:] = np.mean(dataK, axis=0)
        
    return centroids,clusterAssment

#一元正态分布概率密度函数
def Normal(x,mu,sigma):
    
    #return np.exp(-(x-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)
    
    N = x.size
    Denom = np.zeros(N)
    for i in range(0,N):
        Denom[i] = math.exp((-1/(2*(np.float64(sigma**2))))*((np.float64(x[i]-mu))**2))/(np.sqrt(2*np.pi)*np.float64(sigma))
    return Denom
    


def GMM2(data):
    Mu=np.random.random((1,2))*100
    SigmaSquare=np.random.random((1,2))*100
    a=np.random.random()
    b=1-a
    Alpha=np.array([[a,b]])

    while(True):
        Old_Mu = copy.deepcopy(Mu)
    
        gauss1=Normal(data,Mu[0][0],np.sqrt(SigmaSquare[0][0]))
        gauss2=Normal(data,Mu[0][1],np.sqrt(SigmaSquare[0][1]))
    
        Gamma1=Alpha[0][0]*gauss1
        Gamma2=Alpha[0][1]*gauss2

        M=Gamma1+Gamma2

        SigmaSquare[0][0]=np.dot((Gamma1/M).T,(data-Mu[0][0])**2)/np.sum(Gamma1/M)
        SigmaSquare[0][1]=np.dot((Gamma2/M).T,(data-Mu[0][1])**2)/np.sum(Gamma2/M)
   
        Mu[0][0]=np.dot((Gamma1/M).T,data)/np.sum(Gamma1/M)
        Mu[0][1]=np.dot((Gamma2/M).T,data)/np.sum(Gamma2/M)

        Alpha[0][0]=np.sum(Gamma1/M)/N
        Alpha[0][1]=np.sum(Gamma2/M)/N

        if sum(abs(Mu[0]-Old_Mu[0])) < 0.1:
            break
    return Mu,np.sqrt(SigmaSquare),Alpha
'''
    if(max(Alpha[0][0],Alpha[0][1]) > 0.9):
        print("Mu:",Mu)
        print("Sigma:",np.sqrt(SigmaSquare))
        print("Alpha",Alpha)
        return Mu,np.sqrt(SigmaSquare),Alpha
    else:
        return 
'''

if __name__ == '__main__':
    #np.seterr(divide='ignore',invalid='ignore')
    conn = pymysql.connect(
        host='127.0.0.1',
        port = 3306,
        user='root',
        passwd='root',
        db ='supnuevo_statistics',

        charset='UTF8'
    )
    cur = conn.cursor()
    path = '/home/schong/schong/Data/newCodigo'
    codigoList = os.listdir(path)
    for codigocsv in codigoList:
        codigo = codigocsv.split('.')[0]
        codigofile = os.path.join(path + '/' + codigocsv)
        codigoData = pd.read_csv(codigofile,header=None,usecols=[0])
        data = codigoData.values
        N = codigoData.size
        if N < 10:
            continue
        X = np.zeros((N,1))
        for i in range(0,N):
            X[i,0] = data[i][0]
        Mu,Sigma,Alpha = GMM2(X)
        print(Sigma)
        #res = minEdist(X)
        myCentroid, clustAssing = kMeans(X,2)
        Centroid = np.squeeze(np.asarray(myCentroid))
        mean = np.mean(X)
        sql = "update supnuevo_statistics.supnuevo_common_commodity set GMM1price = %s, GMM2price = %s, GMMpercent = %s, centroidPrice = %d, Kmeans1price = %s, Kmeans2price = %s, averagePrice = %s where codigo = '%s'" % ( Mu[0][0],Mu[0][1],Alpha[0][0],0,Centroid[0],Centroid[1],mean,codigo )  
        cur.execute(sql)
        conn.commit()
    conn.close()
