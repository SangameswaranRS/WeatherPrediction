import json, time,pymysql, requests

file  =open("city.list.json","r")
jsonContent = json.load(file)
API_KEY = "e07e61b5c6b8896605de5d46d5305230"
db_name ="weather"
db_host = "localhost"
db_port = 3306
db_user = "root"
db_password = "sanga"
print('--Extracting Indian cities--')
indianCitiesList = []
for iterator in jsonContent:
    if iterator["country"] == 'IN':
        indianCitiesList.append(iterator)
print('--Extraction Complete--')
print(str(len(indianCitiesList))+' Cities Extracted.')

# There is a restriction on the requests per minute in the openmap.org API
def extractCityBasedOnID(id):
    global API_KEY
    requestUrl = "https://api.openweathermap.org/data/2.5/weather?id="+str(id)+"&appid="+API_KEY
    res = requests.get(requestUrl)
    if res.status_code==200:
        return json.loads(res.content.decode('utf-8'))
    else:
        print('[Fatal] Request Failed with status Code:'+str(res.status_code))
        return None

def makeDatabaseEntry(geoData):
    try:
        db = pymysql.connect(db_host, db_user, db_password, db_name)
        cursor  = db.cursor()
        insertAreaQuery = "insert into area values(0, %s, %s)"
        cursor.execute(insertAreaQuery, (geoData["coord"]["lat"], geoData["coord"]["lon"]))
        area_id = cursor.lastrowid
        updateAreaFeaturesQuery = 'insert into areaToFeaturesMap values(%s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(updateAreaFeaturesQuery, (area_id, geoData["weather"][0]["main"],geoData["weather"][0]["description"],geoData["main"]["temp"], geoData["main"]["pressure"], geoData["main"]["temp_min"], geoData["main"]["temp_max"], geoData["dt"]))
        db.commit()
        print('Features Updated for Area Id'+str(area_id))
        return True
    except Exception as e:
        print('[Fatal] Exception')
        print(e)
        return False

# Extract some Indian cities and update them in database
for iterator in range(0,100):
    fetchId = indianCitiesList[iterator]["id"]
    geoData = extractCityBasedOnID(fetchId)
    if makeDatabaseEntry(geoData):
       print('Updated for Location Id'+str(fetchId))
    else:
        print('Error Updating '+ str(fetchId))
    time.sleep(5)

print('[OK] Features Updated in database') 

