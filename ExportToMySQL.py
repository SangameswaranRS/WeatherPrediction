# Export data to MySQL
# Command line argument - Path of the file
import sys,pymysql

#Database Credentials
db_name ="weather"
db_host = "localhost"
db_port = 3306
db_user = "root"
db_password = "sanga"
# Connect to MySQL
databaseConnection = pymysql.connect(db_host, db_user, db_password, db_name)
if databaseConnection is not None:
    print('[INFO] Connection established to MySQL instance')
else:
    print('[ERROR] Connection Failed.')
if len(sys.argv)<=1:
    print('[ERROR] Invalid Parameters')
else:
    print('[INFO] Opening '+ sys.argv[1])
    dataFile = open(sys.argv[1])
    print('[INFO] Processing data')
    for line in dataFile:
        try:
            cursor = databaseConnection.cursor()
            contents = line.split(' ')
            refinedContents = [content.replace('\n','') for content in contents if content != '']
            print(refinedContents)
            date = refinedContents[0]
            time = refinedContents[1]
            year, month, date = date.split('-')
            hours, minutes, seconds = time.split(':')
            typ = refinedContents[2]
            C = refinedContents[3]
            stat = refinedContents[4]
            ATim = refinedContents[6]
            vol = refinedContents[7]
            Bl = refinedContents[8]
            maxV = refinedContents[10]
            Area = refinedContents[11]
            mercuryContent = refinedContents[12]
            insertQuery = 'insert into DatasetData values(0, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s ,%s)'
            cursor.execute(insertQuery,(year,month,date,hours, minutes, seconds, typ, C, stat, ATim, vol, Bl, maxV, Area, mercuryContent))
            databaseConnection.commit()
        except Exception as E:
            print('[ERROR] Malformed Line')
            print(E)
    print('[INFO] Data conversion complete')
