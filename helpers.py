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
    for face in faces:
        xValues = []
        yValues = []
        for vertex in face.bounding_poly.vertices:
            xValues.append((vertex.x))
            yValues.append((vertex.y))

        cords = (xValues[0], yValues[0], xValues[1], yValues[2])
        return cords

def calcSize(cords):
    width = cords[2] - cords[0]
    height = cords[3] - cords[1]
    return (width, height)

def getImagePath(name):
    return os.path.join(
        os.path.dirname(__file__),
        'images/{}'.format(name))

