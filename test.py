from PIL import Image
import helpers


image = helpers.CropFace(helpers.getImagePath('face.jpg'))

image.show()
