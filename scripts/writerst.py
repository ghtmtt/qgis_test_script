def write_rst(done_path, problem_path, missing_path, dict_test, list_missing, list_done, provider):
    '''
    done_path = final path for all the done and committed algorithms
    problem_path = file for all the algorithm that have issues (with running or test)
    missing_path = simple list of missing algorithms, these need to be tested
    dict_test = provider dictionary test
    provider = provider string, 'qgis' or 'gdal'
    '''

    gh_link = 'https://github.com/qgis/QGIS/commit/'


    if provider == 'qgis':
        s = 'QGIS Algorithm list'
        h = '#' * len(s)
        ss = 'QGIS Algorithm with issues'
        hh = '#' * len(ss)
        sss = 'QGIS Missing Algorithm list'
        hhh = '#' * len(sss)
        # return s, h
    elif provider == 'gdal':
        s = 'GDAL Algorithm list'
        h = '#' * len(s)
        ss = 'GDAL Algorithm with issues'
        hh = '#' * len(ss)
        sss = 'GDAL Missing Algorithm list'
        hhh = '#' * len(sss)

    f = open(done_path, 'w')

    f.write('{}\n{}\n{}\n\n'.format(h, s, h))
    
    f.write('**{} tested algorithms**\n'.format(len(list_done)))
    f.write('\n\n')


    for key, value in sorted(dict_test.items()):
        if dict_test[key]['test'] == ['yes']:
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


    fproblem = open(problem_path, 'w')
    fproblem.write('{}\n{}\n{}\n\n'.format(hh, ss, hh))

    for key, value in sorted(dict_test.items()):
        if dict_test[key]['test'] == ['no']:
            fproblem.write('* **{}** algorithm or test not working!\n'.format(key))
            fproblem.write("\n")
            for k, v in sorted(value.items()):
                fproblem.write(' * {}: \n'.format(k))
                fproblem.write("\n")
                for i in v:
                    fproblem.write('  * {} \n'.format(i))
                    fproblem.write("\n")

    fproblem.close()

    ff = open(missing_path, 'w')

    ff.write('{}\n{}\n{}\n\n'.format(hhh, sss, hhh))

    for i in list_missing:
        ff.write('* **{}** \n'.format(i))
        ff.write('\n')

    ff.close()
