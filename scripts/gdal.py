# GDAL Processing tests framework

# import standard write rst function
import processing
import yaml
import sys

sys.path.append('/home/matteo/lavori/qgis_test_script/scripts')

# import the writing function
from writerst import write_rst

# yaml file from the repo, ALL THE TESTS MADE!
f = open('/home/matteo/lavori/QGIS/QGIS/python/plugins/processing/tests/testdata/gdal_algorithm_tests.yaml')
data_gdal = yaml.safe_load(f)
f.close()

# list of all the test in the repository yaml file
f_gdal = []

# just clean the list to get the algorithm name
for k, v in data_gdal.items():
    for i in v:
        f_gdal.append(i['algorithm'][5:])


# fill manually all the algorithm tested, EVEN IF TEST FAILS!
done_gdal = [
'aspect',
'cliprasterbyextent',
'cliprasterbymasklayer',
'hillshade',
'slope',
'roughness',
'triterrainruggednessindex',
'nearblack',
'tpitopographicpositionindex',
'colorrelief',
'merge',
'proximity',
'rastercalculator',
'gridinvdist',
'griddatametrics',
'gridaverage',
'gridnearestneighbor',
### test not made but ticket opened
'rasterize',
'rasterize_over',
'contour',
'dissolvepolygons',
'buildvirtualraster',
'executesql',
'warpreproject',
'translate',
'clipvectorsbyextent',
'clipvectorsbypolygon',
'convertformat',
'assignprojection',
'extractprojection',
'importvectorintopostgisdatabaseavailableconnections',
'importvectorintopostgisdatabasenewconnection',
'importlayertableasgeometrylesstableintopostgresqldatabase',
'gdal2xyz',
'polygonize'
]

# add some missing algorithm to the f_gdal list
# e.g the algorithms that work but then the test fails
# this mathing is important to have a clean missing list (missing_gdal)
for i in done_gdal:
    if i not in f_gdal:
        f_gdal.append(i)


# create list of missing tests to be done
# complete and raw list of algotihms
gdal_algs = processing.algList.algs['gdal']

# cleaned list of ALL provider algorithms
all_gdal = []
for k, v in gdal_algs.items():
    all_gdal.append(k[5:])
    all_gdal.sort()



# match the listo of done and all algorithms and create a list of missing one
# the missing list is updated from the repo and from both the correctly tested
# and the test that fails even if the algorithm works fine
missing_gdal = list(set(all_gdal) ^ set(f_gdal))
missing_gdal.sort()


# create empty dictionary that will be filled with the algorithms tested
d_gdal = {}
# fill each key with other empty dict and values
for i in all_gdal:
    d_gdal[i] = {'test':[]}



# manually enter informations on tests made, fails, notes...
# dict keys guide
'''
test = 'yes', 'no'
parameter = parameters used during the test (e.g. 'standard', 'dissolve')
commit = commit(s) sha that are related to the test
ticket = link of the related ticket
note = additional notes regarding the test
'''


d_gdal['aspect']['test'] = ['yes']
d_gdal['aspect']['parameter'] = ['standard', '0 for flat', 'trigonometric angle', 'zevenbergen', 'with edges']
d_gdal['aspect']['commit'] = ['eab5ae28ec2a5dcbbccfd17d8d3ddda376b53c16', '6adbb8b7f5ba14326f83ce9b6eb72bc5']

d_gdal['cliprasterbyextent']['test'] = ['yes']
d_gdal['cliprasterbyextent']['parameter'] = ['standard', 'change NULL values']
d_gdal['cliprasterbyextent']['commit'] = ['eab5ae28ec2a5dcbbccfd17d8d3ddda376b53c16', '6adbb8b7f5ba14326f83ce9b6eb72bc5']

d_gdal['cliprasterbymasklayer']['test'] = ['yes']
d_gdal['cliprasterbymasklayer']['parameter'] = ['standard', 'change NULL values', 'add alpha band', 'no cropping line']
d_gdal['cliprasterbymasklayer']['commit'] = ['eab5ae28ec2a5dcbbccfd17d8d3ddda376b53c16', '6adbb8b7f5ba14326f83ce9b6eb72bc5']

