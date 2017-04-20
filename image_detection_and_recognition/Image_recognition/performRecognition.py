#!/usr/bin/python

# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np


clf, pp = joblib.load("/home/rams/Desktop/image_detection_and_recognition/Image_recognition/digits_cls.pkl")
# Get the path of the training set


class DigitRecognizer:

    def perform(self,image_path):

       # Read the input image
        im = cv2.imread(image_path)

        # Convert to grayscale and apply Gaussian filtering
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

        # Threshold the image
        ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)


        # Find contours in the image
        ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        # Get rectangles contains each contour
        rects = [cv2.boundingRect(ctr) for ctr in ctrs]
        recognize_digit = []

        # For each rectangular region, calculate HOG features and predict
        # the digit using Linear SVM.
        for rect in rects:
            # Draw the rectangles
            cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
            # Make the rectangular region around the digit
            leng = int(rect[3] * 1.6)
            pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
            pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
            roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
            # Resize the image
            roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            roi = cv2.dilate(roi, (3, 3))
            # Calculate the HOG features
            roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
            roi_hog_fd = pp.transform(np.array([roi_hog_fd], 'float64'))

            nbr = clf.predict(roi_hog_fd)
            recognize_digit.append(nbr)
        #     cv2.putText(im, str(int(nbr[0])), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

        # cv2.namedWindow("Resulting Image with Rectangular ROIs", cv2.WINDOW_NORMAL)
        # cv2.imshow("Resulting Image with Rectangular ROIs", im)
        # cv2.waitKey()
        return recognize_digit



# def main():

#     img_path = '/home/rams/Desktop/image_detection_and_recognition/Image_recognition/photo_1.jpg'
#     mylist = []
#     obj = DigitRecognizer()
#     mylist = obj.perform(img_path)

#     for value in  mylist:
# 	   print(value)



# if __name__ == '__main__':
#     main()
