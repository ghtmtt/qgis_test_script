# QGIS Processing tests framework

# import standard write rst function
import processing
import sys
import yaml

sys.path.append('/home/matteo/lavori/qgis_test_script/scripts')

from write_rst import write_rst
from write_rst2 import write_rst2


# output file
qgis_path = "/home/matteo/lavori/qgis_test_script/files/done_committed_qgis.rst"
# github path
gh_link = 'https://github.com/qgis/QGIS/commit/'

# yaml file from the repo, ALL THE TESTS MADE!
f = open('/home/matteo/lavori/QGIS/QGIS/python/plugins/processing/tests/testdata/qgis_algorithm_tests.yaml')
data_qgis = yaml.safe_load(f)
f.close()

# list of all the test in the repository yaml file
f_qgis = []

for k, v in data_qgis.items():
    for i in v:
        f_qgis.append(i['algorithm'][5:])

# empty dictionary of tests
d_qgis = {}

# manually update the updated (and merged! tests))
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
'randomextract'
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
missing_qgis = list(set(all_qgis) ^ set(f_qgis))
missing_qgis.sort()

# create dictionary of missing alg and write rst file

m_qgis = {}
for i in missing_qgis:
    m_qgis[i] = {}

# write the bullet rst file of missing algorithms
qgis_missing_path = "/home/matteo/lavori/qgis_test_script/files/missing_qgis.rst"
write_rst(qgis_missing_path, m_qgis, 'qgis')


# fill each key with other empty dict and values
for i in done_qgis:
    d_qgis[i] = {}


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
d_qgis['randomextract']['ticket'] = ['http://hub.qgis.org/issues/16069']


print(len(done_qgis))

# write the final rst file
#write_rst(qgis_path, d_qgis, 'qgis')


s = 'QGIS Algorithm list'
h = '#' * len(s)

f = open(qgis_path, 'w')

f.write('{}\n{}\n{}\n\n'.format(h, s, h))


for key, value in sorted(d_qgis.items()):
    if d_qgis[key]['test'] == ['yes']:
        f.write('* **{}** \n'.format(key))
        f.write("\n")
        for k, v in sorted(value.items()):
            if k == 'commit':
                f.write(' * {}: \n'.format(k))
                f.write("\n")
                for c in v:
                    f.write('  * {}{} \n'.format(gh_link, c))
                    f.write("\n")
            else:
                f.write(' * {}: \n'.format(k))
                f.write("\n")
                for i in v:
                    f.write('  * {} \n'.format(i))
                    f.write("\n")

f.close()




# write the bullet rst file of missing algorithms
#qgis_missing_path = "/home/matteo/lavori/qgis_test_script/files/missing_qgis.rst"
#write_rst2(qgis_missing_path, d_qgis, m_qgis, 'qgis')


# write the bullet rst file of missing algorithms
qgis_missing_path = "/home/matteo/lavori/qgis_test_script/files/missing_qgis.rst"
#write_rst2(gdal_missing_path, d_gdal, m_gdal, 'gdal')


f = open(qgis_missing_path, 'w')

f.write('{}\n{}\n{}\n\n'.format(h, s, h))

for key in sorted(m_qgis.keys()):
    if key not in d_qgis.keys():
        f.write('* **{}** \n'.format(key))
        f.write('\n')
    elif key in d_qgis.keys():
        if 'ticket' in d_qgis[key]:
            for t in d_qgis[key]['ticket']:
                f.write('* **{}**: -> **BUG!!** see {} \n '.format(key, t))
                f.write('\n')
        elif 'ticket' not in d_qgis[key]:
            f.write('* **{}**: -> algorithm works but problem with the test \n '.format(key))
            f.write('\n')

f.close()
