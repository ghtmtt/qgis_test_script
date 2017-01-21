def write_rst(outfile_path, dict_test, provider):
    '''
    path = path of the output file, replaces the existing file
    dict_test = provider dictionary test
    '''

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


    for key, value in sorted(dict_test.items()):
        f.write('* **{}** \n'.format(key))
        f.write("\n")
        for k, v in sorted(value.items()):
            if k == 'ticket':
                f.write(' * {}: \n'.format(k))
                f.write("\n")
                for i in v:
                    f.write('  * <{}>_ \n'.format(i))
                    f.write("\n")
            else:
                f.write(' * {}: \n'.format(k))
                f.write("\n")
                for i in v:
                    f.write('  * {} \n'.format(i))
                    f.write("\n")

    f.close()
