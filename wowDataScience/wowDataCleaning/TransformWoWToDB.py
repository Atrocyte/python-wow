from wowDataCleaning.DbConnection import DbConnection
from wowDataCleaning.FileCleaner import FileCleaner
from wowDataCleaning.FileGrabber import FileGrabber
from wowDataCleaning.Parsing import ParseResult



class WoWDataToDBTransformer:
    parser = ParseResult()
    con = DbConnection()
    file = FileGrabber()
    clean = FileCleaner()
    rootFolder = "D:\\Mendelt\\Data\\Datasets\\WoWAH\\"

    con.setupDB() #activeer deze bij db schema wijzigingen

    def readFile(self):
        print("Scanning files...")
        allPaths = self.file.getPathsOfAllTxtFilesInDirectory(self.rootFolder)
        cleanEntries = []
        for file in allPaths:
            textFile = self.file.makeStringFromFile(file);
            entries = self.clean.transformPersistentStorageToList(textFile)
            cleanEntries.extend(self.clean.cleanStorageEntries(entries))
        return cleanEntries

    def printDb(self):
        self.con.cur.execute("SELECT * FROM test;")
        for row in self.con.cur:
            print(row)

    def inserMutipleDBObjects(self, entriesFromFile):
        print("dingen" + 1) #breaker tegen extra insert
        print("inserting characters into database...")
        for entry in entriesFromFile:
            unit.insertDBObject(entry)
        print("insert done, committing...")
        self.con.conn.commit()
        # self.con.showDBContent()
        self.con.conn.close()

    def insertDBObject(self, dbEntry):
        character = self.parser.parse(dbEntry)
        self.con.insertCharacter(character)





unit = WoWDataToDBTransformer()
entriesFromFile = unit.readFile()
unit.inserMutipleDBObjects(entriesFromFile)
# proces gebruikt zo'n 6gb RAM en duurt minstens ~80min, nog voor de select. de commits gaan niet heel snel lijkt het
# bij de select ging RAM gebruik naar de max, waardoor er moest worden geswapt


