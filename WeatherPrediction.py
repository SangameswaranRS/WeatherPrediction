import csv, pymysql
import requests,sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.covariance import EllipticEnvelope


db_name ="weather"
db_host = "localhost"
db_port = 3306
db_user = "root"
db_password = "sanga"
weatherCategoryList = []
def create_csv():
    global weatherCategoryList
    try:
        db = pymysql.connect(db_host, db_user, db_password, db_name)
        cursor = db.cursor()
        cursor.execute('select distinct(weatherCategory) from areaToFeaturesMap')
        weatherCategories = cursor.fetchall()
        if weatherCategories is not None:
            weatherCategoryList = []
            for i in range(0,len(weatherCategories)):
                weatherCategoryList.append(weatherCategories[i][0])
            updateDataQuery ='select lattitude,longitude, weatherCategory from area, areaToFeaturesMap where area.areaId = areaToFeaturesMap.areaId;'
            cursor.execute(updateDataQuery)
            results = cursor.fetchall()
            if results is not None:
                file = open("data.csv","w")
                writeList = []
                headers = ['lat','long','ctype']
                writeList.append(headers)
                for i in range(0, len(results)):
                    current = [results[i][0],results[i][1], weatherCategoryList.index(results[i][2])]
                    writeList.append(current)
                writer = csv.writer(file)
                writer.writerows(writeList)
                print('[INFO] CSV Generated.')
                return True
            else:
                print('[INFO] No results found. Unable to proceed')
                return False
        else:
            print('[Fatal] No weather categories found. Unable to proceed')
            return False
    except Exception as e:
        print('-[Fatal]-')
        print(e)
        return False

def predict():
    global weatherCategoryList
    lat = input('Enter Lat: ')
    lon = input('Enter Long: ')
    # Read the CSV.
    df = pd.read_csv("data.csv")
    # Features
    X= np.array(df.drop(["ctype"], 1))
    # Labels
    Y = np.array(df["ctype"])
    elliptic = EllipticEnvelope(contamination=0.15)
    elliptic.fit(X)
    outliner_detect = elliptic.predict([[lat,lon]])
    if outliner_detect == -1:
        print('Untrained area. Sorry unable to predict')
    else:
        clf = neighbors.KNeighborsClassifier(n_neighbors=len(weatherCategoryList))
        clf.fit(X,Y)
        print('[INFO] Classifier Trained')
        prediction = clf.predict([[lat,lon]])
        print('[RESULT] Prediction: '+ weatherCategoryList[prediction[0]])



create_csv()
predict()
