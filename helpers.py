import io
import os
import BingSearch

from PIL import Image
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account

creds = service_account.Credentials.from_service_account_file('/Users/andrewhirasawa/HackNC2018-a7ec909b5efa.json')
client = vision.ImageAnnotatorClient(credentials=creds)

def CropFace(img):
    cords = detectFace(img)
    image = Image.open(img)
    image = image.crop(cords)
    return image

def detectFace(img):
    # Loads the image into memory
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.face_detection(image=image)
    faces = response.face_annotations
    if len(faces)==0:
        return False

    for face in faces:
        xValues = []
        yValues = []
        for vertex in face.bounding_poly.vertices:
            xValues.append((vertex.x))
            yValues.append((vertex.y))

        cords = (xValues[0], yValues[0], xValues[1], yValues[2])
        return cords


def faceOnFace(img1, img2):
#     with io.open(img1, 'rb') as image_file1:
#         content1 = image_file1.read()
#
#
#     with io.open(img2,'rb') as image_file2:
#         content2 = image_file2.read()

    if detectFace(img1) != False:
        cords = detectFace(img1)
        image2 = Image.open(img2)
        image2 = image2.resize(calcSize(cords))
        image1 = Image.open(img1)
        image1.paste(image2, (cords[0],cords[1]))
        return image1
    else:
        return False

def objOnFace(img1, img2):
    with io.open(img1, 'rb') as image_file1:
        content1 = image_file1.read()


    with io.open(img2,'rb') as image_file2:
         content2 = image_file2.read()

    if detectFace(img1) != False:
        cords = detectFace(img1)
        image2 = Image.open(img2)
        image2 = image2.resize(calcSize(cords))
        image1 = Image.open(img1)
        image1.paste(image2, (cords[0], cords[1]))
        return image1
    else:
        return False

def calcSize(cords):
    width = cords[2] - cords[0]
    height = cords[3] - cords[1]
    return (width, height)


def getImagePath(name):
    return os.path.join(
        os.path.dirname(__file__),
        'images/{}'.format(name))


def getLabels(img):
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    descriptions = list()

    for label in labels:
        descriptions.append(label.description)

    return descriptions


def detectObjects(path):
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))