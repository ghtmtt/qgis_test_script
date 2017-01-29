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

# yaml file from the repo, ALL THE TESTS MADE!
f = open('/home/matteo/lavori/QGIS/QGIS/python/plugins/processing/tests/testdata/qgis_algorithm_tests.yaml')
data_qgis = yaml.safe_load(f)
f.close()

# list of all the test in the repository yaml file
f_qgis = []

for k, v in data_qgis.items():
    for i in v:
        f_qgis.append(i['algorithm'][5:])


# fill manually all the algorithm tested, EVEN IF TEST FAILS!
done_qgis = [
'reprojectlayer',
'variabledistancebuffer',
'adduniquevalueindexfield',
'linestopolygons',
'joinattributestable',
'convexhull',
'countuniquepointsinpolygon',
'countpointsinpolygonweighted',
'pointsalonglines',
'meancoordinates',
'singlepartstomultipart',
'zonalstatistics',
### test not made but ticket opened
'concavehull',
'randomextract',
'definecurrentprojection'
]

# add some missing algorithm to the f_gdal list
# e.g the algorithms that work but then the test fails
# this mathing is important to have a clean missing list (missing_gdal)
for i in done_qgis:
    if i not in f_qgis:
        f_qgis.append(i)


# create list of missing tests to be done
# complete and raw list of algotihms
qgis_algs = processing.algList.algs['qgis']

# cleaned list of algorithms
all_qgis = []
for k, v in qgis_algs.items():
    all_qgis.append(k[5:])
    all_qgis.sort()



# match the listo of done and all algorithms and create a list of missing one
# the missing list is updated from the repo and from both the correctly tested
# and the test that fails even if the algorithm works fine
missing_qgis = list(set(all_qgis) ^ set(f_qgis))
missing_qgis.sort()


# create empty dictionary that will be filled with the algorithms tested
d_qgis = {}
# fill each key with other empty dict and values
for i in all_qgis:
    d_qgis[i] = {'test':[]}



# manually enter informations on tests made, fails, notes...
# dict keys guide
'''
test = 'yes', 'no'
parameter = parameters used during the test (e.g. 'standard', 'dissolve')
commit = commit(s) sha that are related to the test
ticket = link of the related ticket
note = additional notes regarding the test
'''


# manually enter informations on tests made, fails, notes...
d_qgis['reprojectlayer']['test'] = ['yes']
d_qgis['reprojectlayer']['commit'] = ['627ce52ef5857f5bdaa5857e44f48a9028585ca8']

d_qgis['variabledistancebuffer']['test'] = ['yes']
d_qgis['variabledistancebuffer']['parameter'] = ['standard', 'dissolve']
d_qgis['variabledistancebuffer']['commit'] = ['627ce52ef5857f5bdaa5857e44f48a9028585ca8']

d_qgis['adduniquevalueindexfield']['test'] = ['yes']
d_qgis['adduniquevalueindexfield']['commit'] = ['627ce52ef5857f5bdaa5857e44f48a9028585ca8']

d_qgis['linestopolygons']['test'] = ['yes']
d_qgis['linestopolygons']['commit'] = ['627ce52ef5857f5bdaa5857e44f48a9028585ca8']

d_qgis['joinattributestable']['test'] = ['yes']
d_qgis['joinattributestable']['commit'] = ['627ce52ef5857f5bdaa5857e44f48a9028585ca8']

d_qgis['convexhull']['test'] = ['yes']
d_qgis['convexhull']['parameter'] = ['minimum hull', 'hull based on field']
d_qgis['convexhull']['commit'] = ['116e5674b0560a6ebd7ae1cf34770b7fb29829c2']

d_qgis['countuniquepointsinpolygon']['test'] = ['yes']
d_qgis['countuniquepointsinpolygon']['commit'] = ['94856b59b1e711a6900c46c8815b7408da1cd4ac', '590abf0a4409d612712635374462561cbad34340']

d_qgis['countpointsinpolygonweighted']['test'] = ['yes']
d_qgis['countpointsinpolygonweighted']['commit'] = ['94856b59b1e711a6900c46c8815b7408da1cd4ac']

d_qgis['pointsalonglines']['test'] = ['yes']
d_qgis['pointsalonglines']['commit'] = ['2c6649358af613f8861e2a9f5b910c11b04c9af4']

d_qgis['meancoordinates']['test'] = ['yes']
d_qgis['meancoordinates']['commit'] = ['7958db29d116d0bfec462c155b3ffeb5e9f44e4e']
d_qgis['meancoordinates']['ticket'] = ['http://hub.qgis.org/issues/16066']

d_qgis['singlepartstomultipart']['test'] = ['yes']
d_qgis['singlepartstomultipart']['commit'] = ['c25907010228c1c5594e949362beb539c3639aaf']

d_qgis['zonalstatistics']['test'] = ['yes']
d_qgis['zonalstatistics']['commit'] = ['8994877717bbb0b3beb86ee6f53926e777eadcc9']




## TEST RUN BUT NOT UPLOADABLE
d_qgis['concavehull']['test'] = ['no']
d_qgis['concavehull']['ticket'] = ['http://hub.qgis.org/issues/15985']

d_qgis['randomextract']['test'] = ['no']
d_qgis['randomextract']['note'] = ['output not uploadable for the test']
d_qgis['randomextract']['ticket'] = ['http://hub.qgis.org/issues/16069']

d_qgis['definecurrentprojection']['test'] = ['no']
d_qgis['definecurrentprojection']['note'] = ['output not uploadable for the test']


qgis_done_path = "/home/matteo/lavori/qgis_test_script/files/done_qgis.rst"
qgis_problem_path = "/home/matteo/lavori/qgis_test_script/files/problem_qgis.rst"
qgis_missing_path = "/home/matteo/lavori/qgis_test_script/files/missing_qgis.rst"

write_rst(qgis_done_path, qgis_problem_path, qgis_missing_path, d_qgis, missing_qgis, done_qgis, 'qgis')
