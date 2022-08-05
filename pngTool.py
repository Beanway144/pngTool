import os
from PIL import Image

dir = input("> Enter directory path (do not end input with a slash): ")
pngList = []

for file in os.listdir(dir):
    if file.endswith(".png"):
        pngList += [dir + "/" + file]
print(pngList)
for path in pngList:
    img = Image.open(path)
    rgba = img.convert("RGBA")
    datas = rgba.getdata()
    newData = []

    for item in datas:
        if item[0] > 250 and item[1] > 250 and item[2] > 250:  # finding black colour by its RGB value
            # storing a transparent value when we find a black colour
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)  # other colours remain unchanged
  
    rgba.putdata(newData)
    rgba.save(path, "PNG")

print("Done! Modified files: ")
for path in pngList:
    print(path)