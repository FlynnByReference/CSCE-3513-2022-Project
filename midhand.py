import psycopg2

##Class to connect
class connectToHeroku():
    def __init__(self): 
        pass
        
    def addPlayer(self, id, first_name, last_name, codename):
        ##Define variables for database
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.codename = codename
        
        ##Try for attempting to connect to database
        try:
            conn = psycopg2.connect(dbname="dehqhhni3itaso", user="uwurfbcdfmcdro", password="bc2ca24d7e3bd67fe8d33b46123ebc44d2353d32a15b11f54f56da50c640092d", host = "ec2-35-153-35-94.compute-1.amazonaws.com")
            cur = conn.cursor()
        except:
            print("Wasn't able to connect")
       
        
        ##Variables to execute entry to SQL
        sqlTest = "INSERT INTO player (id, first_name, last_name, codename) VALUES (%s, %s, %s, %s)"
        playerValues = (self.id, self.first_name, self.last_name, self.codename)
        
        ##Attempt to enter infor to player in db
        try:
            cur.execute(sqlTest, playerValues)
            conn.commit()
        except:
            print("Unable to add player")

        ##Disconenct from database
        conn.close()


