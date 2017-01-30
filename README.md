QGIS Processing Test framework
==============================
This repository stores the updated list of algorithm added to the Processing core plugin of QGIS.

Providers tested are **QGIS core algorithms** and **GDAL algorithms**.

The `files` folder contains:

* updated list of tested algorithms: `done_xxx.rst`
* missing list of the algorithms: `missing_xxx.rst`
* list of the algorithms that have problems: `problem_xxx.rst`

- `done_committed_gdal.rst` contains the list of **QGIS algorithms**
- `done_committed_gdal.rst` contains the list of **GDAL algorithms**

All `rst` files are automatically created when a new test is added to the [QGIS](https://github.com/qgis/QGIS/) repository, respectively for [GDAL](https://github.com/qgis/QGIS/blob/master/python/plugins/processing/tests/testdata/gdal_algorithm_tests.yaml) and [QGIS](https://github.com/qgis/QGIS/blob/master/python/plugins/processing/tests/testdata/qgis_algorithm_tests.yaml)

Algorithms are tested for the upcoming **QGIS 3** release. QGIS is constantly compiled from source to take advantages of all the bug fixed and eventually other tested algorithms.

Whenever a test fails, e.g. due to a bug of the algorithm itself, a ticket is opened to inform the developers.

Some algorithms work fine but there are some problem with the tests: some algorithm are not suite for the testing framework (e.g. load layer into databases or some testing problem due to the local pc configuration).
All these algorithms are added to the `problem_xxx.rst` file with a note describing the problem.

For more information about the testing framework itself, please visit the page of the [QGIS repository](https://github.com/qgis/QGIS/tree/master/python/plugins/processing/tests) 
