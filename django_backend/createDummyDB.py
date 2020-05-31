"""
columns of the csv
GRID_ID
X_COORDINATE_CENTER
Y_COORDINATE_CENTER
INJURED_LEVEL1
INJURED_LEVEL2
INJURED_LEVEL3
INJURED_LEVEL4

PersonInfo has the following attributes

number
status
    Guvende = 1
    ZorDurumda = 2
    GidaIhtiyaci = 4
    BezIhtiyaci = 8
    CadirIhtiyaci = 16
    EnkazAltindayim = 32
    KomsumdanSesGeliyor = 64
long
lat


if a row has value less than 1 for all injured sections
        status = guvende
        
        gida ihtiyaci with random %RANDOM_FOOD_RATIO

    for the number of people in injured levels
        create a new entry with:
            lat long addition with gaussion noise 
            GidaIhtiyaci =  %RANDOM_FOOD_RATIO
            BezIhtiyaci = %RADOM_BEZ_RATIO
            CadirIhtiyaci = %RANDOM_CADIR_RATIO
            
            if Injuredlevel1
                status = ZorDurumda
                
            if injured level2
                status = ZorDurumda
            
            if level3
                komsundansesgeliyor

            if level4
                enkazaltindayim

"""
import csv
import numpy as np
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


os.environ['DJANGO_SETTINGS_MODULE'] = 'deprem_backend.settings'
import django
django.setup()

from smsget.models import PersonInfo

filename = "population_injured.csv"


LAT_SIGMA = 0.005
LONG_SIGMA = 0.005




class StatusMap():
    Guvende = 1
    ZorDurumda = 2
    GidaIhtiyaci = 4
    BezIhtiyaci = 8
    CadirIhtiyaci = 16
    EnkazAltindayim = 32
    KomsumdanSesGeliyor = 64


db = []


id_additon_unique = 10000

def add_to_DB(num,stat,long,lat,txt):
    global id_additon_unique,db
    num_unique = num+str(id_additon_unique)
    id_additon_unique+=1
    num_unique_as_int = int(num_unique)
    entry = {'num':num_unique_as_int,'stat':stat,'long':long,'lat':lat,'txt':txt}
    db.append(entry)

def get_random_lat_long(lat,long):
    lat_offset = np.random.normal(0.0, LAT_SIGMA, 1)
    long_offset = np.random.normal(0.0, LONG_SIGMA, 1)
    final_long = long+long_offset[0]
    final_lat = lat+lat_offset[0]
    return final_lat,final_long



counter = 0
first_time = True
try:
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for row in csv_reader:
            if first_time:
                first_time = False;
                continue

            num = row[0]
            long = float(row[1])
            lat = float(row[2])
            level_1_num = int(float(row[3]))
            level_2_num = int(float(row[4]))
            level_3_num = int(float(row[5]))
            level_4_num = int(float(row[6]))

            # add a safe entry for each row
            entry_lat,entry_long = get_random_lat_long(lat,long)
            status = StatusMap.Guvende
            add_to_DB(num,status,entry_long,entry_lat,txt="")
            

            for i in range(level_1_num):
                entry_lat,entry_long = get_random_lat_long(lat,long)
                status = StatusMap.ZorDurumda
                add_to_DB(num,status,entry_long,entry_lat,txt="")

            for i in range(level_2_num):
                entry_lat,entry_long = get_random_lat_long(lat,long)
                status = StatusMap.ZorDurumda
                add_to_DB(num,status,entry_long,entry_lat,txt="")

            for i in range(level_3_num):
                entry_lat,entry_long = get_random_lat_long(lat,long)
                status = StatusMap.KomsumdanSesGeliyor
                add_to_DB(num,status,entry_long,entry_lat,txt="")
            
            for i in range(level_4_num):
                entry_lat,entry_long = get_random_lat_long(lat,long)
                status = StatusMap.EnkazAltindayim
                add_to_DB(num,status,entry_long,entry_lat,txt="")
              
             


except ImportError:
    raise ImportError("csv file not found")

print("finished execution")


"""
test_person = PersonInfo(num=5379125656,stat=1,lat=41.015,long=28.9784)
test_person.save()
test_person = PersonInfo(num=5379125657,stat=2,lat=41.1327,long=29.096)
test_person.save()
test_person = PersonInfo(num=5379125658,stat=64,lat=41.0575,long=28.9118,txt="3 saattir ses geliyor")
test_person.save()
test_person = PersonInfo(num=534625656,stat=13,lat=40.9978,long=29.0265)
test_person.save()
test_person = PersonInfo(num=537956,stat=32,lat=40.99511,long=29.099894,txt="dudugum var. evin banyo tarafindayim")
test_person.save()
"""

for entry in db:
    num = entry["num"]
    stat = entry["stat"]
    lat = entry["lat"]
    long = entry["long"]
    txt = entry["txt"]
    new_person = PersonInfo(num=num,stat=stat,lat=lat,long=long,txt=txt)
    new_person.save()
