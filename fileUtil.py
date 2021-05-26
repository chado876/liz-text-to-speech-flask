import speechUtil as speechUtil
import os
import glob
import PyPDF2
import docx2txt



def readFromFile(fileName):
    filePath = "uploads/" + fileName
    filetype = fileName.split('.')[-1]
    fileNameWithoutExt = ( fileName.rsplit( ".", 1 )[ 0 ] )

    if filetype == 'txt':
        with open(filePath,"r") as f:
            string = f.read()
            print("FILE TEXT IS: " + string)
            print(fileNameWithoutExt)
            speechUtil.synthesize_and_save_to_file(string, fileNameWithoutExt)
    elif filetype == 'pdf':
        output = ''
        pdfFileObj = open(filePath, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        totalPages = pdfReader.numPages
        for i in range(totalPages):
            page = pdfReader.getPage(i)
            output += page.extractText()
        print("PDF output is: " + output)
        speechUtil.synthesize_and_save_to_file(output, fileNameWithoutExt)
    elif filetype == 'docx':
        docxOutput = docx2txt.process(filePath)
        print("DOCX output is: " + docxOutput)
        speechUtil.synthesize_and_save_to_file(docxOutput, fileNameWithoutExt)

def clean_up_files():
    files = glob.glob('output/*')
    for f in files:
        os.remove(f)
    files2 = glob.glob('uploads/*')
    for f in files2:
        os.remove(f)
