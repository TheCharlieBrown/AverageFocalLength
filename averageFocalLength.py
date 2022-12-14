"""
The following program will calculate the average
focal length used in a group of images
"""
import sys, os
from exif import Image
from math import ceil

if (len(sys.argv) == 1):
	path = input("Enter path to image files: ")
elif (len(sys.argv) == 2):
	path = sys.argv[1]
else:
	sys.exit("Invalid number of arguments provided.\n \
	Usage: %s [path]\n" % sys.argv[0])

if (not os.path.exists(path)):
	sys.exit("path does not exist")


focalLengths = []

fullPaths = []

# Creates a list of filepaths to be used for the calculation
for dirPath, subDirs, files in os.walk(path):
	for file in files:
		if file.lower().endswith(".jpg"):
			fullPaths.append(os.path.join(dirPath, file))

for fullPath in fullPaths:
	# Opens the image file and reads the EXIF data
	with open(fullPath, 'rb') as imgFile:
		img = Image(imgFile)

	equivFocalLength = img.get("focal_length_in_35mm_film")
	standardFocalLength = img.get("focal_length")
	
	# If the 35mm equivalent focal length is available,
	# then use it, otherwise use the standard focal length.

	if equivFocalLength is not None:
		focalLengths.append(equivFocalLength)
	elif standardFocalLength is not None:
		focalLengths.append(standardFocalLength)

if (focalLengths):
	averageFocalLength = ceil(sum(focalLengths)/len(focalLengths))
	print(averageFocalLength)
else:
	print("No focal lengths available")

