# Welcome to dumbpy

|  |  |
|------------------------------------|------------------------------------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/dumbpy.svg)](https://pypi.org/project/dumbpy/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/dumbpy.svg)](https://pypi.org/project/dumbpy/) |
| Meta | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI. If you don't plan to publish to PyPI, you can remove them.*

DumbPy is an alternative version of NumPy, which facilitates scientific computing using Python. DumbPy contains numeric functions that provide useful summary statistics of numerical lists, listed below. DumbPy additionally carries out strict input testing to provide clear and user-friendly error messages and facilitate proper usage.

DumbPy Functions:

-   `support_functions` - these functions will test the inputted object, and will catch any input besides a list of numbers and produce suitable error messages. Additionally, there will be a helper function that will take user input on whether to flatten an inputted list of lists into one list.

-   `arithmetic_mean` - the mean function will calculate and return the mean, or the average, of the inputted numerical list.

-   `std_deviation` - the standard deviation function will calculate and return the standard deviation of the inputted numerical list.

-   `median` - the median function will calculate and return the median value of the inputted numerical list

As stated above, the NumPy package already exists and provides similar functions. NumPy can be found at the following link: <https://numpy.org/>. DumbPy is an alternative version, which is much simpler and has a narrower focus.

## Contributors

-   Hector Prieto
-   Nicole Link
-   Samrawit Mezgebo

## Get started

You can install this package into your preferred Python environment using pip:

``` bash
$ pip install dumbpy
```

To use dumbpy in your code:

``` python
>>> import dumbpy
>>> dumbpy.arithmetic_mean([1,2,3])
2.0
```

## Copyright

-   Copyright © 2026 Hector Palafox.
-   Free software distributed under the [MIT License](./LICENSE).
