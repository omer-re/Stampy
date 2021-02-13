# reference https://medium.com/@schedulepython/how-to-watermark-your-pdf-files-with-python-f193fb26656e

from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import os

"""
Refer to an image if you want to add an image to a watermark.
Fill in text if you want to watermark with text.
Alternatively, following settings will skip this.picture_path = None
text = None
"""
#picture_path = 'company_logo.png'
text = '203957741'  # Folder in which PDF files will be watermarked. (Could be shared folder)
file = r'C:\Users\omer.reuveni\Desktop\Album_scan\water\203957741.pdf'

def ID_stamp(orig_file_path, id_text):

    c = canvas.Canvas('watermark.pdf')

    # if picture_path:
    #     #c.drawImage(picture_path, 15, 15)
    #     if text:
    #         c.setFontSize(22)
    #         c.setFillColor('Red')
    #         c.setFont('Helvetica-Bold', 10)
    #         c.drawString(15, 15, text)
    #         c.save()
    if file.endswith(".pdf"): output_file = PdfFileWriter()
    input_file = PdfFileReader(open(file, "rb"))
    page_count = input_file.getNumPages()


    # get input dims
    (_,_,width,height)=input_file.getPage(0).mediaBox

    ######  Create new template with watermark ###
    c = canvas.Canvas('watermark.pdf')
    #if picture_path:
        #c.drawImage(picture_path, 15, 15)
    if text:
        c.setFontSize(22)
        c.setFillColor('Red')
        c.setFont('Helvetica-Bold', 12)
        c.drawString(15, height-20, text)
        c.save()

    watermark = PdfFileReader(open("watermark.pdf", "rb"))

    #########

    for page_number in range(page_count):
        input_page = input_file.getPage(page_number)
        input_page.mergePage(watermark.getPage(0))
        output_file.addPage(input_page)

        output_path = file.split('.pdf')[0] + '_watermarked' + '.pdf'
    with open(output_path, "wb") as outputStream:
        output_file.write(outputStream)


def remove_file():
    os.remove('watermark.pdf')

ID_stamp(file,text)
#remove_file()
print("Done")
