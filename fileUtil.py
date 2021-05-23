import speechUtil as speechUtil

def readFromFile(fileName):
    filePath = "uploads/" + fileName
    with open(filePath,"r") as f:
        string = f.read()
    print("FILE TEXT IS: " + string)
    speechUtil.synthesize(string)

    