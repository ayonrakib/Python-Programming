# take folder path as input and print all js file names only
# class File manipulation
# input: none
# str return: none
# method:
#   printJsFileNames
#   input: nothing
#   return: nothing, just print names of all js files
#   method:
#       1. jsFiles empty list
#       2. folderPath var e folder path input nibo
#       2. files list banabo folder path directory er sob file niye
#       3. files list er sob file er jonno:
#           1. last dot index er por theke str er shesh porjonto str jodi js er equal hoy:
#               1. jsFiles e append file
#       4. print jsFiles
#   1. jodi ei file ta execute hoy:
#      1. class theke object banabo
#       2. obj er printJsFiles method call
import os
class FileManipulation():
    def __init__(self) -> None:
        pass


    def __str__(self) -> str:
        pass


    def printJsFiles(self):
        jsFiles = []
        folderPath = input("Please insert the folder path: ")
        files = os.listdir(folderPath)
        for file in files:
            if file[file.rfind("."):] == ".js":
                jsFiles.append(file)
        print(jsFiles)


if __name__ == "__main__":
    fileManipulation = FileManipulation()
    fileManipulation.printJsFiles()