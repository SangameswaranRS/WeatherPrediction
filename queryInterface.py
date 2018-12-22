import pymysql

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
year = input('Enter Year: ')
yearlyAverageSQL = 'select avg(mercuryContent) as average from DatasetData where year=%s;'
cursor = databaseConnection.cursor()
cursor.execute(yearlyAverageSQL,(year))
yearlyAverage = cursor.fetchone()
if yearlyAverage is not None:
    print('[INFO] Yearly Average: '+str(yearlyAverage[0]))
else:
    print('[INFO] Data not found for year')
monthlyAverageSQL = 'select month, avg(mercuryContent) as average from DatasetData where year=%s group by month;'
cursor.execute(monthlyAverageSQL,(year))
results = cursor.fetchall()
if results is not None:
    print('[INFO] Monthly Average')
    for result in results:
        print(result)
else:
    print('[INFO] Data Not Found')
dailyAverageSQL='select date, avg(mercuryContent) as average from DatasetData where year=%s group by date;'
cursor.execute(dailyAverageSQL, year)
results = cursor.fetchall()
if results is not None:
    print('[INFO] Daily Average- Ordered by date')
    for result in results:
        print(result)
else:
    print('[INFO] Data not found')

