import processing
import yaml

for k,v in processing.algList.algs.items():
    print(k)
    


##GDALOGR
gdal = processing.algList.algs['gdal']

# all gdal algorithms in Processing
tutti_gdal = []
for k, v in gdal.items():
    tutti_gdal.append(k[5:])
    
# open the repository file of the gdal tests already made
f = open('/home/matteo/lavori/QGIS/QGIS/python/plugins/processing/tests/testdata/gdal_algorithm_tests.yaml')

data_gdal = yaml.safe_load(f)
f.close()

for k, v in data_gdal.items():
    go = v
    
fatti_gdal = []
for i in go:
    fatti_gdal.append(i['algorithm'][5:])

mancanti_gdal = list(set(tutti_gdal) ^ set(fatti_gdal))
mancanti_gdal.sort()

f = open("/home/matteo/lavori/qgis_test_script/lista_test_gdal.csv", 'w')

for i in mancanti_gdal:
    f.write("{},\n".format(i))

f.close()




##QGIS
qgis = processing.algList.algs['qgis']

tutti_qgis = []
for k, v in qgis.items():
    tutti_qgis.append(k[5:])
    

f = open('/home/matteo/lavori/QGIS/QGIS/python/plugins/processing/tests/testdata/qgis_algorithm_tests.yaml')

data_qgis = yaml.safe_load(f)
f.close()

for k, v in data_qgis.items():
    qg = v
    
fatti_qgis = []
for i in qg:
    fatti_qgis.append(i['algorithm'][5:])

mancanti_qgis = list(set(tutti_qgis) ^ set(fatti_qgis))
mancanti_qgis.sort()

f = open("/home/matteo/lavori/qgis_test_script/lista_test_qgis.csv", 'w')

for i in mancanti_qgis:
    f.write("{},\n".format(i))
#    f.write("%s ',' \n"%i)

f.close()



