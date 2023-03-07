from PIL import Image, ImageEnhance, ImageFilter
import os
from pathlib import Path

before = "./Before"  #Before files
after = "./After"  #After files

print(">> Enter Constast factor. >> 1.0-2.0 recommended")
factor = float(input(">> "))
try:
    #Iterate and edit each image
    for filename in os.listdir(before):

        img = Image.open(f"{before}/{filename}")  ###Create image editing object & selecting each image for edits
        
        edit = img.filter(ImageFilter.SHARPEN)    ####edited image as edit

        enhance = ImageEnhance.Contrast(edit)  #enhance object
        edit = enhance.enhance(factor)   #Saving to edit
        plain = os.path.splitext(filename)[0]   #Extracting plain name w/out ext

        edit.save(f"{after}/{plain}.png")   ##Saving as _edited.png
        print(f"{plain}  edit complete...")
except:
    print("Integer only...")