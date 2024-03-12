# License Plate Recognition

This project focuses on license plate recognition using image processing techniques implemented with OpenCV and text recognition capabilities provided by Pytesseract. The goal is to extract license plate information from images automatically.


## Overview

License plate recognition involves several steps:

1. Grayscale Conversion: The input image is converted from color to grayscale, simplifying subsequent processing steps.

2. Binary Thresholding: A binary threshold operation is applied to the grayscale image to convert it into a binary (black and white) image. This step helps in emphasizing the features of interest, such as the characters on the license plate.

3. Contour Detection: Contours are identified in the binary image to locate potential regions of interest, which may correspond to license plates. Filtering is applied to select contours based on their aspect ratio, which is typical for license plates. This helps in discarding irrelevant contours and focusing on those likely to contain license plate information.

4. Plate Extraction: Once the relevant contour is identified, the image is cropped to extract only the region containing the license plate. This cropped image is then passed to Pytesseract for text extraction.

5. Text Recognition with Pytesseract: Pytesseract is employed to perform Optical Character Recognition (OCR) on the extracted license plate image. It attempts to recognize and extract the characters present on the plate.
## Limitations and Future Improvements

- Quality Dependency: The current model's performance heavily relies on the quality of input images. It is most effective with high-quality images and may struggle with low-resolution or noisy images.
- Character Recognition Accuracy: The model may inaccurately recognize characters, especially when they are similar in appearance. This can lead to errors in the extracted license plate information.
- Image Enhancement: Enhancements in image preprocessing and filtering techniques can be implemented to improve the clarity and quality of the extracted license plate images.


## Acknowledgements

This project draws inspiration and learning from the work of Santi Fiorino. A significant portion of the project's implementation is based on concepts and techniques presented in his repository. For more details, refer to [license-plate-recognition](https://github.com/santifiorino/license-plate-recognition).


