# MIT License
#
# Copyright (c) 2026 Hector Palafox
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
dumbpy
======

A small statistics-oriented package providing simple utilities for working with
nested iterables of numeric values.

Public API
----------
mean
    Compute the arithmetic mean of numeric values.
stddev
    Compute the population standard deviation of numeric values.
median
    Compute the median of numeric values.
flatten
    Flatten a nested iterable into a one-dimensional list.
validate
    Flatten input and ensure all elements are numeric.
"""

from dumbpy.arithmetic_mean import arithmetic_mean
from dumbpy.median import median
from dumbpy.std_deviation import std_deviation
from dumbpy.support_functions import flatten_list
from dumbpy.support_functions import validate_list

__all__: list[str] = [
    "arithmetic_mean",
    "std_deviation",
    "median",
    "flatten_list",
    "validate_list"
]