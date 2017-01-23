# GDAL Processing tests framework

# import standard write rst function
import processing
import sys
sys.path.append('/home/matteo/lavori/qgis_test_script/scripts')

from write_rst import write_rst

# output file
gdal_path = "/home/matteo/lavori/qgis_test_script/files/done_committed_gdal.rst"


# dictionary of tests
d_gdal = {}

# manually update the updated (and merged! tests))
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
### test not made but ticket opened
'rasterize',
'rasterize_over'
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
missing_gdal = list(set(all_gdal) ^ set(done_gdal))
missing_gdal.sort()

# create dictionary of missing alg and write rst file

m_gdal = {}
for i in missing_gdal:
    m_gdal[i] = {}

# write the bullet rst file of missing algorithms
gdal_missing_path = "/home/matteo/lavori/qgis_test_script/files/missing_gdal.rst"
write_rst(gdal_missing_path, m_gdal, 'gdal')


# fill each key with other empty dict and values
for i in done_gdal:
    d_gdal[i] = {}



# manually enter informations on tests made, fails, notes...
# d_gdal['reprojectlayer']['test'] = ['yes']
# d_gdal['reprojectlayer']['commit'] = ['627ce52ef5857f5bdaa5857e44f48a9028585ca8']
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

## no tests but ticket opened
d_gdal['rasterize']['test'] = ['no']
d_gdal['rasterize']['ticket'] = ['http://hub.qgis.org/issues/16061']

d_gdal['rasterize_over']['test'] = ['no']
d_gdal['rasterize_over']['ticket'] = ['http://hub.qgis.org/issues/16061']




# write the final rst file
write_rst(gdal_path, d_gdal, 'gdal')
