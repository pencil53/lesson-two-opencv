import cv2
#imread, to read image
#imread_color(1) used for loading images with color use 
#imread_greyscale(0) used for loading images in greyscale
#imread_unchanged(-1) used for loading without change
#imshow, to show image to me 2 parameters, the window in displat, and the image in display
#waitKey(0), image shown on screen until key pressed
#destroy all windows, does what it says

#read & display an image without changes 
"""
image= cv2.imread("Mango.jpg")
cv2.imshow("Tree", image)
cv2.waitKey(0)

#displaying in greyscale
image1= cv2.imread("Mango.jpg",0)
cv2.imshow("Tree1", image1) 
cv2.waitKey(0)

"""
#save image using opencv after mods
"""
image_path="C:/Users/akshu/Downloads/Coconut_Palm_9.jpg"
image2= cv2.imread(image_path,0)
cv2.imshow("coconut", image2)
cv2.imwrite("greycoconut.jpg",image2)
cv2.waitKey(0)
"""

#loading jackfruit in color
image3= cv2.imread("Jackfruit.jpg",1)
#splitting image to 3 colors BGR
b,g,r= cv2.split(image3)
cv2.imshow("Tree2",image3)
cv2.waitKey(0)
cv2.imshow("Treeblue", b)
cv2.waitKey(0)
cv2.imshow("Treeblue", g)
cv2.waitKey(0)
cv2.imshow("Treeblue", r)
cv2.waitKey(0)
cv2.destroyAllWindows()