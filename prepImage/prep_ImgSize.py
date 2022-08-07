from PIL import Image

input_loc = str(input("Enter the name of image located in demo/img in jpg format: "))

fullPathImg = "demo/img/" + input_loc + ".jpg"

basewidth = 256
img = Image.open(fullPathImg)
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)

pathtosave = 'demo/img/resized/' + input_loc + '_resized' '.jpg'
img.save(pathtosave)

print('Image resized successfully!')