d_gdal['hillshade']['test'] = ['yes']
d_gdal['hillshade']['parameter'] = ['standard', 'with edges', 'zevenbergen']
d_gdal['hillshade']['commit'] = ['eab5ae28ec2a5dcbbccfd17d8d3ddda376b53c16', '6adbb8b7f5ba14326f83ce9b6eb72bc5']

d_gdal['slope']['test'] = ['yes']
d_gdal['slope']['parameter'] = ['standard', 'with edges', 'zevenbergen', 'percent instead of degree']
d_gdal['slope']['commit'] = ['eab5ae28ec2a5dcbbccfd17d8d3ddda376b53c16', '6adbb8b7f5ba14326f83ce9b6eb72bc5']

d_gdal['roughness']['test'] = ['yes']
d_gdal['roughness']['parameter'] = ['standard', 'with edges']
d_gdal['roughness']['commit'] = ['64f2b660fdb34a447e072777727fe578dac44087']

d_gdal['triterrainruggednessindex']['test'] = ['yes']
d_gdal['triterrainruggednessindex']['parameter'] = ['standard', 'with edges']
d_gdal['triterrainruggednessindex']['commit'] = ['ad11ec4b7f04d5c3f6ff1bffb2f6fd48ba96bf70']

d_gdal['nearblack']['test'] = ['yes']
d_gdal['nearblack']['parameter'] = ['standard']
d_gdal['nearblack']['commit'] = ['1f645c19968603a443839a67dd2b7e9e526f2c76']

d_gdal['tpitopographicpositionindex']['test'] = ['yes']
d_gdal['tpitopographicpositionindex']['parameter'] = ['standard', 'with edges']
d_gdal['tpitopographicpositionindex']['commit'] = ['eb826fb058189cbfc43bc822bcd5088c198c090a']

d_gdal['colorrelief']['test'] = ['yes']
d_gdal['colorrelief']['parameter'] = ['standard', 'with edges']
d_gdal['colorrelief']['commit'] = ['4a60ef7c46c08016a9be0d8db6f06bf0dc15f977']

d_gdal['merge']['test'] = ['yes']
d_gdal['merge']['parameter'] = ['standard', 'separate into bands']
d_gdal['merge']['commit'] = ['765149466da5602b78101d0ef0395243fcaa001c']

d_gdal['proximity']['test'] = ['yes']
d_gdal['proximity']['parameter'] = ['standard']
d_gdal['proximity']['commit'] = ['1ada8e1a6c6c64524959bf06aa0a490ae777fbba']

d_gdal['rastercalculator']['test'] = ['yes']
d_gdal['rastercalculator']['parameter'] = ['standard']
d_gdal['rastercalculator']['commit'] = ['375c115beb7c7c8c7144aa76e578a623cebe17b1']

d_gdal['gridinvdist']['test'] = ['yes']
d_gdal['gridinvdist']['parameter'] = ['standard values']
d_gdal['gridinvdist']['commit'] = ['5480177c3c1b466be77c9ce93367d53af7d2398f']

d_gdal['griddatametrics']['test'] = ['yes']
d_gdal['griddatametrics']['parameter'] = ['standard values adjusted']
d_gdal['griddatametrics']['commit'] = ['294acffdae630763de41141f1e7ee5220e034783']

d_gdal['gridaverage']['test'] = ['yes']
d_gdal['gridaverage']['parameter'] = ['standard values adjusted']
d_gdal['gridaverage']['commit'] = ['641d287e72fec5774bd2fe84a6fef7d94e6e717b']

d_gdal['gridnearestneighbor']['test'] = ['yes']
d_gdal['gridnearestneighbor']['parameter'] = ['standard values adjusted']
d_gdal['gridnearestneighbor']['commit'] = ['7dfff4d42124aa50902e62263c33572fd083f69c']





