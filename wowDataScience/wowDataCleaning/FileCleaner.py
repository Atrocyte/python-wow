import re


class FileCleaner:


    def transformPersistentStorageToList(self, textFile):
        onlyStoragePart = textFile.split("RoundInfo")[0]
        lastBracketRemoved = onlyStoragePart.split("}")[0]
        lines = []
        for line in lastBracketRemoved.split(sep="\t")[1:]:
            lines.append(line)
        return lines

    def cleanStorageEntries(self, persistentStorageList):
        cleanedEntries = []
        for line in persistentStorageList:
            result = re.sub(r"\[\d*\] = ", "", line)        #removing the "[number] ="
            result = re.sub(r"\"", "", result)              #removing the double quotes
            result = result[:-2]                            #removing the trailing comma
            cleanedEntries.append(result)
        return cleanedEntries