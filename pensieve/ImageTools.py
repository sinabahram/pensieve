import cv2
import cv2.cv as cv


class ImageTools:
    image = None

    # Display and update image in a window
    def display(self):
        cv2.namedWindow("Image")
        while True:
            if self.image is not None:
                cv2.imshow("Image", self.image)
            cv2.waitKey(10)
