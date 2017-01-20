def write_rst(outfile_path, dict_test):
    '''
    path = path of the output file, replaces the existing file
    dict_test = provider dictionary test
    '''
    
    f = open(outfile_path, 'w')


    for key, value in sorted(dict_test.items()):
        f.write('* **{}** \n'.format(key))
        f.write("\n")
        for k, v in sorted(value.items()):
            f.write(' * {}: \n'.format(k))
            f.write("\n")
            for i in v:
                f.write('  * {} \n'.format(i))
                f.write("\n")

    f.close()