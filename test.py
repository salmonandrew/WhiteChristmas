from PIL import Image
import BingSearch
import pyperclip
import helpers


path1 = helpers.getImagePath('test2.jpg')

BingSearch.GetImage('walnut')

path2 = helpers.getImagePath('bing.jpg')

image = helpers.objOnFace(path1, path2)

image.show()






