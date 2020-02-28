import os
import csv

mydir = r'/data/scratch/dan/ADNI0/5pt_rename'

i = 44;

with open("5pt_rename.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'name', 'speed'])
    for parent, dirnames, filenames in os.walk(mydir):
        for filename in filenames:
            print(os.path.join(parent, filename))
            newname = str(i)+'.nii'
            writer.writerow([newname, filename, '1'])
            os.rename(os.path.join(parent, filename), os.path.join(parent, newname))
            i +=1
