import os
import csv

mydir = r'/data/scratch/dan/ADNI0/Prelim_mask'

if __name__=='__main__':
 
    for pathstr, dirlist, filelist in os.walk(mydir):
       # print(pathstr, dirlist, filelist)  
        for dir in dirlist:
            dirpath = os.path.join(pathstr,dir)
            newname = str(dir)
            os.rename(os.path.join(dirpath, "brain.nii"), os.path.join('/data/scratch/dan/ADNI0/Prelim_mask0',newname))



