# GDAL Processing tests framework

# import standard write rst function
import sys
sys.path.append('/home/matteo/lavori/qgis_test_script')

from write_rst import write_rst

# output file
gdal_path = "/home/matteo/lavori/qgis_test_script/lista_test_gdal.rst"


# dictionary of tests
d_gdal = {}

# manually update the updated (and merged! tests))
done_gdal = [
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
gdal_missing_path = "/home/matteo/lavori/qgis_test_script/missing_gdal.rst"
write_rst(gdal_missing_path, m_gdal)


# fill each key with other empty dict and values
for i in done_gdal:
    d_gdal[i] = {}



# manually enter informations on tests made, fails, notes...
# d_gdal['reprojectlayer']['test'] = ['yes']
# d_gdal['reprojectlayer']['commit'] = ['627ce52ef5857f5bdaa5857e44f48a9028585ca8']



# write the final rst file
write_rst(gdal_path, d_gdal)
