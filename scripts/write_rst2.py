def write_rst2(outfile_path, dict_test, dict_missing, provider):
    '''
    Function that writes a *rst* file from a dictionary.
    It is aimed to write a *rst* file for the MISSING TEST provider
    
    Function loops and checks if in the missing dictionary are some algorithm
    also in the done dictionary and adds a defaul string if algorithm runs but
    test is not uploadable

    INPUT:
        outfile_path = path of the output file, replaces the existing file
        dict_test = provider dictionary of algorithms tested (both test run or not)
        dict_missing = provider dictionary of MISSING tests
        provider = provider string, 'qgis' or 'gdal'
    '''

    gh_link = 'https://github.com/qgis/QGIS/commit/'


    if provider == 'qgis':
        s = 'QGIS Algorithm list'
        h = '#' * len(s)
        # return s, h
    elif provider == 'gdal':
        s = 'GDAL Algorithm list'
        h = '#' * len(s)
        # return s, h

    f = open(outfile_path, 'w')

    f.write('{}\n{}\n{}\n\n'.format(h, s, h))

    for key in sorted(dict_missing.keys()):
        if key in sorted(dict_test.keys()):
            # if same key in both dictionary, add defaul string
            f.write('* **{}** -> algorithm works, test not uploadable \n'.format(key))
            f.write("\n")
            # if not just write the algorithm name
        else:
            f.write('* **{}** \n'.format(key))
            f.write("\n")

    f.close()
