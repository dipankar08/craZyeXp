def Reverse():
  from pyPdf import PdfFileWriter, PdfFileReader
  output_pdf = PdfFileWriter()

  with open(r'input.pdf', 'rb') as readfile:
      input_pdf = PdfFileReader(readfile)
      total_pages = input_pdf.getNumPages()
      for page in xrange(total_pages - 1, -1, -1):
          print page
          page1= input_pdf.getPage(page);
          page1.rotateClockwise(180);
          page1.scale(2,2)
          output_pdf.addPage(page1)
      with open(r'output.pdf', "wb") as writefile:
          output_pdf.write(writefile)
          
def Merge():
  from pyPdf import PdfFileWriter, PdfFileReader
  output_pdf = PdfFileWriter()
  
  with open(r'input.pdf', 'rb') as readfile:
      input_pdf = PdfFileReader(readfile)
      total_pages = input_pdf.getNumPages()
      for page in xrange(total_pages - 1, -1, -2):
          print page
          page1 = input_pdf.getPage(page)
          page2 = input_pdf.getPage(page-1)
          page1.mergePage(page2)
          output_pdf.addPage(page1)
      with open(r'output.pdf', "wb") as writefile:
          output_pdf.write(writefile)
          
Reverse()
