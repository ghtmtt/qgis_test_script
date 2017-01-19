# import modules
import processing
import yaml


##GDALOGR
gdal = processing.algList.algs['gdal']

# list of all the qgis test available
tutti_gdal = []
for k, v in gdal.items():
    tutti_gdal.append(k[5:])
    
# open the yaml file in the repo (pull the repo so list is updated))
f = open('/home/matteo/lavori/QGIS/QGIS/python/plugins/processing/tests/testdata/gdal_algorithm_tests.yaml')

data_gdal = yaml.safe_load(f)
f.close()

for k, v in data_gdal.items():
    go = v

# list of all the already runned tests    
fatti_gdal = []
for i in go:
    fatti_gdal.append(i['algorithm'][5:])

# compare and create list of missing tests
mancanti_gdal = list(set(tutti_gdal) ^ set(fatti_gdal))
# sort the list
mancanti_gdal.sort()

# dictionary of tests
d_gdal = {}

# fill each key with other empty dict and values
for i in mancanti_gdal:
    d_gdal[i] = {
    'test':[],
    'parameter':[],
    'commit':[],
    'ticket':[], 
    'note':[]
    }


# write rst file
f = open("/home/matteo/lavori/qgis_test_script/lista_test_gdal.rst", 'w')


for key, value in sorted(d_gdal.items()):
    f.write('* **{}** \n'.format(key))
    f.write("\n")
    for k, v in value.items():
        f.write(' * {}: \n'.format(k))
        f.write("\n")
        for i in v:
            f.write('  * {} \n'.format(i))
            f.write("\n")

f.close()