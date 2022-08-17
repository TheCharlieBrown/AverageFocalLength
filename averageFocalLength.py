"""
The following program will calculate the average
focal length used in a group of images
"""

from exif import Image
from os import walk
from math import ceil

path = "C:\\Users\\Dean\\OneDrive - UNSW\\Photography\\Edits"

focalLengths = []

files = []

# Creates a list of files to be used for the calculation
for (dir_path, dir_names, file_names) in walk(path):
	files.extend(file_names)

for file in files:
	full_path = path + "/" + file

	# Opens the image file and reads the EXIF data
	try:
		with open(full_path, 'rb') as img_file:
			img = Image(img_file)
	except IOError:
		continue

	equivFocalLength = img.get("focal_length_in_35mm_film")
	standardFocalLength = img.get("focal_length")
	
	# If the 35mm equivalent focal length is available,
	# then use it, otherwise use the standard focal length.

	if equivFocalLength is not None:
		focalLengths.append(equivFocalLength)
	elif standardFocalLength is not None:
		focalLengths.append(standardFocalLength)

averageFocalLength = ceil(sum(focalLengths)/len(focalLengths))
print(averageFocalLength)

