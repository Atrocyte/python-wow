import psycopg2 as psycopg2


class DbConnection:
    conn = psycopg2.connect("dbname=postgres user=postgres")
    cur = conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def setupDB(self):
        self.cur.execute("CREATE TABLE wow2 (id BIGSERIAL PRIMARY KEY, dinges integer, timestamp varchar, seq integer, avatarId integer, guild integer, level integer, race varchar, class varchar, zone varchar, anderedinges boolean, andergetal integer);")
        self.conn.commit()

    def insertCharacter(self, character):
        self.cur.execute("INSERT INTO wow2 (dinges, timestamp, seq, avatarId, guild, level, race, class, zone, anderedinges, andergetal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                         (character.dinges, character.timestamp, character.seq, character.id, character.guild, character.level, character.race, character.role, character.zone, character.watIsDit, character.anderGetal))

    def showDBContent(self):
        self.cur.execute("SELECT * FROM wow2;")
        for row in self.cur:
            print(row)

# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (666, "DINGEN*"))
#
# cur.execute("SELECT * FROM test;")
# for row in cur:
#     print(row)
#
# conn.commit()