## no tests but ticket opened
d_gdal['rasterize']['test'] = ['no']
d_gdal['rasterize']['ticket'] = ['http://hub.qgis.org/issues/16061']

d_gdal['rasterize_over']['test'] = ['no']
d_gdal['rasterize_over']['ticket'] = ['http://hub.qgis.org/issues/16061']

d_gdal['contour']['test'] = ['no']
d_gdal['contour']['note'] = ['GML output conflicts with the test, algorithm works fine']

d_gdal['dissolvepolygons']['test'] = ['no']
d_gdal['dissolvepolygons']['ticket'] = ['http://hub.qgis.org/issues/16122']

d_gdal['buildvirtualraster']['test'] = ['no']
d_gdal['buildvirtualraster']['ticket'] = ['http://hub.qgis.org/issues/16123']

d_gdal['executesql']['test'] = ['no']
d_gdal['executesql']['note'] = ['algorithms NOT working if output in GML']

d_gdal['warpreproject']['test'] = ['no']
d_gdal['warpreproject']['note'] = ['algorithm cannot run and reproject layers']

d_gdal['translate']['test'] = ['no']
d_gdal['translate']['note'] = ['cannot open the output']
d_gdal['translate']['ticket'] = ['http://hub.qgis.org/issues/16276']

d_gdal['clipvectorsbyextent']['test'] = ['no']
d_gdal['clipvectorsbyextent']['note'] = ['fails to open the output with the given drivers']
d_gdal['clipvectorsbyextent']['ticket'] = ['http://hub.qgis.org/issues/16277']

d_gdal['clipvectorsbypolygon']['test'] = ['no']
d_gdal['clipvectorsbypolygon']['note'] = ['fails to open the output with the given drivers']
d_gdal['clipvectorsbypolygon']['ticket'] = ['http://hub.qgis.org/issues/16277']

d_gdal['convertformat']['test'] = ['no']
d_gdal['convertformat']['note'] = ['mail at qgis dev, waiting']

d_gdal['assignprojection']['test'] = ['no']
d_gdal['assignprojection']['note'] = ['algorithm is not doing anything, mail at qgis dev, waiting']

d_gdal['extractprojection']['test'] = ['no']
d_gdal['extractprojection']['note'] = ['algorithm is not doing anything, mail at qgis dev, waiting']

d_gdal['importvectorintopostgisdatabaseavailableconnections']['test'] = ['no']
d_gdal['importvectorintopostgisdatabaseavailableconnections']['note'] = ['works, but output not uploadable for the test']

d_gdal['importvectorintopostgisdatabasenewconnection']['test'] = ['no']
d_gdal['importvectorintopostgisdatabasenewconnection']['note'] = ['not working and output not uploadable for the test']

d_gdal['importlayertableasgeometrylesstableintopostgresqldatabase']['test'] = ['no']
d_gdal['importlayertableasgeometrylesstableintopostgresqldatabase']['note'] = ['not working and output not uploadable for the test']

d_gdal['gdal2xyz']['test'] = ['no']
d_gdal['gdal2xyz']['note'] = ['seems working but dbf in output not suitable for the test']

d_gdal['polygonize']['test'] = ['no']
d_gdal['polygonize']['note'] = ['works also for GML output, but test fails due to CRS, also Alex made the test, no more in the code https://github.com/qgis/QGIS/commit/159fda68f2e3ac0c557a3b2e166dc24f95ad83ed#diff-21dd2d61eb16fd109e496b2a91abe493']



gdal_done_path = "/home/matteo/lavori/qgis_test_script/files/done_gdal.rst"
gdal_problem_path = "/home/matteo/lavori/qgis_test_script/files/problem_gdal.rst"
gdal_missing_path = "/home/matteo/lavori/qgis_test_script/files/missing_gdal.rst"

write_rst(gdal_done_path, gdal_problem_path, gdal_missing_path, d_gdal, missing_gdal, done_gdal, 'gdal')
