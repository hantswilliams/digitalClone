from PIL import Image
from io import BytesIO


def img_resizer_function(file):

    img = Image.open(BytesIO(file))
    
    basewidth = 256
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))

    resized_img = img.resize((basewidth,hsize), Image.ANTIALIAS)

    print('Image resized successfully!')

    return img, resized_img