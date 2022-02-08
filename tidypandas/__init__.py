# flake8: noqa
import importlib

# hard dependencies
hard_dependencies = ["pandas", "pandas_flavor"]

for dep in hard_dependencies:
    try:
        importlib.import_module(dep)
    except ImportError:
        print(f"Could not import {dep}")

try:
    import pandas as pd
except ImportError:
    print("Could not import pandas.")

# grouping
from tidypandas.grouping import add_count
