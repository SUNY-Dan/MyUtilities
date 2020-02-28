#!/bin/bash

for file in ./*.nii 
do        
    deepbrain-extractor -i "$file" -o  ../Prelim_mask/"$file"
    
done
