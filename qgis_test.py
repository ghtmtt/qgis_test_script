# QGIS Processing tests framework

# import standard write rst function
import sys
sys.path.append('/home/matteo/lavori/qgis_test_script')

from write_rst import write_rst

# output file
qgis_path = "/home/matteo/lavori/qgis_test_script/done_committed_qgis.rst"

# empty dictionary of tests
d_qgis = {}

# manually update the updated (and merged! tests))
done_qgis = [
'reprojectlayer',
'variabledistancebuffer',
'adduniquevalueindexfield',
'linestopolygons',
'joinattributestable',
'countuniquepointsinpolygon',
'countpointsinpolygonweighted',
'pointsalonglines',
'meancoordinates',
'singlepartstomultipart',
'zonalstatistics'
]


# create list of missing tests to be done
# complete and raw list of algotihms
qgis_algs = processing.algList.algs['qgis']

# cleaned list of algorithms
all_qgis = []
for k, v in qgis_algs.items():
    all_qgis.append(k[5:])

# sort the list
all_qgis.sort()


# match the listo of done and all algorithms and create a list of missing one
missing_qgis = list(set(all_qgis) ^ set(done_qgis))
missing_qgis.sort()

# create dictionary of missing alg and write rst file

m_qgis = {}
for i in missing_qgis:
    m_qgis[i] = {}

# write the bullet rst file of missing algorithms
qgis_missing_path = "/home/matteo/lavori/qgis_test_script/missing_qgis.rst"
write_rst(qgis_missing_path, m_qgis)


# fill each key with other empty dict and values
for i in done_qgis:
    d_qgis[i] = {}

# dict keys guide
'''
test = 'yes', 'no', 'not uploadable yet'
parameter = parameters used during the test (e.g. 'standard', 'dissolve')
commit = commit(s) sha that are related to the test
ticket = if tickes have been opened during the test
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

d_qgis['countuniquepointsinpolygon']['test'] = ['yes']
d_qgis['countuniquepointsinpolygon']['commit'] = ['94856b59b1e711a6900c46c8815b7408da1cd4ac', '590abf0a4409d612712635374462561cbad34340']

d_qgis['countpointsinpolygonweighted']['test'] = ['yes']
d_qgis['countpointsinpolygonweighted']['commit'] = ['94856b59b1e711a6900c46c8815b7408da1cd4ac']

d_qgis['pointsalonglines']['test'] = ['yes']
d_qgis['pointsalonglines']['commit'] = ['2c6649358af613f8861e2a9f5b910c11b04c9af4']

d_qgis['meancoordinates']['test'] = ['yes']
d_qgis['meancoordinates']['commit'] = ['7958db29d116d0bfec462c155b3ffeb5e9f44e4e']

d_qgis['singlepartstomultipart']['test'] = ['yes']
d_qgis['singlepartstomultipart']['commit'] = ['c25907010228c1c5594e949362beb539c3639aaf']

d_qgis['zonalstatistics']['test'] = ['yes']
d_qgis['zonalstatistics']['commit'] = ['8994877717bbb0b3beb86ee6f53926e777eadcc9']


print(len(done_qgis))

# write the final rst file
write_rst(qgis_path, d_qgis)
