from PIL import Image
import helpers

path1 = helpers.getImagePath("angry.jpg")
image = helpers.getImagePath("face.jpg")
# image.save('images/test.jpg')

helpers.objOnFace(path1, helpers.getImagePath('bing.jpg')).show()



