# tidypandas

![Tests](https://github.com/albutz/tidypandas/actions/workflows/tests.yml/badge.svg)

The `tidypandas` package is a conglomeration of useful helper function for data wrangling with `pandas`. It is (and per se will always be) work in progress as I add a function if

1. I construct roughly the same helper function in multiple (non-related) projects.
2. The function is nontrivial.

At the moment, `tidypandas` includes the following functions and methods:

- `pd.DataFrame.add_count()` augments the `DataFrame` operated on by a new column with group-wise counts and is inspired by `dplyr::add_count()` in R. 