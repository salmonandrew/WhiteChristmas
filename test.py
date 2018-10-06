from PIL import Image
import helpers

path = helpers.getImagePath('apple.jpeg')

image = helpers.CropFace(helpers.getImagePath('face.jpg'))

helpers.localize_objects(path)
