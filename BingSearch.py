from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials
import requests
from io import BytesIO
from PIL import Image


subscription_key = 'fce0f8d880f84085a5efebbb39639224'

assert subscription_key

def GetImage(search_term):
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "license": "public", "imageType": "photo"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    urls = [img["thumbnailUrl"] for img in search_results["value"][:1]]

    imagedata = requests.get(urls[0])
    imagedata.raise_for_status()
    image = Image.open(BytesIO(imagedata.content))
    image.save('images/bing.jpg')


