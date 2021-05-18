# take folder path as input and print all js file names only
# printJsFileNames
# input: folder path as str
# return: nothing, just print names of all js files
# method:
#   1. jsFiles empty list
#   2. files list banabo path directory er sob file niye
#   3. files list er sob file er jonno:
#       1. dot index er por theke str er shesh porjonto str jodi js er equal hoy:
#           1. jsFiles e append file
#   4. print jsFiles
import os

def printJsFiles(filePath):
    files = os.listdir(filePath)
    jsFiles = []
    for file in files:
        if file[file.index("."):] == ".js":
            jsFiles.append(file)
    print(jsFiles)

filePath = 'D:/PythonProgramming/printjsfiles'
printJsFiles(filePath)