import cv2
import os
import numpy as np
from PIL import Image


FACE_DETECTOR_PATH = "{base_path}/cascades/haarcascade_frontalface_default.xml".format(
    base_path=os.path.abspath(os.path.dirname(__file__)))

dataset_images_path="{base_path}/yalefaces/".format(
    base_path=os.path.abspath(os.path.dirname(__file__)))


face_cascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
# For face recognition we will the the LBPH Face Recognizer
recognizer = cv2.createLBPHFaceRecognizer()





class FaceRecognition :

	def get_images_and_labels(self,dataset_images_path):

	    # We will not read the image with the .sad extension in the training set
	    # Rather, we will use them to test our accuracy of the training
	    image_paths = [os.path.join(dataset_images_path, f) for f in os.listdir(dataset_images_path) if not f.endswith('.sad')]

	    # images will contains face images
	    images = []
	    # labels will contains the label that is assigned to the image
	    labels = []

	    for image_path in image_paths:
	        # Read the image and convert to grayscale
	        image_pil = Image.open(image_path).convert('L')
	        # Convert the image format into numpy array
	        image = np.array(image_pil, 'uint8')
	        # Get the label of the image
	        nbr = int (os.path.split(image_path)[1].split(".")[0].replace("subject", ""))

	        # Detect the face in the image
	        faces = face_cascade.detectMultiScale(image)
	        # If face is detected, append the face to images and the label to labels
	        for (x, y, w, h) in faces:
	            images.append(image[y: y + h, x: x + w])
	            labels.append(nbr)
	    # return the images list and labels list
	    return images, labels



	def recognizer_face(self,path_1):

	    predict_image_pil = Image.open(path_1).convert('L')

	    predict_image = np.array(predict_image_pil, 'uint8')

	    faces = face_cascade.detectMultiScale(predict_image)

	    for (x, y, w, h) in faces:
	        nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])

	    return nbr_predicted,conf

	def perform_recognition(self,image_path):
	

		images, labels=self.get_images_and_labels(dataset_images_path)
           
		recognizer.train(images, np.array(labels))

		num,confidence=self.recognizer_face(image_path)

		return num,confidence  



# def main():
# 	image_path = '/home/rams/Desktop/UI_task_List/Faces_recognistion/myproject/myapp/yalefaces/subject01.sad'
# 	obj=FaceRecognition()
# 	number,conf=obj.perform_recognition(image_path)
# 	print(conf)

# if __name__ == '__main__':
# 	main()
