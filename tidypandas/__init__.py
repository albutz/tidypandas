# flake8: noqa
import importlib

# hard dependencies
hard_dependencies = ["pandas", "pandas_flavor"]

for dep in hard_dependencies:
    try:
        importlib.import_module(dep)
    except ImportError:
        print(f"Could not import {dep}")

# clean up
del hard_dependencies, dep, importlib

# grouping
from tidypandas.grouping import add_count

# read
from tidypandas.read import read_sub
