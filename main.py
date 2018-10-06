import io
import os

from PIL import Image
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account

creds = service_account.Credentials.from_service_account_file('/Users/andrewhirasawa/HackNC2018-a7ec909b5efa.json')
# Instantiates a client
client = vision.ImageAnnotatorClient(credentials=creds)

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'images/face.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
# response = client.label_detection(image=image)
# labels = response.label_annotations
#
# print('Labels:')
# for label in labels:
#    print(label.description)

image = vision.types.Image(content=content)

response = client.face_detection(image=image)
faces = response.face_annotations

# Names of likelihood from google.cloud.vision.enums
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                   'LIKELY', 'VERY_LIKELY')
print('Faces:')

for face in faces:
    print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
    print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
    print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in face.bounding_poly.vertices])

    print('face bounds: {}'.format(','.join(vertices)))
    print(type(face.bounding_poly.vertices))
    xValues = []
    yValues = []

    for vertex in face.bounding_poly.vertices:
        xValues.append((vertex.x))
        yValues.append((vertex.y))

    print(xValues)
    print(yValues)
    width = xValues[1] - xValues[0]
    height = yValues[2] - yValues[1]
    size = (width, height)

overlay = os.path.join(
    os.path.dirname(__file__),
    'images/apple.jpeg')

image1 = Image.open(file_name)
image2 = Image.open(overlay)

image2 = image2.resize(size)

image1.paste(image2, (xValues[0],yValues[0]))

image1.show()
