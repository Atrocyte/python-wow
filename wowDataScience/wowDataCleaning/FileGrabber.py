import os
from functools import reduce

import re

from os.path import join, isdir


class FileGrabber:

    rootDirectory = "D:\\Mendelt\\Data\\Datasets\\WoWAH\\"

    def returnTextFilesFrom(self, rootDirectory):
        self.rootDirectory = rootDirectory
        filenames = reduce(lambda x, y: x + y, [files for root, dirs, files in os.walk(self.rootDirectory)])  # gewoon gejat
        textFiles = []
        for name in filenames[0:25]:
            if (str(name).endswith("txt")):
                textFiles.append(str(name))
        return textFiles

    def printFileContents(self, file):
        text = open(file, "r")
        for line in text:
            result = re.sub(r".* \"", "\"", line)
            print(result)

    def makeStringFromFile(self, textFile):
        with open(textFile, "r", encoding="utf8") as resultingString:
            return resultingString.read()

    def getPathsOfAllTxtFilesInDirectory(self, rootDirectory):
        self.rootDirectory = rootDirectory
        monthFolders = self.grabDirectories(self.rootDirectory)
        dayFolders = []
        for sub in monthFolders:
            for result in self.grabDirectories(sub):
                dayFolders.append(result)

        # outputFile = open(join(rootDirectory, "allPaths.txt"), "w") #activate for textfile output of paths
        filePaths = []
        for directory in dayFolders:
            files = [join(directory, s) for s in os.listdir(directory)]
            for file in files:
                if str(file).endswith(".txt"):
                    filePaths.append(file)
                    # outputFile.write(file + "\n") #138083 lines
        return filePaths

    def grabDirectories(self, directory):
        return [join(directory, s) for s in os.listdir(directory) if isdir(join(directory, s))]

    def provideOutputFile(self, filename):
        return open(join(self.rootDirectory, (filename+".txt")), "w")