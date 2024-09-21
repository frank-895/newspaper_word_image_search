## Newspaper Word Image Search

**Description**

This Python program analyzes a ZIP file containing pages of newspaper articles. When a specific word is searched, it displays which pages contain that word and the faces found in the corresponding images. The program leverages Optical Character Recognition (OCR) for text extraction and employs face detection techniques to locate faces in the images.

**Features**

- Extracts text from images of newspaper articles using Tesseract OCR.
- Detects faces in the images using Haar Cascades.
- Searches for specified words in the extracted text and identifies relevant pages.
- Generates a contact sheet displaying the detected faces for pages containing the searched word.

**Requirements**

- Python 3.x
  
*Required Libraries:*

- zipfile
- PIL (Pillow)
- pytesseract
- opencv-python
- numpy
- Tesseract OCR installed and properly configured on your machine.

**Usage**

To use this program, ensure you have the required libraries installed and Tesseract OCR set up. Then, run the script with the following command:
```
python script.py
```

**Test Cases**

The script includes test cases for the following words:

- "Christopher"
- "Mark"

These will generate contact sheets displaying the results found in the specified ZIP files.

**Development Skills**

This project enhances the following skills:

- Image Processing: Gain experience in handling images and applying image analysis techniques.
- Optical Character Recognition (OCR): Learn how to extract text from images using Tesseract.
- Face Detection: Implement face detection using Haar Cascades, reinforcing knowledge of computer vision.
- Data Structures: Work with dictionaries and lists to store and manage image data and results.
- Modular Programming: Practice writing functions that encapsulate specific tasks for clarity and reusability.

**Acknowledgments**

This program is a final project for a Python3 Specialisation Course with the University of Michigan, showcasing the integration of multiple libraries and techniques for image processing and analysis.
