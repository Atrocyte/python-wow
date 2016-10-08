from datetime import date

exampleString = "03/17/06 22:33:25"

class DateParser:

    def toDays(self, int):
        sub = int * 10
        sub = sub / 60
        sub = sub /24
        print(str(sub) + " days")

    def toHours(self, int):
        sub = int * 10
        sub = sub / 60
        print(str(sub) + " hours")

    #doet niet
    def parseDate(self, string):
        result = date.fromtimestamp(string)
        print(date.today())
