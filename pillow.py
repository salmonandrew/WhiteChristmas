from PIL import Image
import os

file_name1 = os.path.join(
    os.path.dirname(__file__),
    'images/angry.jpg')

file_name2 = os.path.join(
    os.path.dirname(__file__),
    'images/face.jpg')

image1 = Image.open(file_name1)
image2 = Image.open(file_name2)

image2.show()

image1 = image1.resize((100,100))
image1.show()
image2.paste(image1, mask = None)
image2.show()
