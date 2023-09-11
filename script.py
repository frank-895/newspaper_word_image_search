## THIS PROGRAM ANALYSES A ZIP FILE OF PAGES OF NEWSPAPER ARTICLES
## WHEN A WORD IS SEARCHED, THE PROGRAM DISPLAYS WHICH PAGES CONTAIN THE WORD
## AND ALL OF THE FACES THAT ARE ON THIS NEWSPAPER PAGE.

# load in libraries
import zipfile
from zipfile import ZipFile

import PIL
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

import math

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

def faces(image):
    ''' takes an image and returns a list of locations of faces in the image
        image: image in PIL format
        return: list of tuples containing the locations of the corners of each face in format (x1, y1, x2, y2)
        '''
    
    new_image = np.asarray(image) # convert to numpy array 
    list_faces = face_cascade.detectMultiScale(cv.cvtColor(new_image, cv.COLOR_BGR2GRAY), 1.3, minSize = (25,25), minNeighbors = 5)
    if list_faces != ():
        list_faces = list_faces.tolist() # convert to list from numpy array
    else: # if there are no faces in list_faces
        return list_faces
    new_list = []
    # face_cascade returns image in format (x,y,w,h), which is converted to (x1,y1, x2, y2) format
    for item in list_faces:
        new_list.append((item[0],item[1],item[0]+item[2],item[1]+item[3]))
    return new_list

def search_word(dic, word):
    ''' searches the dictionary for keys in which the word appears in the corresponding item.
    dic: the dictionary with each image as a key, word: the word to be searched for
    return: list of keys in which the word appears
    '''

    list_keys = []
    for key in dic.keys():
        # in this program, the words on the newspaper page are saved in the first index of the item
        if word in dic[key][1]:
            list_keys.append(key)
    return list_keys

def display_face(image, bounding_box):
    ''' returns a cropped version of the original image, as defined by the bounding box
    image: image in RGB format, bounding_box: in format (x1, y1, x2, y2)
    return: cropped version of original image
    '''

    cropped_image = image.crop(tuple(bounding_box))
    return(cropped_image)

def create_dict(zip_link):
    ''' creates a dictionary where each key is a newspaper page and each item is a list containing the 
    image, the words on the newspaper page, and the bounding boxes where faces are located.
    zip_link: the ZIP file containing multiple pages of a newspaper
    return: returns the dictionary described above
    '''
    strings_faces_dict = {}
    with ZipFile(zip_link) as myzip:
        for file in myzip.infolist():
            with myzip.open(file.filename) as myfile:
                image = Image.open(myfile)
                list_faces = faces(image)
                strng = pytesseract.image_to_string(image) # save text on each page to dictionary
                strings_faces_dict[file.filename] = [image, strng, list_faces]
    return strings_faces_dict

def contact_sheet(zip_link, word, max_size):
    ''' creates and displays a contact sheet for each newspaper page a certain word appears in.
    zip_link: the ZIP file containing multiple pages of a newspaper,
    word: the word to be searched for in each newspaper page,
    max_size: the size each image should appear to the user.
    return: no return, just displays to user.
    '''
    strings_faces_dict = create_dict(zip_link)
    list_keys = search_word(strings_faces_dict, word)
    for key in list_keys:
        print("Results found in file {}".format(key))
        x = 0
        y = 0
        if strings_faces_dict[key][2] != ():
            sheet = PIL.Image.new("RGB", (max_size[0] * 5, max_size[1] * math.ceil(len(strings_faces_dict[key][2]) / 5)))
            for box in strings_faces_dict[key][2]:
                new_face = display_face(strings_faces_dict[key][0], box)
                new_face.thumbnail(max_size)
                sheet.paste(new_face, (x, y))
                if x + max_size[0] == sheet.width:
                    x = 0
                    y = y + max_size[1]
                else:
                    x = x + max_size[0]
            display(sheet)
        else:
            print("But there were no faces in that file!")
                    
        
# Test program
max_size = (100, 100)
print('CONTACT SHEET FOR "CHRISTOPER"')
contact_sheet("readonly/small_img.zip", "Christopher", max_size)
print('CONTACT SHEET FOR "MARK"')
contact_sheet("readonly/images.zip", "Mark", max_size)