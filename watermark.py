# read pdf, read watermark, create new file, merge watermark pdf to new file 

from PyPDF2 import PdfFileWriter, PdfFileReader

pdf = PdfFileReader("PDF1.pdf")
watermark = PdfFileReader("watermark.pdf")

new_pdf = PdfFileWriter()

pageswatermark = watermark.getPage(0)
pagespdf = pdf.getNumPages()

for i in range(pagespdf):
    getPage = pdf.getPage(i)
    getPage.mergePage(pageswatermark)
    new_pdf.addPage(getPage)





openNewPdf = open("watermarkAdded.pdf", "wb")
new_pdf.write(openNewPdf)

openNewPdf.close()