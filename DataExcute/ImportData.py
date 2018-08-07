import os
import struct

path = '/home/schong/Documents/Data/UploadData'
pathto = '/home/schong/Documents/Data/UploadData'
datelist = os.listdir(path)

def intBitsToFloat(b):
   s = struct.pack('>l', b)
   return struct.unpack('>f', s)[0]

def getIntFromByte(data, pos):
    accum = 0
    for shiftBy in range(2):
        accum |= (data[pos + shiftBy] & 0xff) << shiftBy * 8 
    return accum

def getCodigoFromBytes(data, pos, len):
    codigo = bytes.decode(data[pos:pos+len])
    return codigo

def getFloatFromBytes(data, pos):
    accum = 0
    for shiftBy in range(4):
        accum |= (data[pos + shiftBy] & 0xff) << shiftBy * 8 

    accum = intBitsToFloat(accum)
    return accum


dates = '20180719'
merchantlist = os.listdir(path + '/' + dates)
for merchants in merchantlist:
    Olddir = os.path.join(path + '/' + dates + '/' + merchants)
    file_data = open(Olddir,'rb')
    bindata = file_data.read()
    #bindata = bindata[44:]
    #bindata.split(0000 1010)
    cod = getIntFromByte(bindata, 0)
    codigo = getCodigoFromBytes(bindata, 2, 16)
    preciopub = getFloatFromBytes(bindata, 18)
    file_data.close()
