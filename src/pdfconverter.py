# -*- coding: utf-8 -*-

import os

from fpdf import FPDF
from PIL import Image

def to_pdf(folder,destination,volume, manganame):
    volume = "Volume_" + volume
    print("[  " + volume + "  ] Converting all pictures downloaded to pdf")


    lista = os.listdir(folder)
    if(lista):
        with Image.open(os.path.join(folder ,str(len(lista)) + ".jpg")) as cover:
            width, height = cover.size

        pdf = FPDF(unit = "pt", format = [width, height])
        for i in range(1, len(lista)+1):
            img = str(i) + ".jpg"     
            pdf.add_page()
            try:
                pdf.image(os.path.join(folder , img), 0, 0)
            except RuntimeError as err:
                print("Error in image file {}. Skipping this image".format(str(err)))
                continue

        pdf.output(os.path.join(destination , manganame + "_" + volume + ".pdf"), "F")

        print("[  " + volume + "  ] Concluded with success.")
        print("[  " + volume + "  ] The pdf is inside your downloaded folder.")
        print("[  " + volume + "  ] Deleting all images in tmp folder...")

        for img in lista:
            os.remove(os.path.join(folder , img))

        print("Done\n")
    else:
        print("No files on tmp folder. Please make sure you found the correct url. \n")
         