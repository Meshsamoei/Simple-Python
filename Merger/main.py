import PyPDF2
import sys
from sys import argv
import os
import time

merger = PyPDF2.PdfFileMerger()

# if files.endswith(".pdf"):
#     merger.append(files)
# merger.write("AllPdf.pdf")

# time.sleep(.5)

# print(">> Pdf merged...!")
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("AllPdf.pdf") 
    print(">> Pdf merged...!")