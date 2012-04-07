#Author: Pablo Moles
#Read the README for more information

''' ATENTION! You must have installed in your system the library pyPdf '''

from pyPdf import PdfFileReader
import os

print 'Give the path: '
f=open('pdfs.txt','w')
f.write(' --- With title --- \n')
nonsense=[]
for fileName in os.listdir(raw_input()):
    try:
        if fileName.lower()[-3:] == "pdf":
        	input1 = PdfFileReader(file(fileName, "rb"))
  		if not input1.getDocumentInfo().title:
			nonsense.append(fileName) 
        	else:
        		f.write(input1.getDocumentInfo().title+', '+input1.getDocumentInfo().author+'\n')
    except:
        print '!!!! ', fileName, ' has weird format, the document is not well-formed'
f.write('\n\n --- Without title --- \n')
for elem in nonsense:
	f.write(elem+'\n')
f.close()
