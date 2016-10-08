from wowDataCleaning.DateParser import DateParser
from wowDataCleaning.DbConnection import DbConnection
from wowDataCleaning.FileGrabber import FileGrabber


class ReadingDb():
    connector = DbConnection()
    cur = connector.cur
    header = "ID,    dinges,       timestamp,   seq, avatarId, guild, level, race, class, zone, geenIdee, andergetal"

    def doSelect(self):
        self.cur.execute("SELECT count(timestamp) FROM wow2 WHERE avatarId = 53 AND zone = 'Ahn''Qiraj';")
        # print(self.header)
        resultingList = []
        for row in self.cur:
            print(row)
        #     resultingList.append(row)
        # print(resultingList)

        self.connector.close()

    def printQueryToFile(self, outputName):
        file = FileGrabber()
        output = file.provideOutputFile(outputName)
        print("writing file: " + outputName + ".txt")
        self.cur.execute("SELECT id FROM wow2 WHERE avatarId = 53;")

        for row in self.cur:
            output.write(row + "\n")

        print("closing connection")
        self.connector.close()



unit = ReadingDb()
date = DateParser()

# unit.doSelect()
unit.printQueryToFile("query1")

numberOfTimestamps = 444
date.toHours(numberOfTimestamps)
date.toDays(numberOfTimestamps)
