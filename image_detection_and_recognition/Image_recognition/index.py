# USAGE
# python index.py --dataset dataset --index index.csv

# import the necessary packages
from my_imagesearch.colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "path the directory that conatins the images to be indexed")


args = vars(ap.parse_args())

# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))

# open the output index file for writing
output = open("index.csv", "w")

path='/home/rams/Desktop/UI_task_List/myproject1/myproject/myapp/dataset'

image_paths = [os.path.join(path, f) for f in os.listdir(path)]

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.png"):
#for imagePath in image_paths:
	# extract the image ID (i.e. the unique filename) from the image
	# path and load the image itself
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)

	# describe the image
	features = cd.describe(image)

	# write the features to file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()
