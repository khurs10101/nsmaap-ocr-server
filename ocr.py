import requests
from PIL import Image
from io import StringIO
from tesserocr import PyTessBaseAPI
import urllib

# column = Image.open('chin-emo.png')
# gray = column.convert('L')
# blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')
# blackwhite.save("chin-emo_bw.jpg")





def process_image(url):
    _get_image(url)
    column = Image.open('01.jpg')
    gray = column.convert('L')
    blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')
    blackwhite.save("sample.jpg")
    with PyTessBaseAPI() as api:
        api.SetImageFile('sample.jpg')
        return api.GetUTF8Text()
        


def _get_image(url):
    f = open('01.jpg','wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()