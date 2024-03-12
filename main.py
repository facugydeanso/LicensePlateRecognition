import cv2 as cv
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class LicensePlateRecognition:
    #We know that license plates in Argentina have an aspect ratio of 400/130 = 3.07692307692. We also know they are rectangular. We can use this information to filter the contours.
    def __init__(self, min_w=80, max_w=110, min_h=25, max_h=52, ratio=400/130):
        self.min_w = min_w
        self.max_w = max_w
        self.min_h = min_h
        self.max_h = max_h
        self.ratio = ratio
    
    #The first step is to read the image
    def read_image(self, path):
        self.img = cv.imread(path)

    #Reading the image produces a BGR representation of it. We can convert it to a grayscale for easier processing.
    def convert_to_grayscale(self, img):
        return cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    #Binary Threshold helps us to convert the image to a binary image. This is important for the next step which is finding the contours.
    def binary_threshold(self, img):
        return cv.threshold(img, 150, 255, cv.THRESH_BINARY)[1]
    
    #We can find the contours to detect all the shapes in the image. It's important to filter results since hundreds of contours can be found in an image.
    def find_contours(self, img):
        return cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[0]
    
    def filter_contours(self, countors):
        filtered_countors = []
        for c in countors:
            x, y, w, h = cv.boundingRect(c)
            aspect_ratio = w / h
            if np.isclose(aspect_ratio, self.ratio, atol=0.5) and self.min_w <= w <= self.max_w and self.min_h <= h <= self.max_h:
                filtered_countors.append(c)
        return filtered_countors
    
    #The image is zoomed so we can only see the license plate.
    def crop_license_plate(self, img, countors):
        x, y, w, h = cv.boundingRect(countors[0])
        return img[y:y+h, x:x+w]
    
    def read_license_plate(self, path, i):
        alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        options = "-c tessedit_char_whitelist={}".format(alphanumeric)
        options += " --psm {}".format(8)

        img = cv.imread(path)
        gray = self.convert_to_grayscale(img)
        binary_license_plate = self.binary_threshold(gray)
        countors = self.find_contours(binary_license_plate)
        filtered_countors = self.filter_contours(countors)
        if not filtered_countors: 
            return "No license plate found"
        license_plate = self.crop_license_plate(binary_license_plate, filtered_countors)
        cv.imwrite(f"./licenses/license_plate_{i:03}.png", license_plate)
        text = pytesseract.image_to_string(license_plate, config=options)
        return text
