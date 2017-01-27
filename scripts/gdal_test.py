# GDAL Processing tests framework

# import standard write rst function
import processing
import sys
import yaml

sys.path.append('/home/matteo/lavori/qgis_test_script/scripts')

from write_rst import write_rst
from write_rst2 import write_rst2


# output file
gdal_path = "/home/matteo/lavori/qgis_test_script/files/done_committed_gdal.rst"
# github path
gh_link = 'https://github.com/qgis/QGIS/commit/'



# yaml file from the repo, ALL THE TESTS MADE!
f = open('/home/matteo/lavori/QGIS/QGIS/python/plugins/processing/tests/testdata/gdal_algorithm_tests.yaml')
data_gdal = yaml.safe_load(f)
f.close()

# list of all the test in the repository yaml file
f_gdal = []

for k, v in data_gdal.items():
    for i in v:
        f_gdal.append(i['algorithm'][5:])


# dictionary of tests
d_gdal = {}

# manually update tests I MADE (and merged! tests))
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
### test not made but ticket opened
'rasterize',
'rasterize_over',
'contour',
'dissolvepolygons',
'buildvirtualraster'
]

# create list of missing tests to be done
# complete and raw list of algotihms
gdal_algs = processing.algList.algs['gdal']

# cleaned list of algorithms
all_gdal = []
for k, v in gdal_algs.items():
    all_gdal.append(k[5:])

# sort the list
all_gdal.sort()

# match the listo of done and all algorithms and create a list of missing one
missing_gdal = list(set(all_gdal) ^ set(f_gdal))
missing_gdal.sort()

# create dictionary of missing alg

m_gdal = {}
for i in missing_gdal:
    m_gdal[i] = {}


# fill each key with other empty dict and values
for i in done_gdal:
    d_gdal[i] = {}


# dict keys guide
'''
test = 'yes', 'no'
parameter = parameters used during the test (e.g. 'standard', 'dissolve')
commit = commit(s) sha that are related to the test
ticket = link of the related ticket
note = additional notes regarding the test
'''


# manually enter informations on tests made, fails, notes...

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


# write the final rst file
#write_rst(gdal_path, d_gdal, 'gdal')



s = 'GDAL Algorithm list'
h = '#' * len(s)
# return s, h

f = open(gdal_path, 'w')

f.write('{}\n{}\n{}\n\n'.format(h, s, h))


for key, value in sorted(d_gdal.items()):
    if d_gdal[key]['test'] == ['yes']:
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






#gdal_missing_path = "/home/matteo/lavori/qgis_test_script/files/missing_gdal.rst"
#write_rst2(gdal_missing_path, d_gdal, m_gdal, 'gdal')


# write the bullet rst file of missing algorithms
gdal_missing_path = "/home/matteo/lavori/qgis_test_script/files/missing_gdal.rst"
#write_rst2(gdal_missing_path, d_gdal, m_gdal, 'gdal')

f = open(gdal_missing_path, 'w')

f.write('{}\n{}\n{}\n\n'.format(h, s, h))

for key in sorted(m_gdal.keys()):
    if key not in d_gdal.keys():
        f.write('* **{}** \n'.format(key))
        f.write('\n')
    elif key in d_gdal.keys():
        if 'ticket' in d_gdal[key]:
            f.write('* **{}**: -> **BUG!!** see {} \n '.format(key, d_gdal[key]['ticket']))
            f.write('\n')
        if 'ticket' not in d_gdal[key]:
            f.write('* **{}**: -> algorithm works but problem with the test \n '.format(key))
            f.write('\n')

f.close()
