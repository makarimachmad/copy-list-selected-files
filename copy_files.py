# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:12:31 2020

@author: FUJITSU
"""

import shutil
import os

asli = os.listdir("D:\\Koding\\Python\\Skripsi Daun Jati\\Daun Jati\\Perhutani\\ph1")
len(asli)
asli

resize = os.listdir("D:\Koding\Python\Skripsi Daun Jati\Daun Jati\Dataset\Resize\ph1")
len(resize)
resize

tujuan = r"D:\\Koding\\Python\\Skripsi Daun Jati\\Daun Jati\\dataset\\tujuan"


def listComplementElements(list1, list2):
    storeResults = []

    for num in list1:
        if num not in list2: # this will essentially iterate your list behind the scenes
            storeResults.append(num)

    return storeResults

bantu = listComplementElements(asli, resize)

print(bantu)
len(bantu)

for i in bantu:
    shutil.copy("D:\\Koding\\Python\\Skripsi Daun Jati\\Daun Jati\\Perhutani\\ph1\\"+i, tujuan)