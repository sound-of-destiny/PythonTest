
def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return set(map(frozenset, C1))

def scanD(D, Ck, minSupport):
    ssCnt = {}          #存放候选项的出现次数
    numItems = len(D)   #数据集大小
    retList = []        #存放频繁项
    supportData = {}    #存放频繁项集支持度
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if can not in ssCnt.keys():
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    
    for key in ssCnt.keys():
        support = float(ssCnt[key])/float(numItems)
        if support >= minSupport:
            retList.append(key)
        supportData[key] = support

    return retList,supportData

def aprioriGen(Lk,k): #创建候选集Ck
    ##Lk为频繁项，k为项集元素个数
    retlist = []
    for i in range(len(Lk)-1):
        for j in range(i+1,len(Lk)):
            L1 = list(Lk[i])[:k-2]
            L1.sort()
            L2 = list(Lk[j])[:k-2]
            L2.sort()
            if L1 == L2:
                retlist.append((Lk[i] | Lk[j])) #集合并
    return retlist

def apriori(dataSet,minSupport=0.5):
    C1 = createC1(dataSet)
    D = list(map(set,dataSet))
    L1,supportData = scanD(D,C1,minSupport)
    L = [L1]
    k = 2

    while len(L[k-2]) > 0:
        Ck = aprioriGen(L[k-2],k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1

    return L,supportData
