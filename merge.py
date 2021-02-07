from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_list = ["PDF1.pdf","PDF2.pdf"]


write_obj = PdfFileWriter()     # object for writing the file
for i in pdf_list:
    read_obj = PdfFileReader(i)   #object for reading the file
    pages = read_obj.getNumPages()        #gets number of pages by the object which reads the file
    # print(pages)

    for j in range(pages):
        read_EachPage = read_obj.getPage(j)                      #retrieves the page by the number of that page from the file   #pages number starts from 0
        write_obj.addPage(read_EachPage)                         #adds each page to the writing file which is created separatedly


openMergedFilePDF = open("merged.pdf", "wb")   #writing the file in binary code as its not text document
write_obj.write(openMergedFilePDF)