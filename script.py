import psycopg2 
from psycopg2.extras import execute_values
from timeit import default_timer as timer
import random 
import sys
import string

def main(): 
    # startEntireProgram = timer()
    try:
        conn = psycopg2.connect(credentials)    #url to connect to the database server
    except:
        print("I couldn't connect to the server. Please check to be connected")
    else:
        continueTheScript(conn)

def continueTheScript(conn):
    cur = conn.cursor()

    _MAX_SAILOR = 1000000
    _MAX_BOAT = 1000000

    # Punto 1
    start = timer()
    cur.execute( 'DROP TABLE IF EXISTS "Sailor" CASCADE; DROP TABLE IF EXISTS "Boat";' )
    end = timer()
    print(' Step 1 needs %s ns' % str(round((end - start)*1000000000, 0)), file=sys.stdout)

    # Punto 2s
    start = timer()

    cur.execute( 'CREATE TABLE "Sailor" ( ' +
        '"id" INTEGER PRIMARY KEY,' +
        '"name" CHAR(50) NOT NULL,' +
        '"address" CHAR(50) NOT NULL,' +
        '"age" INTEGER NOT NULL,' +
        '"level" FLOAT NOT NULL);' )

    cur.execute( 'CREATE TABLE "Boat" ( ' +
        '"bid" CHAR(25) PRIMARY KEY,' +
        '"bname" CHAR(50) NOT NULL,' +
        '"size" CHAR(30) NOT NULL,' +
        '"captain" INTEGER NOT NULL REFERENCES "Sailor"("id"));' )
    end = timer()
    print(' Step 2 needs %s ns' % str(round((end - start)*1000000000, 0)), file = sys.stdout)

    # Punto 3
    start = timer()
    indexList = generazioneIndexList(_MAX_SAILOR)
    listSailorExecution = [
        [
            str(i),
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=50)),
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=50)),
            str(random.choice(range(1, 100))),
            str(val)
        ] for i, val in enumerate(indexList)
    ]
    listSailorExecution.append( #last tuple 
        [
            str(len(indexList)), 
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=50)),
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=50)),
            str(random.choice(range(1, 100))), 
            str(185)
        ])

    execute_values(cur,
            "INSERT INTO \"Sailor\" (id, name, address, age, level) VALUES %s",
            listSailorExecution)
    end = timer()
    print(' Step 3 needs %s ns' % str(round((end - start)*1000000000, 0)), file = sys.stdout)

    # Punto 4
    start = timer()
    # set boat index (bid)
    listBoatId = {(
            (''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=25)))
        ) for _ in range(_MAX_BOAT)
    }
    # list of indexes for captain
    random.shuffle(indexList)
    listBoatExecution = [
        [
            str(val), 
            str(random.choice(range(1,1000000))), 
            str(random.choice(range(1,1000000))), 
            str(indexList[i])
        ] for i, val in enumerate(listBoatId)
    ]

    execute_values(cur,
            "INSERT INTO \"Boat\" (bid, bname, size, captain) VALUES %s",
            listBoatExecution)
    end = timer()
    print(' Step 4 needs %s ns' % str(round((end - start)*1000000000, 0)), file = sys.stdout)

    # Punto 5
    stampaIdSailor(cur, 5)

    # Punto 6
    cambiaValoreLevel(cur, 185, 200, 6)
    # Punto 7
    idAddressSailor(conn, 200, 7)

    # Punto 8 
    start = timer()

    cur.execute("CREATE INDEX level_index ON \"Sailor\" (level);")
    end = timer()
    print(' Step 8 needs %s ns' % str(round((end - start)*1000000000, 0)), file = sys.stdout)

    # Punto 9
    stampaIdSailor(cur, 9)

    # Punto 10
    cambiaValoreLevel(cur, 200, 210, 10)

    # Punto 11
    idAddressSailor(conn, 210, 11)

    # Clean up
    conn.commit()
    cur.close()
    conn.close()


def stampaIdSailor(cur, numFunc):
    start = timer()
    cur.execute('SELECT id FROM \"Sailor\" ORDER BY id;')

    stringOut = ""
    for row in cur:
        stringOut += "%s,\n" % (row)
    print(stringOut[:-2], file = sys.stderr)

    end = timer()
    print(' Step %s needs %s ns' % (str(numFunc), str(round((end - start)*1000000000, 0))), file = sys.stdout)


def cambiaValoreLevel(cur, prima, dopo, numFunc):
    start = timer()
    cur.execute("UPDATE \"Sailor\" SET level = %s WHERE level = %s;" % (dopo, prima))
    end = timer()
    print(' Step %s needs %s ns' % (str(numFunc), str(round((end - start)*1000000000, 0))), file = sys.stdout)


def idAddressSailor(conn, valore, numFunc):
    start = timer()
    cur = conn.cursor('cursor_name_%s' % (numFunc), cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT id, address FROM \"Sailor\" WHERE level=%s;" % (valore))
    for row in cur:
        print("%s" % (row), file = sys.stderr) 
    cur.close()
    end = timer()
    print(' Step %s needs %s ns' % (str(numFunc), str(round((end - start)*1000000000, 0))), file = sys.stdout)


def generazioneIndexList(numRange):
    indexSet = { i for i in range(numRange) }
    indexList = list(indexSet)
    random.shuffle(indexList)
    return indexList



if __name__ == "__main__":
    main()
