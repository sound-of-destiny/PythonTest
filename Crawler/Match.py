
import numpy as np

def levenshtein(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    dif = [([0]*(len1+1))for i in range(len2+1)]
    for a in range(len1+1):
        dif[0][a]=a
    for b in range(len2+1):
        dif[b][0]=b
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if str1[j-1] == str2[i-1]:
                temp = 0
            else:
                temp = 1
            dif[i][j] = min(dif[i-1][j-1]+temp,dif[i-1][j]+1,dif[i][j-1]+1)
    print(str1+" "+str2)
    similarity = 1 - dif[len2][len1]/max(len1,len2)
    print(similarity)
 

str1 = 'hello'
str2 = 'hellefewf'
levenshtein(str1,str2)