from re import split

entry1 = str('0, 01/01/06 00:09:38, 1,407, , 1, Orc, Hunter, Durotar, no, 0')
entry2 = str('0, 01/01/06 00:09:38, 1,0, , 5, Orc, Warrior, Durotar, no, 0')
entry3 = str('0, 01/01/06 00:09:44, 2,6, , 18, Orc, Warlock, Orgrimmar, no, 0')


# print(inputString)

class ParseResult:
    dinges = int
    time = ""
    seq = int
    id = int
    guild = int
    level = int
    race = ""
    role = ""
    zone = ""
    watIsDit = bool
    anderGetal = int

    def __repr__(self):
        return str(self.id) + " " + self.race + " " + self.role + " " + str(self.level)

    def parse(self, input):
        pattern = ","
        result = split(pattern, input)

        # replace all empty values with -1
        i = 0
        for element in result:
            if element == " ":
                result[i] = "-1"
            # print(str(i) + str(result[i]))
            i += 1

        self.dinges = int(result[0].strip())
        self.timestamp = result[1].strip()
        self.seq = int(result[2].strip())
        self.id = int(result[3].strip())
        self.guild = int(result[4].strip())
        self.level = int(result[5].strip())
        self.race = result[6].strip()
        self.role = result[7].strip()
        self.zone = result[8].strip()
        self.watIsDit = bool(result[9].strip())
        self.anderGetal = int(result[10].strip())
        return self

# dinges = ParseResult().parse(entry1)
# dinges2 = ParseResult().parse(entry2)
# dinges3 = ParseResult().parse(entry3)
#
# print(dinges)
# print(dinges2)
# print(dinges3)
