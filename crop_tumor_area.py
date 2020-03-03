from __future__ import division

import os
import random
import nibabel as nib
import numpy as np
from numpy import argwhere
from tqdm import tqdm
import csv
import pandas as ps


def creatfnameListfromcsv(fname):
    ds = ps.read_csv(fname)
   # print(ds.keys())
    patid = []

    patid = np.array(ds['BraTS19ID'].tolist())
    namelist = patid
   ## print(namelist)
    return namelist
	
	
## dataset location
original_location = './data_all/'
new_location = './data_all_cut_tumor/'
fname = 'survival_data_filtered.csv'
namelist = creatfnameListfromcsv(fname)

## nifti files list
original = []

## numpy arrays list
og_array = []
seg_array = []


	
## Converting nifti files into arrays - ORIGINAL
for dirName, subdirList, fileList in sorted(os.walk(original_location)):
    for filename in namelist:
        original.append(os.path.join(dirName, filename))
        original.sort()
    #print("Original: ", original)

for item in tqdm(original):
    img = nib.load(item+'_t2.nii')
    img_seg = nib.load(item+'_seg.nii')
    array = np.array(img.dataobj)
    array_seg = np.array(img_seg.dataobj)
    #print(array.shape)

    
    og_array.append(array)
    seg_array.append(array_seg)
## array is an array of 0,1 in the original image

## For each array in og_array, multiply it by the array in gt_array

with open('position.csv', mode='w') as PositionFile:
    position_writer = csv.writer(PositionFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in tqdm(range(len(og_array))):
        single_array = og_array[i]
        single_array_seg = seg_array[i]

        new_array = argwhere(single_array_seg)
        (xstart, ystart, zstart), (xstop, ystop, zstop) = new_array.min(0), new_array.max(0) + 1
        ##print(i+1,(xstart, ystart, zstart), (xstop, ystop, zstop))
    
        x_range = xstop - xstart
        y_range = ystop - ystart
        z_range = zstop - zstart

        (xc,yc,zc) = (int((xstart+xstop)/2), int((ystart+ystop)/2), int((zstart+zstop)/2))
        single_position = [str(original[i]),[xc,yc,zc], [xstart, ystart, zstart], [xstop, ystop, zstop]]
        position_writer.writerow(single_position)

    

        (x_size,y_size,z_size) = single_array.shape




        final_array = single_array[xstart:xstop, ystart:ystop, zstart:zstop]
        new_img = nib.Nifti1Image(final_array, None)
        print(i, ": ", final_array.shape)

        newfilename= new_location+ original[i].split('/')[2]
        nib.save(new_img, newfilename)


    

