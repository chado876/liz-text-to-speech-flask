import speechUtil as speechUtil

def readFromFile(fileName):
    filePath = "uploads/" + fileName
    with open(filePath,"r") as f:
        string = f.read()
    print("FILE TEXT IS: " + string)
    fileNameWithoutExt = ( fileName.rsplit( ".", 1 )[ 0 ] )
    print(fileNameWithoutExt)
    speechUtil.synthesize_and_save_to_file(string, fileNameWithoutExt)
    