from my_imagesearch.colordescriptor import ColorDescriptor
from my_imagesearch.searcher import Searcher
import cv2

path='/home/rams/Desktop/image_detection_and_recognition/Image_recognition/my_imagesearch/index.csv'


class Solution:

	def perform(self,root_1):
		cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
		query = cv2.imread(root_1)
		features = cd.describe(query)

		
		
# perform the search
		searcher = Searcher(path)
		results = searcher.search(features)
		
		return results

# display the query
		#cv2.imshow("Query", query)

# loop over the results
		#for (score, resultID) in results:
# load the result image and display it
			#result = cv2.imread(path1 + "/" + resultID)
			#cv2.imshow("Result", result)
			#cv2.waitKey(0)




