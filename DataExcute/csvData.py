import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = '/home/schong/Documents/UploadData'
datelist = os.listdir(path)

for dates in datelist:
    merchantlist = os.listdir(path + '/' + dates)
    for merchants in merchantlist:
        timelist = os.listdir(path + '/' + dates + '/' + merchants)
        for times in timelist:
            filetype = os.path.splitext(times)[1]
            if filetype == '.dat':
                continue
            data = pd.read_csv(times)
            test = data[0]
            