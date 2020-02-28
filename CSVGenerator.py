import os
import csv

mydir = r'/data/scratch/dan/ADNI0/5pt'

if __name__=='__main__':
    with open("5pt.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'speed'])

        for pathstr, dirlist, filelist in os.walk(mydir):
            for file in filelist:
                writer.writerow([file, '1'])

    f.close()

