#!/bin/sh

# Evan Krell
# Script to label all `.jpg` images in directory based on filename string

# Define font
font="/home/ekrell/.local/share/fonts/Comfortaa/Comfortaa-VariableFont_wght.ttf"

# Read list of files (ignore already labeled)
filenames=($(ls *.jpg | grep -v -e "--labeled"))

for filename in ${filenames[@]}; do
	# Extract text to label image from image filename
	text=$(echo $filename | sed -e "s/__/@@/g" -e "s/_/ /g" -e "s/.jpg//" -e "s/\-[0-9]\+$//")
	# Create output filename
	outfile=$(echo $filename | sed -e "s/.jpg/--labeled${number}.jpg/") 
	# Label the image
	add_btmleft_image_text.py -i $filename -t "$text" -w $outfile -f $font
done
