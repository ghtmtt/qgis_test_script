# import modules
import processing
import yaml

##QGIS
qgis = processing.algList.algs['qgis']

# list of all the qgis test available
tutti_qgis = []
for k, v in qgis.items():
    tutti_qgis.append(k[5:])
    
# open the yaml file in the repo (pull the repo so list is updated))
f = open('/home/matteo/lavori/QGIS/QGIS/python/plugins/processing/tests/testdata/qgis_algorithm_tests.yaml')

data_qgis = yaml.safe_load(f)
f.close()

for k, v in data_qgis.items():
    qg = v

# list of all the already runned tests    
fatti_qgis = []
for i in qg:
    fatti_qgis.append(i['algorithm'][5:])

# compare and create list of missing tests
mancanti_qgis = list(set(tutti_qgis) ^ set(fatti_qgis))
# sort the list
mancanti_qgis.sort()

# dictionary of tests
d_qgis = {}

# fill each key with other empty dict and values
for i in mancanti_qgis:
    d_qgis[i] = {
    'test':[],
    'parameter':[],
    'commit':[],
    'ticket':[], 
    'note':[]
    }


# write rst file
f = open("/home/matteo/lavori/qgis_test_script/lista_test_qgis.rst", 'w')


for key, value in sorted(d_qgis.items()):
    f.write('* **{}** \n'.format(key))
    f.write("\n")
    for k, v in sorted(value.items()):
        f.write(' * {}: \n'.format(k))
        f.write("\n")
        for i in v:
            f.write('  * {} \n'.format(i))
            f.write("\n")

f.close()

