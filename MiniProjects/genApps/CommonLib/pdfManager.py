####################################33
#
# Pdf Manager : Do Operation from Pdf File.
#
######################################

class pdfManager:

  def mergePdf(flist=[],oname='merge.pdf'):
    " Take a list of paths "
    from PyPDF2 import PdfFileReader, PdfFileWriter
    output = PdfFileWriter()
    for p in flist[]
      pdfOne = PdfFileReader(file( p, "rb"))
      output.addPage(pdfOne.getPage(0)) 
    outputStream = file(oname, "wb")
    output.write(outputStream)
    outputStream.close()
    print 'Success: Merge'

  def bookMark():
    pass